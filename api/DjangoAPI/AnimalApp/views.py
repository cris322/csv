from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AnimalApp.models import perritos,accesorios
from AnimalApp.serializers import perritosSerializer,accesoriosSerializer 
# Create your views here.
@csrf_exempt
def AnimalApi(request,id=0):
    if request.method =='GET':
        perro=perritos.objects.all()
        perros_Serializer=perritosSerializer(perro,many=True)
        return JsonResponse(perros_Serializer.data,safe=False)
    elif request.method =='POST':
        perros_data=JSONParser().parse(request)
        perros_Serializer=perritosSerializer(data=perros_data)
        if perros_Serializer.is_valid():
            perros_Serializer.save()
            return JsonResponse('se agrego correctamente',safe=False)
        return JsonResponse("fallo al agregar",safe=False)
    elif request.method=='PUT':
        perros_data=JSONParser().parse(request)
        perro=perritos.objects.get(IdPerro=perros_data['IdPerro'])
        perros_Serializer=perritosSerializer(perro,data=perros_data)
        if perros_Serializer.is_valid():
            perros_Serializer.save()
            return JsonResponse("actualizado correctamente",safe=False)
        return JsonResponse("error al actualizar",safe=False)
    elif request.method=='DELETE':
        perros_data=JSONParser().parse(request)
        perro=perritos.objects.get(IdPerro=perros_data['IdPerro'])

        if  perro!=id:
            perro.delete()
            return JsonResponse("se elimino correctamente",safe=False)
        return JsonResponse("error al eliminar",safe=False)
    
@csrf_exempt
def AccesorioApi(request,id=0):
    if  request.method =='GET':
        Accesorio=accesorios.objects.all()
        accesorio_Serializer=accesoriosSerializer(Accesorio,many=True)
        return JsonResponse(accesorio_Serializer.data,safe=False)
    elif request.method =='POST':
        accesorios_data=JSONParser().parse(request)
        Accesorio_Serializer=accesoriosSerializer(data=accesorios_data)
        if Accesorio_Serializer.is_valid():
            Accesorio_Serializer.save()
            return JsonResponse('se agrego correctamente',safe=False)
        return JsonResponse("fallo al agregar",safe=False)
    elif request.method=='PUT':
        accesorios_data=JSONParser().parse(request)
        Accesorio=accesorios.objects.get(IdAccesorio=accesorios_data['IdAccesorio'])
        accesorios_Serializer=accesoriosSerializer(Accesorio,data=accesorios_data)
        if accesorios_Serializer.is_valid():
            accesorios_Serializer.save()
            return JsonResponse("actualizado correctamente",safe=False)
        return JsonResponse("error al actualizar",safe=False)
    elif request.method=='DELETE':
        accesorios_data=JSONParser().parse(request)
        Accesorio=accesorios.objects.get(IdAccesorio=accesorios_data['IdAccesorio'])
        if  Accesorio!=id:
            Accesorio.delete()
            return JsonResponse("se elimino correctamente",safe=False)
        return JsonResponse("error al eliminar",safe=False)
    
