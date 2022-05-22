from django.shortcuts import redirect, render , get_object_or_404
from .models import Book
from .forms import *

# Create your views here.

def index(request):
  title = None
  search = Book.objects.all()
  if 'search_name' in request.GET:
    title = request.GET['search_name']
    if title:
      search = search.filter(title__icontains= title)

  context ={
     'books' : search,
   }
  return render(request, 'page/Books.html' ,context)

def Student(request):
    title = None
    search = Book.objects.all()
    if 'search_name' in request.GET:
      title = request.GET['search_name']
      if title:
        search = search.filter(title__icontains= title)

    context ={
      'books' : search,
    }
    return render(request, 'page/BookStudent.html' ,context)


def add(request):
  if request.method =='POST':
    AddBook = BookForm(request.POST, request.FILES, request.FILES)
    if AddBook.is_valid():
      AddBook.save()
      return redirect(index)
  context ={
     'form' : BookForm(),
   }
  return render(request, 'page/addBook.html', context)

def update(request, id):
  book_id = Book.objects.get(id = id)
  if request.method =='POST':
    book_update =BookForm(request.POST , request.FILES, instance =book_id)
    if book_update.is_valid():
      book_update.save()
      return redirect(index)
  else:
    book_update = BookForm(instance=book_id)
  context ={
    'form' : book_update,
  }
  return render(request ,'page/update.html',context)



def borrowed(request, id):
  book_id = Book.objects.get(id=id)
  book_id.status = 'borrowed'
  book_id.borrowing_period = 10
  book_id.save(update_fields = ['status'])
  book_id.save(update_fields = ['borrowing_period'])
  return redirect(Student)

def returned(request, id):
  book_id = Book.objects.get(id=id)
  book_id.status = 'active'
  book_id.borrowing_period = 0
  book_id.save(update_fields = ['status'])
  book_id.save(update_fields = ['borrowing_period'])
  return redirect(Student)

def extend(request, id):
  book_id = Book.objects.get(id = id)
  if request.method =='POST':
    extend_book =ExtendForm(request.POST , instance =book_id)
    if extend_book.is_valid():
      extend_book.save()
      return redirect(Student)
  else:
    extend_book = ExtendForm(instance=book_id)
  context ={
    'form' : extend_book,
  }
  return render(request ,'page/extend_period.html',context)


def delete(request, id):
  book_delete = get_object_or_404(Book ,id = id)
  if request.method =='POST':
    book_delete.delete()
    return redirect('/Books/allBooks')
  return render (request, 'page/Delete.html')