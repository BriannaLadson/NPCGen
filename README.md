# NPCGen
NPCGen is a lightweight Python library for generating deterministic, customizable NPC data—including races, compatibility groups, and mixed ancestry—for games and simulations.

***
## How to Generate NPCs

### 1. Import core classes
```
from npcgen.models import Race, RaceRegistry
from npcgen.core import NPCGenerator
```

### 2. Create a RaceRegistry
The registry holds all races and defines genetic compatibility via groups.

```
races = RaceRegistry()
```

### 3. Define Compatibility Groups
Races in the same group are genetically compatible (can produce mixed ancestry).

```
races.add_group("Humanoid")
races.add_group("Felinenoid")
```

### 4. Register Races
Each race is assigned to a compatibility group.

```
races.add_race(Race("Human", "Humanoid"))
races.add_race(Race("Elf", "Humanoid"))

races.add_race(Race("Tigerfolk", "Felinenoid"))
races.add_race(Race("Lionfolk", "Felinenoid"))
```

### 5. Initialize the NPC Generator
Pass the race registry into NPCGenerator. Optionally, you can pass in a integer seed for deterministic output.

```
gen = NPCGenerator(races)
```

### 6. Generate NPCs
Generate any number of NPCs at one.

Each NPC is returned as a dictionary containing:
* A unique id
* An ancestry dict (e.f. {"Human": 1.0} or {"Human": 0.5, "Elf": 0.5})

```
npcs = gen.generate(10)
```

### 7. Use the Generated Data
NPCGen only produces data - how you use it is up to your simulation or game.

```
for npc in npcs:
  print(npc)
```

Example Output
```
{'id': 1, 'ancestry': {'Human': 1.0}}
{'id': 2, 'ancestry': {'Elf': 0.5, 'Human': 0.5}}
```
