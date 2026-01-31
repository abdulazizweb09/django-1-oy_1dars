from django.contrib import admin
from .models import *
# Register your models here.

class KutubxonachiAdmin(admin.ModelAdmin):
    list_display=['name','start','end']
    search_fields=['name',]
    # ordering=('name',)
    list_filter=['start','end']



class MuallifAdmin(admin.ModelAdmin):
    list_display=['id','name','age','jins','deta','quantity','tric']
    search_fields=['name',]
    list_display_links=['id','name']
    list_filter=['tric',]
    list_editable=['quantity','tric']

class KitobAdmin(admin.ModelAdmin):
    search_fields=['name']


class TalabaAdmin(admin.ModelAdmin):
    search_fields=['name']


class RecordAdmin(admin.ModelAdmin):
    list_display=['id','talaba','kitob','admin','olingan_sana','qaytarish_sana']
    # search_fields=['name',]
    # list_display_links=['id','name']
    # list_filter=['tric',]
    # list_editable=['quantity','tric']

    autocomplete_fields=['admin','kitob','talaba']

admin.site.register(Talaba,TalabaAdmin)
admin.site.register(Kutubxonachi,KutubxonachiAdmin)
admin.site.register(Kitob,KitobAdmin)
admin.site.register(Record,RecordAdmin)
admin.site.register(Muallif,MuallifAdmin)
# admin.site.register()