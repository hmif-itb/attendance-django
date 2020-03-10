from django.urls import include, path
from .views import EventView

urlpatterns = [
    path('<int:code>/', EventView.as_view(), name='event-details')
]
