from dataclasses import dataclass
from logic.skills import ConcreteSkill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: ConcreteSkill