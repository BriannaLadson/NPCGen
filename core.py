import random
from typing import Dict, List
from .models import RaceRegistry
from .races import generate_ancestry

class NPCGenerator:
	def __init__(
		self,
		race_registry: RaceRegistry,
		*,
		seed: int = None,
		allow_mixed_ancestry: bool = True,
		mixed_ancestry_chance: float = 0.20
	):
	
		self.race_registry = race_registry
		self.rng = random.Random(seed)
		self.allow_mixed_ancestry = bool(allow_mixed_ancestry)
		self.mixed_ancestry_chance = float(mixed_ancestry_chance)
		
		self.next_id = 1
		
	def generate_one(self) -> Dict:
		npc_id = self.next_id
		
		self.next_id += 1
		
		ancestry = generate_ancestry(
			self.rng,
			self.race_registry,
			allow_mixed = self.allow_mixed_ancestry,
			mixed_chance = self.mixed_ancestry_chance,
		)
		
		return {
			"id": npc_id,
			"ancestry": ancestry,
		}
		
	def generate(self, n):
		return [self.generate_one() for _ in range(n)]