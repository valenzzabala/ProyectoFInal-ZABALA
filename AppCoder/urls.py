from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos,name="cursos"),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar",views.buscar),
    path("elimina_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("editar_curso/<int:id>",views.editar , name="editar_curso"),
    
    path("alumnos", views.ver_alumnos, name="alumnos"),
    path("alta_alumno",views.alta_alumno, name="alta_alumno"),
    path("buscar_alumno",views.buscar_alumno,name="buscar_alumno"),
    path("busqueda",views.busqueda),
    path("eliminar_alumno/<int:id>", views.eliminar_alumno,name="eliminar_alumno"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    path('alumnos_curso/<int:curso_id>/', views.alumnos_curso, name='alumnos_curso'),
    
    path("ver_profes", views.ver_profes , name="profesores"),
    path("alta_profe", views.alta_profe, name="alta_profe"),
    path("editar_profe/<int:id>",views.editar_profe, name="editar_profe"),
    path("eliminar_profe/<int:id>",views.eliminar_profe , name="eliminar_profe"),
    path("buscar_profe", views.buscar_profe, name="buscar_profe"),
    path('resultado_busqueda_p.html', views.resultado_busqueda_p, name='resultado_busqueda_p'),
    path("profesores_curso/<int:curso_id>/", views.profesores_curso, name="profesores_curso"),


    path("login", views.login_request, name='login'),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil")

]