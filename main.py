import argparse

from cmt import cmt, config

parser = argparse.ArgumentParser(description='Capability Matrix Tool')
parser.add_argument('file_name', help='The Capability Matrix raw data file name to process')
args = parser.parse_args()

skills_matrix = cmt.parse(args.file_name, config.get_default_config())
cmt.print_confluence_wiki_markup(skills_matrix)
