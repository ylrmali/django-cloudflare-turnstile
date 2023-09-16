from django.shortcuts import render
from main.forms import Forms

# Create your views here.

def index(request):
    '''
        use forms and recaptcha
    '''
    forms = Forms()
    return render(request, 'main/index.html', context= {'forms': forms})