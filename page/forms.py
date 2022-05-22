from django import forms
from django.forms import widgets
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'ISPN',
            'publisherYear',
            'author',
            'status',
            'borrowing_price_day',
            'borrowing_period',
            'photo_book',   
        ]
class BorrowForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'status',
            'borrowing_period',           
        ]

class ExtendForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'borrowing_period',
        ]