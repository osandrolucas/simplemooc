from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'usuario': 'Sandro Lucas Azevedo Ferreira'}) #Renderiza e Substitui variável
   #HttpResponse('Hello Word. É só fazer certo que funciona!')  #Sempre temos que retornar um httpresponse