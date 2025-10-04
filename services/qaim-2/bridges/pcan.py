"""
PCAN — Problem Canonicalization Bridge

Transforms domain-specific problems into standardized optimization formats.
Implements S1000D/ATA-aware canonicalization with metadata preservation.

TFA Layer: FWD (Nowcast)
"""

from typing import Dict, Any, Optional


class ProblemCanonicalizer:
    """
    Problem Canonicalization Bridge (PCAN).
    
    Transforms diverse problem representations into a canonical format
    that can be processed by downstream AI bridges and solvers.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize canonicalizer with configuration.
        
        Args:
            config: Configuration with cache_size, s1000d_aware, ata_mapping
        """
        self.config = config
        self.cache_size = config.get('cache_size', 1000)
        self.s1000d_aware = config.get('s1000d_aware', False)
        self.ata_mapping = config.get('ata_mapping', False)
        self._cache = {}
    
    async def canonicalize(
        self,
        problem: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Canonicalize a problem into standard format.
        
        Args:
            problem: Raw problem specification
            metadata: Optional metadata (ATA chapter, domain, S1000D refs)
            
        Returns:
            Canonical problem representation with:
            - problem_type: string identifier
            - variables: list of variable definitions
            - constraints: list of constraint objects
            - objectives: list of objective functions
            - metadata: preserved and enriched metadata
        """
        problem_type = problem.get('problem_type', 'unknown')
        
        # Extract and normalize variables
        variables = self._extract_variables(problem)
        
        # Extract and normalize constraints
        constraints = self._extract_constraints(problem)
        
        # Extract and normalize objectives
        objectives = self._extract_objectives(problem)
        
        # Enrich metadata with ATA/S1000D mappings
        enriched_metadata = self._enrich_metadata(metadata or {})
        
        canonical = {
            'problem_type': problem_type,
            'variables': variables,
            'constraints': constraints,
            'objectives': objectives,
            'metadata': enriched_metadata
        }
        
        return canonical
    
    def _extract_variables(self, problem: Dict[str, Any]) -> list:
        """Extract and normalize variable definitions."""
        variables = problem.get('variables', [])
        
        normalized = []
        for var in variables:
            if isinstance(var, dict):
                normalized.append({
                    'name': var.get('name'),
                    'type': var.get('type', 'continuous'),
                    'lower_bound': var.get('lower_bound', 0),
                    'upper_bound': var.get('upper_bound', float('inf')),
                    'domain': var.get('domain')
                })
            elif isinstance(var, str):
                # Simple variable name
                normalized.append({
                    'name': var,
                    'type': 'continuous',
                    'lower_bound': 0,
                    'upper_bound': float('inf')
                })
        
        return normalized
    
    def _extract_constraints(self, problem: Dict[str, Any]) -> list:
        """Extract and normalize constraint definitions."""
        constraints = problem.get('constraints', [])
        
        normalized = []
        for con in constraints:
            if isinstance(con, dict):
                normalized.append({
                    'type': con.get('type'),
                    'expression': con.get('expression'),
                    'sense': con.get('sense', '<='),
                    'rhs': con.get('rhs', con.get('value', 0)),
                    'metadata': con.get('metadata', {})
                })
        
        return normalized
    
    def _extract_objectives(self, problem: Dict[str, Any]) -> list:
        """Extract and normalize objective functions."""
        objectives = problem.get('objectives', [])
        
        normalized = []
        for obj in objectives:
            if isinstance(obj, dict):
                normalized.append({
                    'name': obj.get('name'),
                    'expression': obj.get('expression'),
                    'sense': obj.get('sense', 'minimize'),
                    'weight': obj.get('weight', 1.0)
                })
        
        return normalized
    
    def _enrich_metadata(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Enrich metadata with ATA/S1000D mappings."""
        enriched = metadata.copy()
        
        # Add ATA chapter mapping if enabled
        if self.ata_mapping:
            ata_chapter = metadata.get('ata_chapter')
            if ata_chapter:
                enriched['ata_info'] = self._get_ata_info(ata_chapter)
        
        # Add S1000D references if enabled
        if self.s1000d_aware:
            s1000d_refs = metadata.get('s1000d_refs', [])
            if s1000d_refs:
                enriched['s1000d_info'] = self._get_s1000d_info(s1000d_refs)
        
        return enriched
    
    def _get_ata_info(self, ata_chapter: str) -> Dict[str, Any]:
        """Get ATA chapter information."""
        # Basic ATA chapter mapping
        ata_mapping = {
            'ATA-21': {'name': 'Air Conditioning', 'domain': 'ECS'},
            'ATA-22': {'name': 'Auto Flight', 'domain': 'LCC'},
            'ATA-23': {'name': 'Communications', 'domain': 'IIS'},
            'ATA-24': {'name': 'Electrical Power', 'domain': 'EDI'},
            'ATA-34': {'name': 'Navigation', 'domain': 'IIS'},
            'ATA-42': {'name': 'Integrated Modular Avionics', 'domain': 'IIS'},
            'ATA-57': {'name': 'Wings', 'domain': 'AAA'},
            'ATA-71': {'name': 'Powerplant', 'domain': 'PPP'},
        }
        
        return ata_mapping.get(ata_chapter, {'name': 'Unknown', 'domain': 'Unknown'})
    
    def _get_s1000d_info(self, s1000d_refs: list) -> Dict[str, Any]:
        """Get S1000D reference information."""
        return {
            'references': s1000d_refs,
            'count': len(s1000d_refs),
            'types': list(set(ref.split('-')[0] for ref in s1000d_refs if '-' in ref))
        }
