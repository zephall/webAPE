from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login (request, user)
                    return HttpResponse('auth success')
                else:
                    return HttpResponse('disabled acc')
            else:
                return HttpResponse('Invalid Log')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})
    
# Create your views here.
