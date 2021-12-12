
from typing import Counter, List


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
            xPofX.append(value_xPofX)
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
            xRaiseTwoPofX.append(value_xRTPX)
            counter+=1
        
        return xRaiseTwoPofX