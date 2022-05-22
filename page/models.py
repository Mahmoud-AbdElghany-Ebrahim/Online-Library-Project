from django.db import models

class Book(models.Model) :
    statu = [
        ('avalible', 'avalible'),
        ('borrowed','borrowed'),
    ]
    title =models.CharField(max_length=200)
    ISPN = models.IntegerField(null=True, blank=True)
    publisherYear = models.IntegerField(null=True, blank=True)
    author = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=statu, null=True, blank=True)
    photo_book = models.ImageField(upload_to='Photo' , null=True, blank=True)
    borrowing_price_day = models.DecimalField(max_digits=6 ,decimal_places=2 , null=True, blank=True)
    borrowing_period = models.IntegerField(null= True ,blank=True) 
    def __str__(self) :
        return self.title