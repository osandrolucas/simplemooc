from django.urls import path
from simplemooc.core import views

#Se houver o arquivo de url vai para ele. Se não houver, vai para o do core.
app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]