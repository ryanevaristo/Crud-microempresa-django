from django.shortcuts import render

# Create your views here.

form = MeuForm(request.POST, request.FILES)
