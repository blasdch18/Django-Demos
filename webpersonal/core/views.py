from django.shortcuts import render, HttpResponse


html_base = """
<h1> Web Personal </h1>
<ul>
    <li> <a href="/"> Portada </a></li>
    <li> <a href="/about-me"> Acerca de  </a></li>
    <li> <a href="/portafolio"> Portafolio  </a></li>
    <li> <a href="/contactos"> Contactos </a></li>
</ul>    
"""

# Create your views here.

def home(request):
    return render(request, "core/home.html")
    
def about(request):
    return render(request, "core/acerca.html")               

def portafolio(request):
    return render(request, "core/portafolio.html")

def contactos(request):
    return render(request, "core/contactos.html")