from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
#from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

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
                login(request,usuario)
                return redirect('myapp_index')
                #return HttpResponse("Usuario creado correctamente.")
            except IntegrityError:
                return render(request,'signup.html',{
                    'form':UserCreationForm,
                    'mensaje':"El usuario ya existe."
                })
        return render(request,'signup.html',{
            'form':UserCreationForm,
            'mensaje':"La contraseña no coincide."
        })
        
def signout(request):
    print("Entra al logout")
    logout(request)
    return redirect('authU_welcome')

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html",{
            'form':AuthenticationForm
        })
    else:
        print("Valida autenticación")
        print(request.POST)
        user= authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, "signin.html",{
            'form':AuthenticationForm,
            'mensaje':"username or password is incorrect."
        })
        else:
            login(request,user)
            return redirect('myapp_index')
        