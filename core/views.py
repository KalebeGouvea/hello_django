from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'Hello {nome}, você tem {idade} anos')
