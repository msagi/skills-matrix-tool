from dataclasses import dataclass
from enum import Enum


class SkillLevel(Enum):
    ZERO = 0
    BEGINNER = 1
    INTERMEDIATE = 2
    EXPERT = 3


@dataclass
class ColleagueSkill:
    # the domain of the skill
    domain: str
    # the skill name
    name: str
    # the knowledge or experience level for the skill
    level: SkillLevel


@dataclass
class Colleague:
    # the name of the colleague
    name: str
    # the ID of the colleague
    id: str
    # the org unit of the colleague
    org_unit: str
    # the role title of the colleague
    role: str
    # the scrum team of the colleague
    team: str
    # the colleague skills
    skills: [ColleagueSkill]

    def get_skill_level(self, domain, name) -> SkillLevel:
        for skill in self.skills:
            if skill.domain == domain and skill.name == name:
                return skill.level
        return SkillLevel.ZERO
