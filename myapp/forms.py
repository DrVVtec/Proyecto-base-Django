from django import forms

class CreateNewProyect(forms.Form):
    name = forms.CharField(label="Nombre del proyecto:",max_length=200)
    tipos_proyectos = [
        ("Interno","Proyecto Interno"),
        ("demo","Demo para prospecto"),
        ("act","Proyecto activo"),
        ("fin","Proyecto completado")
    ]
    tipo = forms.ChoiceField(label="Tipo de proyecto:",choices = tipos_proyectos)
    #tipo = forms.CharField(label="Tipo proyecto:",max_length=100)
    responsable = forms.CharField(label="Responsable:",max_length=100)

class CreateNewTask(forms.Form):
    titulo = forms.CharField(label="Título:",max_length=200)
    descripcion = forms.CharField(label="Descripción:",widget=forms.Textarea)
    #proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    tipo_prioridad = [
        (1,"Alta"),
        (2,"Media"),
        (3,"Baja"),
        (4,"Opcional")
    ]
    prioridad = forms.ChoiceField(label="Prioridad",choices=tipo_prioridad)
    fecha_asignacion = forms.DateField()
    fecha_limite = forms.DateField()
    #fecha_entrega = forms.DateField(required=False)