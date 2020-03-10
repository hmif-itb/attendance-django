from rest_framework import generics
from .serializers import EventSerializer
from .models import Event

class EventView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    lookup_field = 'code'
    queryset = Event.objects.all()