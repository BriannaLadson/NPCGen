from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Set

@dataclass(frozen=True)
class SpeciesGroup:
	"""
	A SpeciesGroup defines genetic compatibility.
	Example: Humanoid, Felinenoid, Draconic, etc.
	"""
	name: str
	description: str = ""
	
@dataclass(frozen=True)
class Race:
	"""
	A Race is a concrete species like Human, Elf, Tigerfolk.
	 
	Races are compatible for reproduction if they share the same species group (unless overridden later).
	"""
	name: str
	group: str
	

class RaceRegistry:
	"""
	Stores all races and species groups.
	Handles genetic compatibility rules.	
	"""
	def __init__(self):
		self.groups: Dict[str, SpeciesGroup] = {}
		self.races: Dict[str, Race] = {}
		
	def add_group(self, name: str, description: str = ""):
		self.groups[name] = SpeciesGroup(name, description)
		
	def add_race(self, race: Race):
		if race.group not in self.groups:
			raise ValueError(f"Race group '{race.group}' is not registered.")
			
		self.races[race.name] = race
		
	def get_race(self, name: str) -> Race:
		return self.races[name]
			
	def get_group(self, name: str) -> SpeciesGroup:
		return self.groups[name]
		
	def compatible(self, race_a: str, race_b: str) -> bool:
		"""
		Returns True if two races can reproduce.
		Default rule: same species group.
		"""
		return self.races[race_a].group == self.races[race_b].group
		
	def races_in_group(self, group_name: str) -> Set[str]:
		return {
			race.name for race in self.races.values() if race.group == group_name
		}