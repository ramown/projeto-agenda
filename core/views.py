from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def index(request):
# 	return redirect('/agenda/')

@login_required(login_url='/login/')
def lista_eventos(request):
	usuario = request.user
	eventos = Evento.objects.filter(usuario=usuario)
	#eventos = Evento.objects.all()
	dados = {'eventos': eventos}
	return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def logout_user(request):
	logout(request)
	return redirect('/')


def login_user(request):
	return render(request, 'login.html')

def submit_login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		usuario = authenticate(username=username, password=password)
		if usuario is not None:
			login(request, usuario)
			return redirect('/')
		else:
			messages.error(request, "Usuário ou senha incorreto(s)")

	return redirect('/')
