import unittest
import os

def analyze_text(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

class TextAnalysisTests(unittest.TestCase):
    '''Tests for the ``analyze_text()`` function'''

    def setUp(self):
       '''fixture that creates a file for the test methods to use'''
       self.filename = 'text_analysis_test_file.txt'
       with open(self.filename, 'w') as f:
           f.write('Now we are engaged in a great civil war.\n'
                   'testing whether that nation,\n'
                   'or any nation so conceived and so dedicated\n'
                   'can long endure')

    def tearDown(self):
        '''fixture that deletes the files used by test methods'''
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        '''basic smoke test: does the function run'''
        analyze_text(self.filename)

    def test_line_count(self):
        '''check that the line count is correct'''
        self.assertEqual(analyze_text(self.filename), 4)

    def test_no_such_file(self):
        '''check the proper exception is thrown for a missing file'''
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        '''check that the function doesn't delete the input file'''
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()