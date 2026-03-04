from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_email(self, value):
        instance = self.instance

        if Employee.objects.filter(email=value).exclude(id=instance.id if instance else None).exists():
            raise serializers.ValidationError("Email already exists.")

        return value

    def validate_employee_id(self, value):
        instance = self.instance

        if Employee.objects.filter(employee_id=value).exclude(id=instance.id if instance else None).exists():
            raise serializers.ValidationError("Employee ID already exists.")

        return value