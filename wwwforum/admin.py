from django.contrib import admin
from .models import Sekce, Vlakno, Prispevek

# Register your models here.

admin.site.register(Sekce)
admin.site.register(Vlakno)
admin.site.register(Prispevek)