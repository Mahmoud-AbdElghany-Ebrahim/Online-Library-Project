from django.shortcuts import render

# Create your views here.
def Ahome(request):
    return render(request , 'adminhome/adminH.html')
    