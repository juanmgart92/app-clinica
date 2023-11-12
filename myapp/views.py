from django.shortcuts import render, redirect

from django.urls import reverse


from .models import RecursosHumanos , PersonalAdministrativo , Enfermera , Medicos , Citas


def login(request):
    if request.method == 'POST':
        # Procesar la autenticación si la solicitud es POST
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
        
        try:
            recursos_humanos = RecursosHumanos.objects.get(usuario=username)
        except RecursosHumanos.DoesNotExist:
            recursos_humanos = None
        
    
        if recursos_humanos is not None and recursos_humanos.password == password:
            # Autenticación exitosa, redirige a la página deseada

            if recursos_humanos.rol == 'Recursos humanos':
                return redirect('recursosHumanos')
            elif recursos_humanos.rol == 'Personal administrativo':
                return redirect('personalAdministrativo')
            elif recursos_humanos.rol == 'Enfermera':
                return redirect('enfermera')
            elif recursos_humanos.rol == 'Medicos':

               return redirect(reverse('medicos') + f'?mensaje={recursos_humanos.cedula}')


            
            return redirect('recursosHumanos')

    
    return render(request, 'login.html')

def recursosHumanos(request):

    if request.method == 'POST':
        # Procesar el formulario si la solicitud es un POST
        nombre = request.POST.get('nombre', '')
        cedula = request.POST.get('cedula', '')
        correo = request.POST.get('correo', '')
        telefono = request.POST.get('telefono', '')
        fecha_nacimiento = request.POST.get('fecha_nacimiento', '')
        direccion = request.POST.get('direccion', '')
        rol = request.POST.get('rol', '')
        usuario = request.POST.get('usuario', '')
        password = request.POST.get('password', '')
        licencia = request.POST.get('licencia', '')

        datos = {
            'nombre':nombre,
            'cedula':cedula,
            'correo':correo,
            'telefono':telefono,
            'fecha_nacimiento':fecha_nacimiento,
            'direccion':direccion,
            'rol':rol,
            'usuario':usuario,
            'password':password,
            'licencia':licencia
        }

        try:
            instancia = RecursosHumanos.objects.get(cedula=cedula)
        except RecursosHumanos.DoesNotExist:
            # La instancia con esta cédula no existe, crea una nueva
            RecursosHumanos.objects.create(
            nombre = nombre,
            cedula=cedula,
            correo=correo,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            rol=rol,
            usuario=usuario,
            password=password,
            licencia=licencia
            )

            print('se creo un nuevo usuario')
        else:
            # La instancia con esta cédula ya existe, actualiza sus campos con los nuevos datos
            for campo, valor in datos.items():
                setattr(instancia, campo, valor)
            instancia.save()

            print('se actualizo la informacion')

    

    # Si la solicitud es GET o no se ha procesado aún, simplemente renderiza el formulario
    return render(request, 'recursosHumanos.html')

def personalAdministrativo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        cedula = request.POST.get('cedula', '')
        fecha_nacimiento = request.POST.get('fecha_nacimiento', '')
        genero = request.POST.get('genero', '')
        direccion = request.POST.get('direccion', '')
        telefono = request.POST.get('telefono', '')
        correo = request.POST.get('correo', '')
        nombre_contacto_emergencia = request.POST.get('nombre_contacto_emergencia', '')
        relacion_paciente = request.POST.get('relacion_paciente', '')
        numero_emergencia = request.POST.get('numero_emergencia', '')
        nombre_compania_seguros = request.POST.get('nombre_compania_seguros', '')
        numero_poliza = request.POST.get('numero_poliza', '')
        estado_poliza = request.POST.get('estado_poliza', '')

        #--
        fecha = request.POST.get('fecha_cita', '')
        hora  = request.POST.get('hora_cita', '')

        datos = {
            'nombre': nombre,
            'cedula': cedula,
            'fecha_nacimiento': fecha_nacimiento,
            'genero': genero,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo,
            'nombre_contacto_emergencia': nombre_contacto_emergencia,
            'relacion_paciente': relacion_paciente,
            'numero_emergencia': numero_emergencia,
            'nombre_compania_seguros': nombre_compania_seguros,
            'numero_poliza': numero_poliza,
            'estado_poliza': estado_poliza,
        }

        datos2 = {
            'nombre': nombre,
            'cedula': cedula,
            'fecha': fecha,
            'hora': hora
        }



        try:
            instancia = PersonalAdministrativo.objects.get(cedula=cedula)
            instancia2 = Citas.objects.get(cedula=cedula)
        except PersonalAdministrativo.DoesNotExist:
            # La instancia con esta cédula no existe, crea una nueva
            PersonalAdministrativo.objects.create(
            nombre= nombre,
            cedula= cedula,
            fecha_nacimiento= fecha_nacimiento,
            genero= genero,
            direccion= direccion,
            telefono= telefono,
            correo= correo,
            nombre_contacto_emergencia= nombre_contacto_emergencia,
            relacion_paciente= relacion_paciente,
            numero_emergencia= numero_emergencia,
            nombre_compania_seguros= nombre_compania_seguros,
            numero_poliza= numero_poliza,
            estado_poliza= estado_poliza,
            )


            Citas.objects.create(
                nombre = nombre ,
                cedula = cedula,
                fecha = fecha,
                hora = hora
            )

            print('se creo un nuevo usuario')
        else:
            # La instancia con esta cédula ya existe, actualiza sus campos con los nuevos datos
            for campo, valor in datos.items():
                setattr(instancia, campo, valor)

            for campo, valor in datos2.items():
                setattr(instancia, campo, valor)

            instancia.save()

            instancia2.save()


            print('se actualizo la informacion')

    

        

    return render(request,'personal.html')


def enfermera(request):
    error_message = None
    paciente = None
    guardar_exitoso = False

    cedula = ' '

    if request.method == 'POST':
        if 'verificar_cedula' in request.POST:
            # Verificar cédula
            cedula = request.POST.get('cedula')

            try:
                paciente = PersonalAdministrativo.objects.get(cedula=cedula)
            except PersonalAdministrativo.DoesNotExist:
                error_message = 'Cédula no encontrada.'
        elif 'guardar_datos' in request.POST:

            presion_arterial = request.POST.get('presion_arterial')
            temperatura = request.POST.get('temperatura')
            pulso = request.POST.get('pulso')
            nivel_oxigeno_sangre = request.POST.get('nivel_oxigeno_sangre')

            enfermera = Enfermera.objects.create(
                cedula=request.POST.get('cedula'),
                presion_arterial=presion_arterial,
                temperatura	=temperatura,
                pulso=pulso,
                nivel_oxigeno_sangre=nivel_oxigeno_sangre,
            )

            print(enfermera)

    return render(request, 'enfemera.html', {'paciente': paciente, 'error_message': error_message, 'guardar_exitoso': guardar_exitoso , 'campo_cedula':cedula})


def medicos(request):

    cedula_medico_login =  request.GET.get('mensaje', None)

    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        fecha = request.POST.get('fecha')
        cedula_medico = request.POST.get('cedula_medico')
        motivo_consulta = request.POST.get('motivo_consulta')
        sintomatologia = request.POST.get('sintomatologia')
        dianostico = request.POST.get('diagnosticoo')
        numero_orden_medicamentos = request.POST.get('numero_orden_medicamentos')
        nombre_medicamento = request.POST.get('nombre_medicamento')
        dosis = request.POST.get('dosis')
        duracion = request.POST.get('duracion')

        #--
        numero_orden_diagnostico = request.POST.get('numero_orden_diagnostico')
        nombre_diagnostico = request.POST.get('nombre_diagnostico')
        cantidad_diagnostico = request.POST.get('cantidad_diagnostico')
        requiere_asistencia_diagnostico = request.POST.get('requiere_asistencia_diagnostico')
        #--
        numero_orden_procedimiento = request.POST.get('numero_orden_procedimiento')
        nombre_procedimiento = request.POST.get('nombre_procedimiento')
        cantidad_procedimiento = request.POST.get('cantidad_procedimiento')
        frecuencia_procedimiento = request.POST.get('frecuencia_procedimiento')
        requiere_asistencia_procedimiento = request.POST.get('requiere_asistencia_procedimiento')


        datos = {
            'cedula':cedula ,
            'fecha': fecha,
            'cedula_medico' : cedula_medico,
            'motivo_consulta' : motivo_consulta,
            'sintomatologia' : sintomatologia,
            'dianostico' : dianostico,
            'numero_orden_medicamentos' : numero_orden_medicamentos,
            'nombre_medicamento' : nombre_medicamento,	
            'dosis' : dosis , 
            'duracion' : duracion,
            'numero_orden_procedimiento' : numero_orden_procedimiento,
            'nombre_procedimiento' : nombre_procedimiento,
            'cantidad_procedimento' : cantidad_procedimiento,
            'frecuencia_procedimiento' : frecuencia_procedimiento,
            'requiere_asistencia_especialista' : requiere_asistencia_procedimiento,
            'numero_orden_dianostico' : numero_orden_diagnostico,
            'nombre_dianostico' : nombre_diagnostico,
            'cantidad_dianostico' : cantidad_diagnostico,
            'requiere_asistencia_dianostico' : requiere_asistencia_diagnostico,	
        }

        try:
            instancia = Medicos.objects.get(cedula=cedula)
        except Medicos.DoesNotExist:
            # La instancia con esta cédula no existe, crea una nueva
            Medicos.objects.create(
            cedula=cedula ,
            fecha= fecha,
            cedula_medico = cedula_medico,
            motivo_consulta = motivo_consulta,
            sintomatologia = sintomatologia,
            dianostico = dianostico,
            numero_orden_medicamentos = numero_orden_medicamentos,
            nombre_medicamento = nombre_medicamento,	
            dosis = dosis , 
            duracion = duracion,
            numero_orden_procedimiento = numero_orden_procedimiento,
            nombre_procedimiento = nombre_procedimiento,
            cantidad_procedimento = cantidad_procedimiento,
            frecuencia_procedimiento = frecuencia_procedimiento,
            requiere_asistencia_especialista = requiere_asistencia_procedimiento,
            numero_orden_dianostico = numero_orden_diagnostico,
            nombre_dianostico = nombre_diagnostico,
            cantidad_dianostico = cantidad_diagnostico,
            requiere_asistencia_dianostico = requiere_asistencia_diagnostico,	
            )

            print('se creo un nuevo usuario')
        else:

            if instancia.numero_orden_medicamentos == numero_orden_medicamentos:
                # La instancia con esta cédula ya existe, actualiza sus campos con los nuevos datos
                for campo, valor in datos.items():
                    setattr(instancia, campo, valor)
                instancia.save()

                print('se actualizo la informacion')

    return render(request , 'medicos.html' ,  {'mensaje': cedula_medico_login})