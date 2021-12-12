from django import http
from django.shortcuts import render
from .models import TableValues
from .forms import InputX
from .proba import DataProbability

# Create your views here.
def index(request, *args, **kwargs):
    # valueOfX = 'xValue' in request.POST and request.POST['xValue']
    # print(valueOfX)
    # xValue = str(valueOfX)
    # xValue = int(xValue.split(","))
    
    tableData = DataProbability([1, 2, 3, 4], [0.95, 0.2, 0.2, 0.1])
    
    xValue_data = tableData.get_XValue()
    pOfX_data = tableData.get_POfX()
    xPofX_data = tableData.get_xPofX()
    xRaiseTwo_data = tableData.get_xRaiseTwo()
    xRaiseTwoPofX_data = tableData.get_xRaiseTwoPofX()

    context = {
            
        'x': xValue_data,
        'px': pOfX_data,
        'xpx': xPofX_data,
        'x2': xRaiseTwo_data,
        'x2px': xRaiseTwoPofX_data,
    }
    return render(request, 'Discrete_Probability_Distribution\index.html', context)