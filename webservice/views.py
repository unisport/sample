__author__ = 'azhukov'

from rest_framework import serializers, generics

from models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class ItemList(generics.ListCreateAPIView):
    model = Item
    serializer_class = ItemSerializer


class ItemListKids(ItemList):
    def get_queryset(self):
        return self.model.objects.filter(kids=True)


class ItemSingle(generics.RetrieveUpdateAPIView):
    model = Item
    serializer_class = ItemSerializer

    lookup_field = 'id'  # because of custom pk field
