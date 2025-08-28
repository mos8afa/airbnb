from .serializers import PropertySerializer
from .models import Property
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView , RetrieveAPIView

class PropertyListApi(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

class PropertyDetailApi(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]


