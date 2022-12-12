from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from .models import*
from django.contrib import messages
from django.contrib.auth.decorators import login_required #Proteger vista}
# from ipware import get_client_ip

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} ha sido creado')
    else:
        form = UserRegisterForm()
    context = {'form' : form}
    return render(request,"register.html", context)



#@login_required
def portafolio(request):
    projects = Project.objects.all()
    return render(request,"portafolio.html", {'projects':projects})


def addproject(request):
    if request.method =='POST':
        formproject = Project(request.POST)
        if formproject.is_valid():
            formproject.save()
            messages.success(request, f'Un nuevo proyecto ha sido agregado')
            
   
  
    return render(request,"addproject.html")




def eliminar(request, id):
    project = Project.objects.get(id=id)
    project.delete_at = timezone.now()
    project.save()
    return redirect("portafolio")



# class IndexView(TemplateView):
#     def get(self, request):
#         projects = Project.objects.all()
#         context = {
#             "projects":projects
#         }
#         ip, public_or_private = get_client_ip(request)
#         ips = Ip(ip=ip)
#         ips.save()
#         return render(request, "index.html", context)

