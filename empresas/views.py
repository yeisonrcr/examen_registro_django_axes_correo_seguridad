from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homeEmpresas(request):
    return render (request,'empresas/home_empresas.html')