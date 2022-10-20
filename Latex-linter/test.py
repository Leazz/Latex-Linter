import unittest
import functions



class test(unittest.TestCase):
    

    def test_addLines(self):
        """
        Testing the add new lines after dots function.
        """
        myFile = "test.tex"
        functions.addLinesAfterDots(myFile) 
        with open("copyOfTheFile.tex", "r") as f:
            contents = f.read()
        with open("expected.tex", "r") as e:
        
                expected = e.read() 
        self.assertEqual(contents, expected)


    def test_addLines_error(self):
        """
        Testing if the add new line after dots function is wrong.
        """
        myFile = "test.tex"
        functions.addLinesAfterDots(myFile) 
        with open("copyOfTheFile.tex", "r") as f:
            contents = f.read()
        expected = ""
        self.assertNotEqual(contents, expected)
            

    def test_addSpace(self):
        """
        Testing the add space function.
        """
        myFile = "test.tex"
        functions.addSpace(myFile)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        with open("expected2.tex", "r") as e:

                expected = e.read()
        self.assertEqual(contents, expected)

      
    def test_addSpace_error(self):
        """
        Testing if the add space function is wrong.
        """
        myFile = "test.tex"
        functions.addSpace(myFile)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        expected = ""
        self.assertNotEqual(contents, expected)
        

    def test_blocks(self):
        """
        Testing the blocks function.
        """
        myFile = "test.tex"
        functions.blocks(myFile)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        with open("expected3.tex", "r") as e:

                expected = e.read() 
        self.assertEqual(contents, expected)


    def test_blocks_error(self):
        """
        Testing if the blocks function is wrong.
        """
        myFile = "test.tex"
        functions.blocks(myFile)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        expected = "" 
        self.assertNotEqual(contents, expected)



    def test_blankLines(self):
        """
        Testing the blank lines function.
        """
        myFile = "test.tex"
        functions.blankLine(myFile, 3)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        with open("expected4.tex", "r") as e:
                expected = e.read() 
        self.assertEqual(contents, expected)


    def test_blankLines_error(self):
        """
        Testing if the blank lines function is wrong.
        """
        myFile = "test.tex"
        functions.blankLine(myFile, 3)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        expected = ""
        self.assertNotEqual(contents, expected)


    def test_chekTheFile(self):
        """
        Testing the check type of file function is a tex file.
        """
        myFile = "test.tex"
        self.assertTrue(functions.checkFileType(myFile), True)

    def test_chekTheFile2(self):
        """
        Testing the check type of file function is a tikz file.
        """
        myFile = "test.tikz"
        self.assertTrue(functions.checkFileType(myFile), True)

    def test_chekTheFile3(self):
        """
        Testing the check type of file function is a bib file.
        """
        myFile = "test.bib"
        self.assertTrue(functions.checkFileType(myFile), True)

    def test_chekTheFile_error(self):
        """
        Testing if the check type of file function is wrong.
        """
        myFile = "test.text"
        self.assertFalse(functions.checkFileType(myFile), False)

    def test_chekTheFile_error2(self):
        """
        Testing if the check type of file function is empty.
        """
        myFile = ""
        self.assertFalse(functions.checkFileType(myFile), False)



if __name__ == '__main__':
    unittest.main()
    