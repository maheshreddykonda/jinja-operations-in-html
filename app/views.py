from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':200,'b':300}
    return render(request,'conditions.html',context=d)
