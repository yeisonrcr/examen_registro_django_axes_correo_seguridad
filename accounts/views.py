from django.shortcuts import render

# Create your views here.



def locked_out(request):
    return render(request, 'accounts/blocked/lock.html')
