from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

def index(request):
	html = get_template('index.html')
	c = Context()
	return HttpResponse(html.render(c))

def transaction(request):
	html = get_template('transaction.html')
	c = Context()
	return HttpResponse(html.render(c))

def checkbook(request):
	html = get_template('checkbook.html')
	c = Context()
	return HttpResponse(html.render(c))

def register(request):
	html = get_template('register.html')
	c = Context()
	return HttpResponse(html.render(c))
