from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from forms import MyRegistrationForm

# Create your views here.

def login(request):
 	 return render(request,'index.html',{params})

#def index(request):
#	html = get_template('index.html')
#	c = Context()
#	return HttpResponse(html.render(c))

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

def auth_view(request): 
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username = username, password = password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/checkbook/') #Logged in page
	else: 
		return HttpResponseRedirect('/accounts/invalid'); # Invalid login page

def loggedin(request):
	return render_to_response('transaction.html', {'username': request.user.username});	# Logged in page

def invalid_login(request):
	return render_to_response('index.html') # Invalid login page

def logout(request):
	auth.logout(request)
	return render_to_response('index.html') # Log out page

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/register_success') 

	args = {}
	args.update(csrf(request))
	args['form'] = MyRegistrationForm()

	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('checkbook.html')



