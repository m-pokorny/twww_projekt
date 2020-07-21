from django.urls import path
from . import views


urlpatterns = [
	path('',views.index, name = 'index'),
	path('vlakno/<int:vlakno_id>', views.vlakno, name='vlakno'),
	
	
]
