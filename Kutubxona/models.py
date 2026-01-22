from django.db import models
from datetime import datetime
# Create your models here.
class Talaba(models.Model):
    name=models.CharField(max_length=50)
    guruh=models.CharField(max_length=100)
    kurs=models.CharField(max_length=100)
    quantity=models.BigIntegerField()
    def __str__(self):
        return self.name

class Muallif(models.Model):
    name=models.CharField(max_length=50)
    age=models.BigIntegerField()
    jins=models.CharField(
        choices=[
            ('Erkak','Erkak'),
            ('Ayol','Ayol')
        ]
    )
    deta=models.DateField(default=datetime.now())
    quantity=models.BigIntegerField()
    tric=models.BooleanField()

    def __str__(self):
        return self.name

class Kitob(models.Model):
    name=models.CharField(max_length=50)
    janr=models.CharField(max_length=100)
    sahifa=models.BigIntegerField()
    muallif=models.ForeignKey(
        Muallif,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Kutubxonachi(models.Model):
    name=models.CharField(max_length=50)
    start=models.TimeField()
    end=models.TimeField()

    def __str__(self):
        return self.name


class Record(models.Model):
    talaba=models.ForeignKey(
        Talaba,
        on_delete=models.CASCADE
    )
    kitob=models.ForeignKey(
        Kitob,
        on_delete=models.CASCADE
    )
    admin=models.ForeignKey(
        Kutubxonachi,
        on_delete=models.CASCADE
    )
    olingan_sana=models.DateField()
    qaytarish_sana=models.DateField()