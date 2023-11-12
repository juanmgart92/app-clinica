from django.contrib import admin

from .models import PersonalAdministrativo , RecursosHumanos , Medicos ,Enfermera
# Register your models here.

admin.site.register(PersonalAdministrativo)
admin.site.register(RecursosHumanos)
admin.site.register(Medicos)
admin.site.register(Enfermera)

