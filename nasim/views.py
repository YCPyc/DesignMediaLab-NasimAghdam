from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def home(request):
    bio = BiographyM.objects.all()
    ani = AnimalM.objects.all()
    veg = VeganismM.objects.all()
    immi = ImmigrantM.objects.all()
    fam = FamilyM.objects.all()
    context = {'bio':bio,'ani':ani,'veg':veg,'immi':immi,'fam':fam}
    return render(request,'nasim/dashboard.html',context);

def Biography(request, pk):
    event = BiographyM.objects.get(name = pk)
    ani = None
    veg = None
    immi = None
    fam = None
    names = []

    if AnimalM.objects.filter(name = pk).exists():
        ani = AnimalM.objects.all()
    names.append("Animal")
    if VeganismM.objects.filter(name = pk).exists():
        veg = VeganismM.objects.all()
    names.append("Veganism")
    if ImmigrantM.objects.filter(name = pk).exists():
        immi = ImmigrantM.objects.all()
    names.append("Immigrant")
    if FamilyM.objects.filter(name = pk).exists():
        fam = FamilyM.objects.all()
    names.append("Family")


    context = {'event':event,'r1':ani,'r2':veg,'r3':immi,'r4':fam,'tags':names}
    return render(request,'nasim/detail.html',context);

def Animal(request, pk):
    bio = None
    veg = None
    immi = None
    fam = None
    names = []

    if BiographyM.objects.filter(name = pk).exists():
        bio = BiographyM.objects.all()
    names.append("Biography")
    
    if VeganismM.objects.filter(name = pk).exists():
        veg = VeganismM.objects.all()
    names.append("Veganism")

    if ImmigrantM.objects.filter(name = pk).exists():
        immi = ImmigrantM.objects.all()
    names.append("Immigrant")

    if FamilyM.objects.filter(name = pk).exists():
        fam = FamilyM.objects.all()
    names.append("Family")

   
    event = AnimalM.objects.get(name = pk)
    context = {'event':event,'r1':bio,'r2':veg,'r3':immi,'r4':fam,'tags':names}
    return render(request,'nasim/detail.html',context);

def Veganism(request, pk):
    bio = None
    ani = None
    immi = None
    fam = None
    names = []

    if BiographyM.objects.filter(name = pk).exists():
        bio = BiographyM.objects.all()
    names.append("Biography")
    if AnimalM.objects.filter(name = pk).exists():
        ani = AnimalM.objects.all()
    names.append("Veganism")
    if ImmigrantM.objects.filter(name = pk).exists():
        immi = ImmigrantM.objects.all()
    names.append("Immigrant")
    if FamilyM.objects.filter(name = pk).exists():
        fam = FamilyM.objects.all()
    names.append("Family")

    
    event = VeganismM.objects.get(name = pk)
    context = {'event':event,'r1':bio,'r2':ani,'r3':immi,'r4':fam,'tags':names}
    return render(request,'nasim/detail.html',context);

def Family(request, pk):
    bio = BiographyM.objects.all()
    ani = AnimalM.objects.all()
    veg = VeganismM.objects.all()
    immi = ImmigrantM.objects.all()
    event = FamilyM.objects.get(name = pk)
    context = {'event':event}
    return render(request,'nasim/detail.html',context);

def Immigration(request, pk):
    bio = BiographyM.objects.all()
    ani = Animal.objects.all()
    veg = VeganismM.objects.all()
    fam = FamilyM.objects.all()
    event = ImmigrantM.objects.get(name = pk)
    context = {'event':event}
    return render(request,'nasim/detail.html',context);