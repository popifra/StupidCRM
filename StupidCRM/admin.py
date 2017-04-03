from django.contrib import admin

# Register your models here.
from .models import anagrafica
from .models import esiti
admin.site.register(anagrafica)
admin.site.register(esiti)
