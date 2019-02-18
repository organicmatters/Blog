# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'webapp/home.html')

def linear_regression(request):
    return render(request, 'webapp/linear_regression.html')

def TransferLearning(request):
    return render(request, 'webapp/TransferLearning.html')

def JupyterSetup(request):
    return render(request, 'webapp/JupyterSetup.html')

def GettingAWSserverrunning(request):
    return render(request, 'webapp/GettingAWSserverrunning.html')

def Finetuning(request):
    return render(request, 'webapp/Finetuning.html')

def Overfitting(request):
    return render(request, 'webapp/reducingoverfitting.html')

def About(request):
    return render(request, 'webapp/About.html')

def DataScienceWorkFlow(request):
    return render(request, 'webapp/DataScienceWorkFlow.html')

def LoadingJungleScoutData(request):
    return render(request, 'webapp/LoadingJungleScoutData.html')

def CleaningJungleScoutData(request):
    return render(request, 'webapp/CleaningJungleScoutData.html')

def SubwayAnalysis(request):
    return render(request, 'webapp/SubwayAnalysis.html')

def EdgarCrawl(request):
    return render(request, 'webapp/EdgarCrawlBlog.html')

def CleaningChicagoCrime(request):
    return render(request, 'webapp/cleaningchicagocrime.html')

def ModelingChicagoCrime(request):
    return render(request, 'webapp/modelingchicagocrime.html')
