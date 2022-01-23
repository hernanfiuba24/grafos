import unittest

class Matrix:

    def __init__(self,rows,columns):
        self.matrix=[]
        self.rows=rows
        self.columns=columns
        for i in range(rows):
            row=[]
            for j in range(columns):
                row.append(None)
            self.matrix.append(row)
    
    def getRows(self):
        return self.rows

    def getColumns(self):
        return self.columns
    
    def setValue(self,row,column,value):
        self.matrix[row][column]=value

    def getValue(self,row,column):
        return self.matrix[row][column]

class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matrix = Matrix(2,4)

    def test_initiliaze(self):
        self.assertEqual(self.matrix.getRows(), 2)
        self.assertEqual(self.matrix.getColumns(), 4)

    def test_set_value(self):
        self.matrix.setValue(1,1,100)
        self.assertEqual(self.matrix.getValue(1,1), 100)
        
if __name__ == "__main__":
    unittest.main()
        

