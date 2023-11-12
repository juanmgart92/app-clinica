from pyexpat import model
from sys import maxsize
from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class RecursosHumanos(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)   
    telefono =models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    licencia = models.CharField(max_length=100)

class PersonalAdministrativo(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    nombre_contacto_emergencia = models.CharField(max_length=100)
    relacion_paciente = models.CharField(max_length=100)
    numero_emergencia = models.CharField(max_length=100)
    nombre_compania_seguros = models.CharField(max_length=100)
    numero_poliza = models.CharField(max_length=100)
    estado_poliza = models.CharField(max_length=100)

class Enfermera(models.Model):
    cedula = models.CharField(max_length=100)
    presion_arterial = models.CharField(max_length=100)
    temperatura = models.CharField(max_length=100)
    pulso = models.CharField(max_length=100)
    nivel_oxigeno_sangre = models.CharField(max_length=100)

class Medicos(models.Model):
    cedula = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    cedula_medico = models.CharField(max_length=100)
    motivo_consulta = models.CharField(max_length=100)
    sintomatologia = models.CharField(max_length=100)
    dianostico = models.CharField(max_length=100)
    numero_orden_medicamentos = models.CharField(max_length=100)
    nombre_medicamento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    #--
    numero_orden_procedimiento = models.CharField(max_length=100)
    nombre_procedimiento = models.CharField(max_length=100)
    cantidad_procedimento = models.CharField(max_length=100)
    frecuencia_procedimiento = models.CharField(max_length=100)
    requiere_asistencia_especialista = models.CharField(max_length=100)
    #--
    numero_orden_dianostico = models.CharField(max_length=100)
    nombre_dianostico = models.CharField(max_length=100)
    cantidad_dianostico = models.CharField(max_length=100)
    requiere_asistencia_dianostico = models.CharField(max_length=100)

class Medicamento(models.Model):
    numero_orden_medicamentos = models.CharField(max_length=100)
    nombre_medicamneto = models.CharField(max_length=100)


class Citas(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)









    
