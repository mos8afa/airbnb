from .serializers import PropertySerializer
from .models import Property

from rest_framework.generics import ListAPIView , RetrieveAPIView

class PropertyListApi(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyDetailApi(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


