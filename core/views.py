from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'Hello {nome}, você tem {idade} anos')

def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse(f'A soma dos números é {soma}.')

def sub(request, n1, n2):
    sub = n1 - n2
    return HttpResponse(f'A diferença dos números é {sub}.')

def mult(request, n1, n2):
    mult = n1 * n2
    return HttpResponse(f'O produto dos números é {mult}.')

def div(request, n1, n2):
    div = n1 / n2
    return HttpResponse(f'O resto da divisão dos números é {div}.')