from django.urls import path

from Facebook_API import views

urlpatterns = [

    path(
        route='login/',
        view=views.Login.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.Logout,
        name='logout'
    ),
    path(
        route='inicio/',
        view=views.Index.as_view(),
        name='inicio'
    ),
    path(
        route='home/',
        view=views.userDetails,
        name='home'
    ),
    path(
        route='getForms/',
        view=views.ListForms,
        name='getForms'
    ),
    path(
        route='admin/',
        view=views.Admin.as_view(),
        name='admin'
    ), path(
        route='csvdata/',
        view=views.GoogleData,
        name='csvdata'
    ),
    path(
        route='newForm/',
        view=views.InsertarFormulario,
        name='newForm'
    ),
    path(
        route='campañas/',
        view=views.Campañas.as_view(),
        name='campañas'
    ),
    path(
        route='resultados/',
        view=views.GoogleResults.as_view(),
        name='resultados'
    ),
    path(
        route='facebookUsers/',
        view=views.FacebookUser.as_view(),
        name='facebookUsers'
    ),
    path(
        route='inhabilitarFormulario/',
        view=views.InhabilitarFormulario,
        name='inhabilitarFormulario'
    ),

]
