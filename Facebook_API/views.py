from datetime import date

import facebook
import pandas as pd
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from Facebook_API.forms import GoogleForms
from Facebook_API.models import User_Facebook, Resultados, Formularios

Dia_de_hoy = date.today()


def GoogleData(values):
    # Leemos la url con el contenido de GoogleShet.
    Results = pd.read_csv(f"{values}/export?format=csv")

    # columnas del excel
    Columns = [
        'Marca temporal', 'Dirección de correo electrónico', 'Género', 'Rango de edad',
        '¿Qué tipo de baldosa o enchape de suelo es el ideal para la casa de tus sueños?',
        'A la hora de diseñar tu cocina, además de la funcionalidad, ¿Qué te atrae más en un salpicadero?',
        'El baño es la parte más tranquila de tu casa, ¿cómo te gustaría que se viera?',
        'Tus personas mas queridas lo primero que van a visitar de tu casa es la sala, '
        '¿Cómo te gustaría que fuese el aspecto de este lugar tan importante?',
    ]

    # Creamos un dataframe con las respectivas columnas y como datatype como objeto.
    df1 = pd.DataFrame(Results, columns=Columns, dtype='object')

    # Cambiar nombre de las columnas
    df1.rename(columns={
        'Marca temporal': 'Timestamp',
        'Dirección de correo electrónico': 'correo',
        'Género': 'genero',
        'Rango de edad': 'edad',
        '¿Qué tipo de baldosa o enchape de suelo es el ideal para la casa de tus sueños?': 'Tipo_baldosa',
        'A la hora de diseñar tu cocina, además de la funcionalidad, ¿Qué te atrae más en un salpicadero?': 'Tipo_Salpicadero',
        'El baño es la parte más tranquila de tu casa, ¿cómo te gustaría que se viera?': 'Tipo_Bano',
        'Tus personas mas queridas lo primero que van a visitar de tu casa es la sala, '
        '¿Cómo te gustaría que fuese el aspecto de este lugar tan importante?': 'Tipo_Sala'

    }, inplace=True)

    # cada variable contiene los resultados de cada columna.
    Timestamp = df1['Timestamp']
    correo = df1['correo']
    genero = df1['genero']
    edad = df1['edad']
    Tipo_baldosa = df1['Tipo_baldosa']
    Tipo_Salpicadero = df1['Tipo_Salpicadero']
    Tipo_Bano = df1['Tipo_Bano']
    Tipo_Sala = df1['Tipo_Sala']

    for TI, CO, GE, ED, TBAL, TSALPI, TBANO, TSALA in zip(Timestamp, correo, genero, edad, Tipo_baldosa,
                                                          Tipo_Salpicadero, Tipo_Bano, Tipo_Sala):
        print(CO)
        UsuarioRespuesta = User_Facebook.objects.get(email=CO)

        newResult = Resultados(
            Usuario_id=UsuarioRespuesta.pk,
            Timestamp=TI,
            correo=CO,
            genero=GE,
            edad=ED,
            Tipo_baldosa=TBAL,
            Tipo_Salpicadero=TSALPI,
            Tipo_Baño=TBANO,
            Tipo_Sala=TSALA,
        )
        # newResult.save()

        return print('CO')


def userDetails(request):
    # obtenmos los datos del usuario autenticado.
    social_user = request.user.social_auth.get(provider='facebook')

    # Obtenemos el token de acceso.
    Token = social_user.extra_data['access_token']

    # Validamos el token
    Graph = facebook.GraphAPI(Token)

    print(Graph)
    # Los datos del usuario que requerimos.
    datos = ['name, email, picture']

    # Obtenemos cada registro del usuario pasando la variable datos como parametro para fields.
    user_profile = Graph.get_object('me', fields=datos)

    # Cada variable contiene un dato del usuario autenticado.
    name = user_profile['name']
    email = user_profile['email']
    picture = user_profile['picture']['data']['url']

    # location = user_profile['location']['name']
    # gender = user_profile['gender']
    # birthday = user_profile['birthday']

    # filtramos por el email si el correo esta en la base de datos
    usuarioExistente = User_Facebook.objects.filter(email=email)

    if usuarioExistente:
        return redirect('api:campañas')
    else:
        # llamamos el modelo de la base de datos, pasamos cada variable y guardamos.
        newUser = User_Facebook(
            name=name,
            email=email,
            picture=picture
            # location=location,
            # gender=gender,
            # birthday=birthday,
        )
        newUser.save()
        # Cuando los datos se almacenen sera redireccionado al formulario de google.
    return redirect('api:campañas')

@login_required
def ListForms(request):
    FormID = request.POST.get('FormID')

    SpreadSheet = Formularios.objects.filter(pk=FormID)

    for val in SpreadSheet.values():
        url = val['urlRespuestas']
        GoogleData(url)

    data = {
        'message': 'Guardado con exito'
    }
    return JsonResponse(data)

@login_required
def InsertarFormulario(request):
    if request.is_ajax():

        Form = GoogleForms(request.POST)

        if Form.is_valid():
            Form.save()
            NombreFormulario = request.POST.get('nombreFormulario', None)
            NuevoFormulario = Formularios.objects.get(nombreFormulario=NombreFormulario)
            response = {
                'message': 'Registro con exito',
                'values': {
                    'pk': NuevoFormulario.pk,
                    'nombreFormulario': NuevoFormulario.nombreFormulario,
                    'urlFormulario': NuevoFormulario.urlFormulario,
                    'urlRespuestas': NuevoFormulario.urlRespuestas
                }
            }
            return JsonResponse(response)
        else:
            response = {
                'error': 'Campos Vacios'
            }
            return JsonResponse(response)

@login_required
def InhabilitarFormulario(request):
    FormID = request.POST.get('id')

    Form = Formularios.objects.get(pk=FormID)
    if Form.estado:
        Form.estado = False
        Form.save()
        response = {
            'message': 'Formulario Inhabilitado'
        }
    else:
        Form.estado = True
        Form.save()
        response = {
            'message': 'Formulario Habilitado'
        }
    return JsonResponse(response)

def Logout(request):
    logout(request)
    return redirect('api:inicio')


class FacebookUser(ListView):
    model = Resultados
    template_name = "FacebookUser.html"


class GoogleResults(ListView):
    model = Formularios
    template_name = "Resultados.html"


class Campañas(ListView):
    model = Formularios
    template_name = "campañas.html"


class Admin(ListView):
    model = Formularios
    context_object_name = 'Formularios'
    template_name = "admin.html"


# login
class Login(LoginView):
    template_name = 'login.html'


class Index(TemplateView):
    template_name = "index.html"
