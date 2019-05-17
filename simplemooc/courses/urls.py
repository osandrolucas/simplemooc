from django.conf.urls import path

from simplemooc.courses import views

app_name = 'index'
urlpatterns = [
    path('index', views.index, name='index'), #Apenas curso, a vazia, será a view cursos que está em simplemooc.courses.view
]
