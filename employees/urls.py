from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView

urlpatterns = [
    path("", EmployeeListCreateView.as_view(), name="employee-list-create"),
    path("<int:pk>/", EmployeeRetrieveUpdateDeleteView.as_view(), name="employee-detail"),
]