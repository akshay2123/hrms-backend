from rest_framework import generics, status
from rest_framework.response import Response
from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceListCreateView(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        employee_id = self.request.query_params.get("employee")
        if employee_id:
            return Attendance.objects.filter(employee_id=employee_id).order_by("-date")
        return Attendance.objects.all().order_by("-date")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Attendance marked successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class AttendanceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Attendance updated successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {"message": "Attendance deleted successfully."},
            status=status.HTTP_200_OK,
        )