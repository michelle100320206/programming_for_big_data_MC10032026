
import unittest

from mc_code_dict import read_file, get_commits, get_authors


class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data)) #testing lines 

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        
    def test_number_of_authors(self): 
        commits = get_commits(self.data)
        self.assertEqual (10, len(authors))
        self.assertEqual(191, len(authors ['Thomas']))

if __name__ == '__main__':
    unittest.main()
