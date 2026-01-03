from django.db import models

# Create your models here.
class Nashriyot(models.Model):
    name=models.CharField(max_length=50)
    locatsiya=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Kitob(models.Model):
    name=models.CharField(max_length=50)
    price=models.BigIntegerField()
    quantity=models.BigIntegerField()
    kelgan_sana=models.DateField()
    nashriyot=models.ForeignKey(
        Nashriyot,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name

class Sotuvchi(models.Model):
    name=models.CharField(max_length=50)
    tel=models.PositiveBigIntegerField()
    def __str__(self):
        return self.name
class Sotuv(models.Model):
    kitob=models.ForeignKey(
        Kitob,
        on_delete=models.CASCADE
    )
    sotuvchi=models.ForeignKey(
        Sotuvchi,
        on_delete=models.CASCADE
    )
    data=models.DateField()
    quantity=models.BigIntegerField()
    



