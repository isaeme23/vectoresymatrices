import unittest
import vectors as vec
import numpy as np

class TestVectors(unittest.TestCase):

    def test_AddVectors(self):
        c1, c2 = [1,2,3], [4,5,6]
        self.assertEqual(vec.AddVectors(c1, c2), [5, 7, 9])

    def test_inverso(self):
        c1 = [1+5j,2+3j,3+1j]
        self.assertEqual(vec.inverso(c1), [(-1-5j), (-2-3j), (-3-1j)])

    def test_Escalarporvector(self):
        c1 , c2 = [1+5j,2+3j,3+1j], 3
        self.assertEqual(vec.EscalarporVectorC(c2,c1), [(3+15j), (6+9j), (9+3j)])

    def test_Addmatrix(self):
        c1, c2 = np.array([[1+5j,2+3j],[3+1j,8]]), np.array([[4+2j,5+1j],[6,3+5j]])
        self.assertEqual(vec.AddMatrix(c1, c2),[[(5+7j), (7+4j)], [(9+1j), (11+5j)]])

    def test_InvMatrix(self):
        c1, = np.array([[1+5j,2+3j],[3+1j,8]])
        self.assertEqual(vec.InvMatrix(c1),[[(-1-5j), (-2-3j)], [(-3-1j), (-8-0j)]])

    def test_EscalarporMatrix(self):
        c1, c2 = np.array([[1+5j,2+3j],[3+1j,8]]), 3
        self.assertEqual(vec.EscalarPorMatrixC(c2,c1), [[(3+15j), (6+9j)], [(9+3j), (24+0j)]])

    def test_Transpuesta(self):
        c1 = np.array([[1+5j,2+3j],[3+1j,8]])
        self.assertEqual(vec.Transpuesta(c1), [[(1+5j), (3+1j)], [(2+3j), (8+0j)]])

    def test_Adjunta(self):
        c1 = np.array([[1+5j,2+3j],[3+1j,8]])
        self.assertEqual(vec.Adjunta(c1), [[(-1-5j), (-3-1j)], [(-2-3j), (-8-0j)]])

    def test_Multiplicar(self):
        c1, c2 = np.array([[1+5j,2+3j],[3+1j,8]]), np.array([[4+2j,5+1j],[6,3+5j]])
        self.assertEqual(vec.multiplicar(c1,c2), [[(6+40j), (-9+45j)], [(58+10j), (38+48j)]])

    def test_productoInterno(self):
        c1, c2 = [1+5j,2+3j,3+1j,8], [4+2j,5+1j,6,3+5j]
        self.assertEqual(vec.producto_interno(c1,c2), (43+85j))

    def test_norma(self):
        c1 = [1+5j,2+3j,3+1j,8]
        self.assertEqual(vec.norma(c1), (21.5+14j))

    def test_distancia(self):
        c1, c2 = [1+5j,2+3j,3+1j,8], [4+2j,5+1j,6,3+5j]
        self.assertEqual(vec.distancia(c1,c2), (6.5-43j))

    def test_productotensor(self):
        c1, c2 = np.array([[1,3],[3,8]]), np.array([[4,5],[6,5]])
        self.assertEqual(vec.producto_tensor(c1,c2), [[ 4  5 12 15]
                                                        [ 6  5 18 15]
                                                        [12 15 32 40]
                                                        [18 15 48 40]])

if __name__ == '__main__':
    unittest.main()