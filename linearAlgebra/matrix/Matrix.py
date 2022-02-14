from collections.abc import Iterable
from typing import List, Tuple

import numpy as np

from mMath.linearAlgebra import matrix
from mMath.linearAlgebra.Vector import Vector


class Matrix():
    '''
    @use matrixes only for cases in which operations such as + * etc are meaningful. Dont use it to represent data
    @todo: Each matrix is composed of columns of vectors. As such replace the inheritence between matrix and vector with composition

    '''

    def __init__(self, rows: Iterable):
        ''''''
        self._setNpRows(rows)

    def _setNpRows(self,rows: Iterable):
        '''A matrix is formed of many rows'''
        self._npRows: np.ndarray = None
        if type(rows) is list:
            if isinstance(rows[0],Vector.Vector):
                vecRows = []
                for vecRow in rows:
                    vecRows.append(vecRow.getNpRow())
                self._npRows = np.asarray(vecRows)
            else:
                self._npRows = np.asarray(rows)
        elif type(rows) is dict:
            self._npRows = rows
        elif type(rows) is np.ndarray:
            self._npRows = rows


    def updateRows(self,rows: Iterable):
        ''''''
        self._setNpRows(rows)


    def __mul__(self, other) -> matrix:
        ''''''
        npResult = None
        if type(other) in (float, np.float64, int):
            npResult = other * self._npRows
        elif type(other) in (Matrix):
            npResult = np.dot(self._npRows, other)
        else:
            raise Exception("matrix multiply dosent understand how to treat 'Other' data type")
        npResult = Matrix(npResult)
        return npResult

    def __add__(self, other: matrix) -> matrix:
        ''''''
        npAdd = np.add(self.getNpRows(), other.getNpRows())
        addMat = Matrix(npAdd)
        return addMat

    def __getInverse(self) -> matrix:
        pass

    def __pow__(self, power, modulo=None) -> matrix:
        if power == -1:
            return self.getInverse()
        elif power == 'T':
            return self.transpose(self)
        elif isinstance(power , int):
            if power>0:
                pass

    def __sub__(self, other: matrix) -> matrix:
        '''over writes subtract'''
        npSub = np.subtract(self.getNpRows(), other.getNpRows())
        subMat = Matrix(npSub)
        return subMat

    def __getitem__(self, index: int):
        '''for brackets []'''
        return self._npRows[index]

    def getNpRowByIndex(self, index: int):
        return self._npRows[index]

    def getNpColByIndex(self, colIndex: int) -> np.ndarray:
        return self._npRows[:, colIndex]

    def transpose(m: matrix) -> matrix:
        '''Transpose'''
        pass

    def getIdentity(dimention: int) -> matrix:
        pass

    def getNpRows(self) -> np.ndarray:
        return self._npRows

    def getRowsNum(self) -> int:
        return self._npRows.shape[0]

    def getColsNum(self) -> int:
        return self._npRows.shape[1]

    def getDimensions(self)->Tuple[int]:
        return self.getNpRows().shape
