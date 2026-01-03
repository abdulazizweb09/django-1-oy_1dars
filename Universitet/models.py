from django.db import models

# Create your models here.
class Yonalish(models.Model):
    name=models.CharField(max_length=50)
    activ=models.BooleanField()
    def __str__(self):
        return self.name

class Fan(models.Model):
    test=models.CharField
    name=test(max_length=50)
    asosiy=models.BooleanField()
    yonalish=models.ForeignKey(
        Yonalish,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name

class Ustoz(models.Model):
    char=models.CharField
    num=models.BigIntegerField
    forign=models.ForeignKey


    name=char(max_length=50)
    age=num()
    jins=char(
        max_length=100,
        choices=[
            ('Erkak','Erkak'),
            ('Ayol','Ayol')
            ]
    )
    daraja=char(
        choices=[
            ('Bakalavr','Bakalavr'),
            ('Magistr','Magistr')
        ]
    )
    fan=forign(
        Fan,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
