import unittest
import functions



class test(unittest.TestCase):
    

    def test_addLines(self):
            myFile = "test.tex"
            functions.addLinesAfterDots(myFile) 
            with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
            with open("expected.tex", "r") as e:
            
                expected = e.read() 
            self.assertEqual(contents, expected)


    def test_addLines_error(self):
            myFile = "test.tex"
            functions.addLinesAfterDots(myFile) 
            with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
            expected = ""
            self.assertNotEqual(contents, expected)
            

    def test_addSpace(self):
        myFile = "test.tex"
        functions.addSpace(myFile)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        with open("expected2.tex", "r") as e:

                expected = e.read()
        self.assertEqual(contents, expected)

      
    def test_addSpace_error(self):
        myFile = "test.tex"
        functions.addSpace(myFile)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        expected = ""
        self.assertNotEqual(contents, expected)
        

    def test_blocks(self):
        myFile = "test.tex"
        functions.blocks(myFile)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        with open("expected3.tex", "r") as e:

                expected = e.read() 
        self.assertEqual(contents, expected)


    def test_blocks_error(self):
        myFile = "test.tex"
        functions.blocks(myFile)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        expected = "" 
        self.assertNotEqual(contents, expected)



    def test_blankLines(self):
        myFile = "test.tex"
        functions.blankLine(myFile, 3)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        with open("expected4.tex", "r") as e:
                expected = e.read() 
        self.assertEqual(contents, expected)


    def test_blankLines_error(self):
        myFile = "test.tex"
        functions.blankLine(myFile, 3)
        with open("copyOfTheFile.tex", "r") as f:
                contents = f.read()
        expected = ""
        self.assertNotEqual(contents, expected)


    def test_chekTheFile(self):
        myFile = "test.tex"
        self.assertTrue(functions.checkFileType(myFile), True)

    def test_chekTheFile2(self):
        myFile = "test.tikz"
        self.assertTrue(functions.checkFileType(myFile), True)

    def test_chekTheFile3(self):
        myFile = "test.bib"
        self.assertTrue(functions.checkFileType(myFile), True)

    def test_chekTheFile_error(self):
        myFile = "test.text"
        self.assertFalse(functions.checkFileType(myFile), False)

    def test_chekTheFile_error2(self):
        myFile = ""
        self.assertFalse(functions.checkFileType(myFile), False)



if __name__ == '__main__':
    unittest.main()
    