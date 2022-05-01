from Kitaplar.api.serializers import KitapSerializers, YorumSerializers
from rest_framework.generics import GenericAPIView, get_object_or_404


from Kitaplar.models import Kitap, Yorum
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from Kitaplar.api.permissions import IsAdminUserOrReadOnly, YorumSahibiOrReadOnly

from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from kitap_pazari.Kitaplar.api.pagination import SmallPagination


class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset =Kitap.objects.all()
    serializer_class = KitapSerializers
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallPagination


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Kitap.objects.all()
    serializer_class = KitapSerializers
    permission_classes = [IsAdminUserOrReadOnly]


class YorumCreateAPIView(generics.CreateAPIView):
    queryset =Yorum.objects.all()
    serializer_class = YorumSerializers
    permission_classes = [permissions.IsAdminUser]


    
    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk= kitap_pk)
        kullanici = self.request.user
        yorumlar = Yorum.objects.filter(kitap=kitap, yorum_sahibi = kullanici)
        serializer.save(kitap=kitap, yorum_sahibi = kullanici)
        if yorumlar.exists():
            raise ValidationError('Sadece bir yorum yapabilirsiniz.')

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Yorum.objects.all()
    serializer_class = YorumSerializers
    permission_classes = [YorumSahibiOrReadOnly]












# class KitapListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset =Kitap.objects.all()
#     serializer_class = KitapSerializers

#     #For Listing
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     #For Creating
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



