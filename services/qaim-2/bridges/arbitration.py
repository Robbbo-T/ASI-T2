"""
ARB — Arbitration Bridge

Runtime adjustment and fallback handling using multi-armed bandits.
Monitors solver performance and switches if needed.

TFA Layer: FE (Federation)
"""

from typing import Dict, Any
import random
import math


class Arbitration:
    """
    Arbitration Bridge (ARB).
    
    Provides runtime adjustment and fallback handling using
    multi-armed bandit algorithms for dynamic solver selection.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize arbitration with configuration.
        
        Args:
            config: Configuration with algorithm, window_size, fallback
        """
        self.config = config
        self.enabled = config.get('enabled', True)
        self.algorithm = config.get('algorithm', 'ucb1')
        self.window_size = config.get('window_size', 1000)
        self.fallback = config.get('fallback', 'cb_glpk')
        
        # Track arm statistics
        self._arm_counts = {}
        self._arm_rewards = {}
        self._total_counts = 0
    
    def select_arm(self, context: Dict[str, Any]) -> str:
        """
        Select solver arm based on context and past performance.
        
        Args:
            context: Context with solver_type, features, system state
            
        Returns:
            Selected solver identifier
        """
        if not self.enabled:
            return context.get('solver_type', self.fallback)
        
        solver_type = context.get('solver_type')
        features = context.get('features', {})
        system_context = context.get('context', {})
        
        # Check if solver is available
        available_solvers = system_context.get('available_solvers', [])
        
        if solver_type not in available_solvers:
            # Fallback if requested solver not available
            return self._select_fallback(available_solvers)
        
        # Check system load
        load = system_context.get('load', 0.0)
        if load > 0.9:
            # Under high load, prefer faster solvers
            return self._select_fast_solver(available_solvers)
        
        # Apply MAB algorithm for refinement
        if self.algorithm == 'ucb1':
            refined = self._ucb1_select(solver_type, available_solvers)
        elif self.algorithm == 'thompson':
            refined = self._thompson_select(solver_type, available_solvers)
        else:
            refined = solver_type
        
        return refined
    
    def _select_fallback(self, available_solvers: list) -> str:
        """Select fallback solver."""
        # Try configured fallback first
        if self.fallback in available_solvers:
            return self.fallback
        
        # Otherwise, pick first available classical solver
        for solver in available_solvers:
            if solver.startswith('cb_'):
                return solver
        
        # Last resort: first available
        return available_solvers[0] if available_solvers else 'cb_glpk'
    
    def _select_fast_solver(self, available_solvers: list) -> str:
        """Select fast solver for high-load situations."""
        # Prefer simple classical solvers under load
        fast_solvers = ['cb_glpk', 'cb_cbc']
        
        for solver in fast_solvers:
            if solver in available_solvers:
                return solver
        
        return available_solvers[0] if available_solvers else 'cb_glpk'
    
    def _ucb1_select(self, solver_type: str, available_solvers: list) -> str:
        """
        UCB1 (Upper Confidence Bound) selection.
        
        Balances exploration and exploitation based on confidence intervals.
        """
        if self._total_counts == 0:
            return solver_type
        
        # Compute UCB score for each available solver
        best_solver = solver_type
        best_score = -float('inf')
        
        for solver in available_solvers:
            if solver not in self._arm_counts:
                # Unexplored arm: infinite UCB
                return solver
            
            count = self._arm_counts[solver]
            avg_reward = self._arm_rewards.get(solver, 0.0) / count
            
            # UCB1 formula
            exploration_bonus = math.sqrt(
                2 * math.log(self._total_counts) / count
            )
            ucb_score = avg_reward + exploration_bonus
            
            if ucb_score > best_score:
                best_score = ucb_score
                best_solver = solver
        
        return best_solver
    
    def _thompson_select(self, solver_type: str, available_solvers: list) -> str:
        """Thompson Sampling selection."""
        # TODO: Implement actual Thompson Sampling with Beta distributions
        return solver_type
    
    def update_arm(self, solver: str, reward: float) -> None:
        """
        Update arm statistics after observing reward.
        
        Args:
            solver: Solver that was used
            reward: Observed reward (e.g., negative solve time for minimization)
        """
        if solver not in self._arm_counts:
            self._arm_counts[solver] = 0
            self._arm_rewards[solver] = 0.0
        
        self._arm_counts[solver] += 1
        self._arm_rewards[solver] += reward
        self._total_counts += 1
        
        # Maintain window size
        if self._total_counts > self.window_size:
            self._decay_statistics()
    
    def _decay_statistics(self) -> None:
        """Decay old statistics to maintain window size."""
        # Simple decay: reduce all counts and rewards by 10%
        decay_factor = 0.9
        
        for solver in self._arm_counts:
            self._arm_counts[solver] = int(self._arm_counts[solver] * decay_factor)
            self._arm_rewards[solver] *= decay_factor
        
        self._total_counts = int(self._total_counts * decay_factor)
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get current arbitration statistics."""
        stats = {
            'total_counts': self._total_counts,
            'arms': {}
        }
        
        for solver in self._arm_counts:
            count = self._arm_counts[solver]
            avg_reward = self._arm_rewards[solver] / count if count > 0 else 0.0
            
            stats['arms'][solver] = {
                'count': count,
                'total_reward': self._arm_rewards[solver],
                'avg_reward': avg_reward
            }
        
        return stats
