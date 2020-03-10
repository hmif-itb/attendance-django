from django.urls import include, path
from .views import AttendanceView, RecordAttendanceView, DestroyAttendanceView

urlpatterns = [
    path('<int:code>/', AttendanceView.as_view(), name='attendance-list'),
    path('<int:code>/checkin/', RecordAttendanceView.as_view(), name='attendance-record'),
    path('<int:code>/<int:pk>/delete', DestroyAttendanceView.as_view(), name='attendance-delete')
]
