# Create your views here.
from django.http import HttpResponse
from django.template import loader,Context
def index(req):
	t = loader.get_template('index.html')
	c = Context({})
	
	# return HttpResponse('<h1>hello welcome to Django!</h1>')
	return HttpResponse(t.render(c))
