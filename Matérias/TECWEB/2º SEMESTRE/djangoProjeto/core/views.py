from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {
		'title': 'E-Commerce FIT',
		'paragrafo1': 'Primeiro parágrafo',
		'paragrafo2': 'Segundo parágrafo'
	}
	return render(request, "index.html", context)

def login(request):
	if request.method == "GET":
		print("Acesso via GET")
	else:
		print("Acesso via POST")
	return render(request, "login.html")