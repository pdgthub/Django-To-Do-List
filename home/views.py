
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    template = loader.get_template('home/home.html')
    
    context = {
        'variable': 'value',
    }
    return HttpResponse(template.render(context, request))

