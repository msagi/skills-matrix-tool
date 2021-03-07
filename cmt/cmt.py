import csv
import logging
import operator
from typing import Dict, List

from cmt.model import Colleague, ColleagueSkill, SkillLevel
from .config import Config, get_default_config
from .formatter import to_str, to_skill_level, format_org


def parse(file_name: str, config: Config = get_default_config()) -> Dict[str, List[Colleague]]:
    logging.debug("Processing {}...".format(file_name))
    rows = []
    with open(file_name, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=config.delimiter, quotechar=config.quote_character)
        # cache all rows from CSV
        for colleague_record in csv_reader:
            rows.append(colleague_record)
    # skip X number of rows at beginning
    for line in range(0, config.skip_lines_at_beginning):
        rows.pop(0)
    # skip X number of rows at end
    for line in range(0, config.skip_lines_at_end):
        rows.pop()
    # mark the header row
    header_row = rows.pop(0)
    skills_matrix = {}
    for row_index in range(0, len(rows)):
        colleague_record = rows[row_index]
        # create new colleague record
        colleague = Colleague(name=colleague_record[0],
                              id=colleague_record[1],
                              org_unit=colleague_record[2],
                              role=colleague_record[3],
                              team=colleague_record[4],
                              skills=[])
        # add colleague skills
        for column in config.group_by_column:
            skill_name = header_row[column]
            # check and add skill domain to the matrix
            if skill_name not in skills_matrix:
                skills_matrix[skill_name] = []
            skill_level = to_skill_level(colleague_record[column])
            if skill_level == SkillLevel.INTERMEDIATE or skill_level == SkillLevel.EXPERT:
                # create skill record
                skill = ColleagueSkill(domain='',
                                       name=skill_name,
                                       level=skill_level)
                # link skill to colleague
                colleague.skills.append(skill)
                # link colleague to skills matrix
                skills_matrix[skill_name].append(colleague)
    # sort colleagues in skill groups by their name
    for skill_name in skills_matrix:
        skills_matrix[skill_name].sort(key=operator.attrgetter('name'))
    logging.debug('Loading complete.')
    return skills_matrix


def print_confluence_wiki_markup(skills_matrix: Dict[str, List[Colleague]]):
    for skill_name in skills_matrix:
        skill_group = skills_matrix[skill_name]
        markup = ["h1. {}".format(skill_name)]

        if skill_group:
            markup.append("\n||Name||ID||Level||Role||Value Stream||")
            for colleague in skill_group:
                skill_level = to_str(colleague.get_skill_level('', skill_name))
                org_unit = format_org(colleague.org_unit, colleague.team)
                markup.append("\n|{}|[~{}]|{}|{}|{}|"
                              .format(colleague.name, colleague.id, colleague.role, org_unit, skill_level))
        else:
            markup.append('\n*Skill gap!*')
        markup.append('\n')
        print(''.join(markup))
