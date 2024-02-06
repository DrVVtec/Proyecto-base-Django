from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Proyecto, Tarea
from .forms import CreateNewProyect, CreateNewTask
# Create your views here.

def index(request):
  return render(request,'index.html')

def proyects(request):
  lista_proyectos = Proyecto.objects.all() 
  return render(request,'proyects.html',{'lista_proyectos':lista_proyectos})

def create_proyect(request):
  if request.method =='GET':
    # Muestra página
    return render(request,'proyect_create.html',{
    'form':CreateNewProyect()
  })
  else:
    Proyecto.objects.create(
      name=request.POST['name'],
      tipo=request.POST['tipo'],
      responsable=request.POST['responsable'])
    return redirect('/proyects/')
    

def tasks(request):
  return render(request,'tasks.html')

def proyect_tasks(request,id):
  #print(id)
  #proyect = Proyecto.objects.get(id=id)
  proyect = get_object_or_404(Proyecto,id=id)
  #print(proyect.name)
  lista_tareas = Tarea.objects.filter(proyecto_id=id)
  #print(tasks)
  return render(request,'proyect_tasks.html',{
    "proyect":proyect,
    "lista_tareas":lista_tareas,
  })

def create_task(request,id):
  if request.method =='GET':
    # Muestra página
    return render(request,'task_create.html',{
    'form':CreateNewTask()
  })
  else:
    proyect = get_object_or_404(Proyecto,id=id)
    Tarea.objects.create(
      titulo=request.POST['titulo'],
      descripcion=request.POST['descripcion'],
      prioridad=request.POST['prioridad'],
      fecha_asignacion=request.POST['fecha_asignacion'],
      fecha_limite=request.POST['fecha_limite'],
      #fecha_entrega=request.POST['fecha_entrega'],
      proyecto=proyect)
    return redirect('myapp_proyect_tasks',id)
    
def delete_task(request, id_t):
  task = get_object_or_404(Tarea,id=id_t)
  task.delete()
  id_p = 1
  return redirect('myapp_proyect_tasks',id_p)

    


def hello(request):
  return HttpResponse("<h1>Hello World</h1>")

def about(request):
  return render(request,'about.html')
