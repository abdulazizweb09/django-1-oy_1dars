from django.contrib import admin
from.models import *
# Register your models here.



class UstozAdmin(admin.ModelAdmin):
    list_display=['name','age','jins','daraja','fan']
    search_fields=['name']

class FanAdmin(admin.ModelAdmin):
    list_display=['name','asosiy','yonalish']
    list_filter=['asosiy','yonalish']
    search_fields=['name']


class YonalishAdmin(admin.ModelAdmin):
    list_display=['name','activ']
    search_fields=['name']
    list_filter=['activ']



admin.site.register(Yonalish,YonalishAdmin)
admin.site.register(Fan,FanAdmin)
admin.site.register(Ustoz,UstozAdmin)