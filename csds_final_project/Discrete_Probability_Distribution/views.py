from typing import List
from django import http
from django.shortcuts import render
from .models import TableValues
from .forms import InputX
from .proba import DataProbability, Probability

# Create your views here.
def index(request, *args, **kwargs):
    
    valueOfX = 'xValue' in request.POST and request.POST['xValue']
    valueOfpX = 'pXValue' in request.POST and request.POST['pXValue']
    try:
        if ((valueOfX is not False) and (valueOfpX is not False)) or ((valueOfX == '') and (valueOfpX == '')):
            print('a:', valueOfX)
            print('a:', valueOfpX)
            xValue = str(valueOfX)
            pXValue = str(valueOfpX)

            xValue = xValue.split(",")
            pXValue = pXValue.split(",")

            xValue = [int(value) for value in xValue]
            pXValue = [float(value) for value in pXValue]

            warns = ''
            if (len(xValue) != len(pXValue)):
                print("heys")
                warns = 'Please make sure that count of X values is equal to count of P(x) values'
            


            print(xValue)
            print(pXValue)
            print(len(xValue))
            print(len(pXValue))

            tableData = DataProbability(xValue, pXValue)

            xValue_data = tableData.get_XValue()
            pOfX_data = tableData.get_POfX()
            xPofX_data = tableData.get_xPofX()
            xRaiseTwo_data = tableData.get_xRaiseTwo()
            xRaiseTwoPofX_data = tableData.get_xRaiseTwoPofX()

            tableRow = []

            for i in range(0, len(xValue_data)):
                tableCol = [xValue_data[i], pOfX_data[i], xPofX_data[i], xRaiseTwo_data[i], xRaiseTwoPofX_data[i]]
                tableRow.append(tableCol)

            mean = Probability.getMean(xPofX_data)
            variance = Probability.getVariance(xRaiseTwoPofX_data, xPofX_data)
            standardDeviation = Probability.getStandardDeviation(xRaiseTwoPofX_data, xPofX_data)

            def getSum(values: List[int]) -> float:
                sumOfValues = sum(values)
                return round(sumOfValues, 2)
            context = {
                'tableRow': tableRow,
                'tableSums': [getSum(pOfX_data), getSum(xPofX_data), getSum(xRaiseTwoPofX_data)],
                'mean': mean,
                'variance': variance,
                'standardDeviation': standardDeviation,
                'warn': '',
                'warnTwo': warns,
                'marginx': (100/ len(xValue_data))-5,
                'plotval': [round(value*100) for value in pOfX_data],
                'marginy': [round((100-(value*100))/2.5) for value in pOfX_data],
                'x': [round(value) for value in xValue_data],
            }
            
            print("sukat: ", len(xValue))
            print("sukat: ", len(pXValue))
            if getSum(pOfX_data) != 1:
                context['warn'] = '''Summation of P(x) is not equal to 1'''
            
            
                
            
                
            

            
            return render(request, 'Discrete_Probability_Distribution\index.html', context)
        else:
            context = {
                'tableRow': [[0,0,0,0,0]]
            }
            return render(request, 'Discrete_Probability_Distribution\index.html', context)
    except: 
        context = {
            'tableRow': [[0,0,0,0,0]]
        }
        return render(request, 'Discrete_Probability_Distribution\index.html', context)
    