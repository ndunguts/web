from django.db import models

# Create your models here.
from django.db import models





# Create your models here.

CATEGORY_CHOICES=(
    ('ACTION','ACTION'),
    ('DRAMA','DRAMA'),
    ('COMEDY','COMEDY'),
    ('ROMANCE','ROMANCE'),
    ('AGASOBANUYE','AGASOBANUYE')
)


LANGUAGE_CHOICES=(
    ('ENGLISH','ENGLISH'),
    ('FRANCE','FRANCE'),
    ('KINYARWANDA','KINYARWANDA')


)

STATUS_CHOICES= (
    ('RECRNITLY ADDED ','RECRNITLY ADDED'),
    ('MOST WATCHED','MOST WATCHED'),
    ('TOP RATED','TOP RATED')
)

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    image=models.ImageField(upload_to='movies')
    categor=models.CharField(choices=CATEGORY_CHOICES,max_length=11)
    language=models.CharField(choices=LANGUAGE_CHOICES , max_length=11)
    status=models.CharField(choices=STATUS_CHOICES,max_length=16)
    year_of_product=models.DateField()
    views=models.IntegerField(default=0)
    video=models.FileField(upload_to="video/" )

    def __str__(self):
        return (self.title)




class tv(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)   


    def __str__(self):
        return (self.name)
             

