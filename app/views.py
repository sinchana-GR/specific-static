from django.shortcuts import render

# Create your views here.
def specific_static(request):
    return render(request,'specific_static.html')
def music_waves(request):
    return render(request,'music_waves.html')
def swiggy(request):
    return render(request,'swiggy.html')
def assign(request):
    return render(request,'assign.html')
def assignment_form(request):
    return render(request,'assignment_form.html')
def html_form(request):
    return render(request,'html_form.html')
def hubspot(request):
    return render(request,'hubspot.html')
def opendoors(request):
    return render(request,'opendoors.html')
def touch(request):
    return render(request,'touch.html')
    