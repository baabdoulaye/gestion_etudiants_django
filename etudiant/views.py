from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# cette fonction permet d'ajouter et d'afficher les informations d'un étudiant
def add_show(request):
    if request.method == "POST": 
        fm = StudentRegistration(request.POST)
        stud = User.objects.all()
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email = em, password = pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm = StudentRegistration(request.POST)
        stud = User.objects.all()
    return render(request, 'etudiant/updatestudent.html',{'id':id,})

# cette fonction permet de modifier les données
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    return render(request, 'etudiant/updatestudent.html')

# cette fonction permet de supprimer les données
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')