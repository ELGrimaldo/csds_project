
from typing import List
import math


class DataProbability:
    def __init__(self, valueOfX: List[int], pOfX: List[float] ) -> None:
        self.valueOfX = valueOfX
        self.pOfX = pOfX
    
    def get_XValue(self) -> List[int]:
        return self.valueOfX

    def get_POfX(self) -> List[float]:
        return self.pOfX

    def get_xPofX(self) -> List[float]:
        valOfX = self.valueOfX
        pOfX   = self.pOfX

        xPofX = []

        counter = 0
        while counter != len(valOfX):
            value_xPofX = valOfX[counter] * pOfX[counter]
            xPofX.append(round(value_xPofX,2))
            counter+=1
        
        return xPofX

    def get_xRaiseTwo(self) -> List[int]:
        value_X = self.get_XValue()

        xRaiseTwo = []
        for value in value_X:
            value_xRaiseTwo = value ** 2
            xRaiseTwo.append(value_xRaiseTwo)
        
        return xRaiseTwo

    def get_xRaiseTwoPofX(self) -> List[float]:
        xRaiseTwo = self.get_xRaiseTwo()
        pOfX = self.get_POfX()

        xRaiseTwoPofX = []

        counter = 0
        while counter != len(xRaiseTwo):
            value_xRTPX = xRaiseTwo[counter] * pOfX[counter]
            xRaiseTwoPofX.append(round(value_xRTPX, 2))
            counter+=1
        
        return xRaiseTwoPofX



class Probability:
    def getMean(px: List[int]):
        result = sum(px)
        return result
    
    def getVariance(xpxTwo: List[int], xpx: List[int]):
        result = (sum(xpxTwo) - sum(xpx)** 2  ) 
        return result

    def getStandardDeviation(xpxTwo: List[int], xpx: List[int]):
        varTwo = (sum(xpxTwo) - sum(xpx)** 2) 
        result = math.sqrt(varTwo)
        return result