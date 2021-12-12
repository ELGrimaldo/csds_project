
from typing import List


class Stats:
    def __init__(self, xValue: List[int]) -> None:
        self.xValue = xValue
    
    def probDistribution(self):
        probDistribution = []
        for value in self.probability: 
            probDistribution.append(value/10)

        return probDistribution

    def meanValues(self):
        mean = []
        probDistribution = self.probDistribution()
        probability = self.probability
        for i in range(0,4):
            mean.append(probability[i] *probDistribution[i])
        
        return mean

    def mean(self):
        return sum(self.meanValues()) 
    
    def xSquared(self):
        xSquared = []
        for value in self.probability:
            xSquared.append(value ** 2)

        return xSquared
        
    def variationValues(self):
        variationValues = []
        probDistribution = self.probDistribution()
        xSquared = self.xSquared()
        for i in range(0, 4):
            variationValues.append(probDistribution[i] * xSquared[i])

        return variationValues

    def variation(self):
        return sum(self.variationValues())

    def variance(self):
        return self.variation() - (self.mean() ** 2)


# a = Stats()

# print(a.probDistribution())
# for i in a.meanValues():
#     print("{:.2f}".format(i))

# print(a.mean())
# print("----------")
# print(a.xSquared())
# print("----------")
# print(a.variationValues())
# print("----------")
# print(a.variation())
# print("----------")
# print(a.variance())