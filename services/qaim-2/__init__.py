"""
QAIM-2 Service Package

Quantum-Classical Optimization via AI Bridges
"""

__version__ = '0.1.0'
__author__ = 'Amedeo Pelliccia'
__bridge__ = 'QS→FWD→UE→FE→CB→QB'

from .core.qaim_orchestrator import QAIM2Orchestrator

__all__ = ['QAIM2Orchestrator']
