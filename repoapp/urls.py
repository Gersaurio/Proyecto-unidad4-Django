from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("",views.index, name="index"),
    path("register", views.register, name="register"),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path("portafolio/usuario",views.portafolio, name='portafolio_usuario'),
    path("portafolio/",views.portafolio, name='portafolio'),
    path("portafolio/usuario/logout",LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("portafolio/addproject",views.addproject,name='addjproject')

    
    

 

]