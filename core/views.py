from django.shortcuts import render


def index(request):
    return render(request,"core/index.html")

def services(request):
    return render(request,"core/services.html")

def a_propos(request):
    return render(request,"core/a_propos.html")

def astuces(request):
    return render(request,"core/astuces.html")
def a_propos(request):
    return render(request,"core/a_propos.html")