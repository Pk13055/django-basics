from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.views import generic


# Create your views here.

def index(request, number, name):
	context = {
		"number" : number,
		"name" : name
	}
	return render(request, 'polls/index.html.j2', context)

def form(request):
	return render(request, 'polls/form.html.j2')

class Detail(generic.DetailView):
	model = Question
	template_name = "polls/index.html.j2"
