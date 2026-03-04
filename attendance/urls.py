from django.urls import path
from .views import AttendanceListCreateView, AttendanceRetrieveUpdateDeleteView

urlpatterns = [
    path("", AttendanceListCreateView.as_view(), name="attendance-list-create"),
    path("<int:pk>/", AttendanceRetrieveUpdateDeleteView.as_view(), name="attendance-detail"),
]