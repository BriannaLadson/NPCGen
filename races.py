import random
from typing import Dict, List, Optional
from .models import RaceRegistry

def normalize_weights(items: List[str], weights:Optional[List[float]] = None):
	if not items:
		raise ValueError("No items to choose from.")
		
	if weights is None:
		return items, [1.0] * len(items)
		
	if len(weights) != len(items):
		raise ValueError("Weights must match items length.")
		
	return items, weights
	
def weighted_choice(rng: random.Random, items: List[str], weights: Optional[List[float]] = None) -> str:
	items, weights = normalize_weights(items, weights)
	return rng.choices(items, weights=weights, k=1)[0]
	
def generate_ancestry(
	rng: random.Random,
	race_registry: RaceRegistry,
	*,
	allow_mixed: bool = True,
	mixed_chance: float = 0.20
	) -> Dict[str, float]:
	
	all_races = list(race_registry.races.keys())
	
	if not all_races:
		raise ValueError("RaceRegistry has no races registered.")
		
	# Pick base race
	r1 = weighted_choice(rng, all_races)
	
	# Pure ancestry
	if (not allow_mixed) or (rng.random() > mixed_chance):
		return {r1: 1.0}
		
	# Mixed ancestry: pick another race from same group (if possible)
	group = race_registry.get_race(r1).group
	candidates = [r for r in race_registry.races_in_group(group) if r != r1]
	
	# If not compatible second race exists, fallback to pure
	if not candidates:
		return {r1: 1.0}
		
	r2 = weighted_choice(rng, candidates)
	
	return {r1: 0.5, r2: 0.5}