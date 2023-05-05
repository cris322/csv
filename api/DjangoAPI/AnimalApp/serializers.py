from rest_framework import serializers
from AnimalApp.models import perritos,accesorios

class perritosSerializer(serializers.ModelSerializer):
    class Meta:
        model=perritos
        fields=('IdPerro','nombrePerro','razaPerro','edadPerro')

class accesoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model=accesorios
        fields=('IdAccesorio','nombreAccesorio','cantidadAccesorio','precioAccesorio')        