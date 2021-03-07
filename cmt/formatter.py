from cmt.model import SkillLevel


def to_str(level: SkillLevel) -> str:
    """
    Map model skill level to printable text
    :param level: skill level
    :return: printable text
    """
    if level == SkillLevel.BEGINNER:
        return 'beginner'
    if level == SkillLevel.INTERMEDIATE:
        return 'intermediate'
    if level == SkillLevel.EXPERT:
        return 'expert'
    return ''


def to_skill_level(level: str) -> SkillLevel:
    """
    Map skill level label to skill level model
    :param level: The label for the skill level
    :return: The model representation for given skill level label
    """
    if '3 - Expert' == level:
        return SkillLevel.EXPERT
    if '2 - Intermediate' == level:
        return SkillLevel.INTERMEDIATE
    if '1 - Novice' == level:
        return SkillLevel.BEGINNER
    return SkillLevel.ZERO


def format_org(org_unit: str, team: str) -> str:
    return "{} - {}".format(org_unit, team)
