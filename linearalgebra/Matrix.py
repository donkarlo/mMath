from collections.abc import Iterable
from typing import List

import numpy as np

from linearalgebra import Matrix
from linearalgebra.Vector import Vector


class Matrix():
    '''todo: Each matrix is composed of columns of vectors. As such replace the inheritence between matrix and vector with composition'''

    def __init__(self, rows: Iterable):
        ''''''
        self._setNpRows(rows)

    def _setNpRows(self,rows: Iterable):
        '''A matrix is formed of many rows'''
        self.__npRows: np.ndarray = None
        if type(rows) is list:
            if isinstance(rows[0],Vector.Vector):
                vecRows = []
                for vecRow in rows:
                    vecRows.append(vecRow.getNpRow())
                self.__npRows = np.asarray(vecRows)
            else:
                self.__npRows = np.asarray(rows)
        elif type(rows) is np.ndarray:
            self.__npRows = rows


    def updateRows(self,rows: Iterable):
        self._setNpRows(rows)


    def __mul__(self, other) -> Matrix:
        ''''''
        npResult = None
        if type(other) in (float, np.float64, int):
            npResult = other * self.__npRows
        elif type(other) in (Matrix):
            npResult = np.dot(self.__npRows, other)
        else:
            raise Exception("Matrix multiply dosent understand how to treat 'Other' data type")
        npResult = Matrix(npResult)
        return npResult

    def __add__(self, other: Matrix) -> Matrix:
        ''''''
        npAdd = np.add(self.getNpRows(), other.getNpRows())
        addMat = Matrix(npAdd)
        return addMat

    def __getInverse(self) -> Matrix:
        pass

    def __pow__(self, power, modulo=None) -> Matrix:
        if power == -1:
            return self.getInverse()
        elif power == 'T':
            return self.transpose(self)
        elif isinstance(power , int):
            if power>0:
                pass

    def __sub__(self, other: Matrix) -> Matrix:
        '''over writes subtract'''
        npSub = np.subtract(self.getNpRows(), other.getNpRows())
        subMat = Matrix(npSub)
        return subMat

    def __getitem__(self, index: int):
        '''for brackets []'''
        return self.__npRows[index]

    def getNpRowByIndex(self, index: int):
        return self.__npRows[index]

    def getNpColByIndex(self, colIndex: int) -> np.ndarray:
        return self.__npRows[:, colIndex]

    def transpose(m: Matrix) -> Matrix:
        '''Transpose'''
        pass

    def getIdentity(dimention: int) -> Matrix:
        pass

    def getNpRows(self) -> np.ndarray:
        return self.__npRows

    def getRowsNum(self) -> int:
        return self.__npRows.shape[0]

    def getColsNum(self) -> int:
        return self.__npRows.shape[1]
