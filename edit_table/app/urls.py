from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),

	#API data
	path('testsapi/', views.testsDataAPI),

	#Create test
	path('createtest/', views.createTest),

	#Create test
	path('updatetest/', views.updateTest),
	
	path('deletetest/', views.deleteTest),
]