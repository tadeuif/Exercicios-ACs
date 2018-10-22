from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {
		'title': 'E-Commerce FIT',
		'paragrafo1': 'Primeiro parágrafo',
		'paragrafo2': 'Segundo parágrafo',
		'alunos': ['Abelardo,', 'Lucas,', 'Kenny,', 'Ruan,', 'Erick,', 'Pedro'],
		'alunos2': [],
		'condicao1': True,
		'condicao2': False,
		'lista': [1, 2, 3, 4, 5]
	}
	return render(request, "index.html", context)

def login(request):
	return render(request, "login.html")

