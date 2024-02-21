from rest_framework import serializers
from api.models import Employees,Tasks


class TaskSerializers(serializers.ModelSerializer):
    employee=serializers.StringRelatedField()
    class Meta:
        model=Tasks
        fields="__all__"
        read_only_fields=["id","assigned_date","employee"]

class EmployeeSerializer(serializers.ModelSerializer):
    tasks=TaskSerializers(read_only=True,many=True)
    class Meta:
        model=Employees
        fields="__all__"
        read_only_fields=["id"]
