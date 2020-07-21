from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Sekce,  Vlakno, Prispevek, PrispevekForm
# Create your views here.

def index(request):
	seznam_sekci = Sekce.objects.order_by('poradi')

	slovnik = {}

	for s in seznam_sekci:
		vlakna = Vlakno.objects.filter(materska_sekce = s.pk)
		slovnik_vlaken={}
		for v in vlakna:
			posledni_prispevek = Prispevek.objects.filter(materske_vlakno = v.pk).order_by('-vytvoreno').first()
			slovnik_vlaken[v] = posledni_prispevek

		slovnik[s] = slovnik_vlaken
			

	
	
	return render( request, 'forum/index.html' , {'slovnik':slovnik})



def vlakno(request, vlakno_id):

	try:
			vlakno = Vlakno.objects.get(pk = vlakno_id)
	except Vlakno.DoesNotExist:
		raise Http404('Stránka neexistuje')

	if request.method == 'POST':
		form = PrispevekForm(request.POST)
		if form.data['obsah'] != '':
			novy_prispevek = Prispevek()
			novy_prispevek.autor = request.user
			novy_prispevek.obsah = form.data['obsah']
			novy_prispevek.materske_vlakno = vlakno
			novy_prispevek.save()

		return redirect('/vlakno/{}'.format(vlakno_id))

	else:
		
		seznam_prispevku = Prispevek.objects.filter(materske_vlakno = vlakno_id).order_by('vytvoreno')
		form = PrispevekForm()
		return render(request, 'forum/vlakno.html',{'seznam_prispevku':seznam_prispevku, 'vlakno':vlakno,'form':form})

def registrace(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')			
			
	else:
		form = UserCreationForm()

	
	return render(request, 'forum/registrace.html', {'form': form})