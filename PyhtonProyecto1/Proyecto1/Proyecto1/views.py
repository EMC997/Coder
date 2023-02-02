from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
    return HttpResponse('Hola Django - Coder')

def segunda_vista(request):
    return HttpResponse('<br>Bienvenidos</br> Ya entendimos esto, es muy facil')

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoTexto = f'hoy es: <br> {dia}'
    return HttpResponse (documentoTexto)

def miNombre(self, nombre):
    documentoTexto= f'mi nombre es: <br> {nombre}'
    return HttpResponse(documentoTexto)

def probandoTemplate(self):
    mihtml = open ('C:/Users/enzoc/OneDrive/Escritorio/python/PyhtonProyecto1/Proyecto1/Proyecto1/Plantillas/template1.html')
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)