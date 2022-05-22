from django.shortcuts import render, redirect
from .models import Student,Admin
from django.contrib import auth
def signUp(request):
    
    Fname=request.POST.get('Fname')
    Lname=request.POST.get('Lname')
    email=request.POST.get('Email')
    password=request.POST.get('password')
    Cpassword=request.POST.get('Con-password')
    phoneNum=request.POST.get('PhoneNum')
    Bdate=request.POST.get('Bdate')
    user=request.POST.get('User')
    global data
    if user=='Student':
        if password==Cpassword:
            data = Student(Fname=Fname, Lname=Lname, email=email, password=password, phoneNum=phoneNum, Bdate=Bdate )
            data.save()
            return render(request,'studenthome/student.html')
    elif user=='Admin':
         if password==Cpassword:
             data = Admin(Fname=Fname, Lname=Lname, email=email, password=password, phoneNum=phoneNum, Bdate=Bdate )
             data.save()
             return render(request,'adminhome/adminH.html')
    else:
        return render (request,'Accounts/signUp.html')   
 
def logIn(request):
    if request.method=='POST':
        email=request.POST.get('Email')
        password=request.POST.get('password')
        data=auth.authenticate(email=email, password=password)
        if data is not None:
            return render(request,'adminhome/adminH.html')
        else:
            return render(request,'adminhome/adminH.html')
    else:
        return render(request, 'Accounts/LogIn.html')

def update(request, id):
  user_id = Student.objects.get(id = id)
  if request.method =='POST':
    user_update =update(request.POST , request.FILES, instance =user_id)
    if user_update.is_valid():
      user_update.save()
      return redirect(signUp)
  else:
    user_update= update(instance=user_id)
  context ={
    'form' : user_update,
  }
  return render(request ,'Accounts/Updates.html',context)