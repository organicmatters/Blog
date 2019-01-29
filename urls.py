from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^linear_regression/', views.linear_regression, name='linear_regression'),
    url(r'^TransferLearning/', views.TransferLearning, name='TransferLearning'),
    url(r'^JupyterSetup/', views.JupyterSetup, name='JupyterSetup'),
    url(r'^GettingAWSserverrunning/', views.GettingAWSserverrunning, name='GettingAWSserverrunning'),
    url(r'^Finetuning/', views.Finetuning, name='Finetuning'),
    url(r'^Overfitting/', views.Overfitting, name='Overfitting'),
    url(r'^About/', views.About, name='About'),
    url(r'^DataScienceWorkFlow/', views.DataScienceWorkFlow, name='DataScienceWorkFlow'),
    url(r'^LoadingJungleScoutData/', views.LoadingJungleScoutData, name='LoadingJungleScoutData'),
    url(r'^CleaningJungleScoutData/', views.CleaningJungleScoutData, name='CleaningJungleScoutData'),
    url(r'^SubwayAnalysis/', views.SubwayAnalysis, name='SubwayAnalysis'),
    url(r'^EdgarCrawl/', views.EdgarCrawl, name='EdgarCrawl')
]
