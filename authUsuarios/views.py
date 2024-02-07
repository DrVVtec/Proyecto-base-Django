from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def signup(request):
    if request.method == "GET":
        print('enviando formulario')
        return render(request,'signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
                usuario.save()
                return HttpResponse("Usuario creado correctamente.")
            except:
                return render(request,'signup.html',{
                    'form':UserCreationForm,
                    'mensaje':"El usuario ya existe."
                })
        return render(request,'signup.html',{
            'form':UserCreationForm,
            'mensaje':"La contraseña no coincide."
        })
        
    