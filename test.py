import unittest

from cmt import cmt, config


class TestProcess(unittest.TestCase):
    def test_process_1(self):
        conf = config.get_default_config()
        skills_matrix = cmt.parse('test_process_1.csv', conf)
        self.assertIsNotNone(skills_matrix)
        cmt.print_confluence_wiki_markup(skills_matrix)


if __name__ == '__main__':
    unittest.main()
