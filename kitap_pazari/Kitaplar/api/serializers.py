from dataclasses import field
import imp
from rest_framework import serializers
from Kitaplar.models import Kitap, Yorum




class YorumSerializers(serializers.ModelSerializer):
    yorum_sahibi = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Yorum
        # fields = '__all__'
        exclude = ['kitap']

class KitapSerializers(serializers.ModelSerializer):
    
    yorumlar = YorumSerializers(many = True, read_only= True)
    class Meta:
        model = Kitap
        fields = '__all__'






