from django.contrib import admin
from django.urls import path

from simplemooc.core import views #Importando a função home do arquivo views.py
from simplemooc.courses import views #Importando a função home do arquivo views.py

urlpatterns = [
    path('', views.index, name='home'),#Para URL vazia, execute a função simplemooc.core.view.home chamada home
    path('cursos/', views.courses(), namspace='index'),
    path('contato/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
