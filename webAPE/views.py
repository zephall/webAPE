from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def reportes(request):
    template = loader.get_template('reports.html')
    return HttpResponse(template.render())
    
# Create your views here.
