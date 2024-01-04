from django.shortcuts import render
from api.models import Employees
from api.serializers import EmployeeSerializer
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action

# Create your views here.

class EmployeesViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        serializers=EmployeeSerializer(qs,many=True)
        return Response(data=serializers.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        serializers=EmployeeSerializer(qs)
        return Response(data=serializers.data)
    
    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp_obj=Employees.objects.get(id=id)
        serializers=EmployeeSerializer(data=request.data,instance=emp_obj)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        else:
            return Response(data=serializers.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return Response(data={"message":"Item deleted"})
    
class EmployeesModelViewSetView(ModelViewSet):
    serializer_class=EmployeeSerializer
    model=Employees
    queryset=Employees.objects.all()

    def list(self, request, *args, **kwargs):
        qs=Employees.objects.all()
        if "department" in request.query_params:
            value=request.query_params.get("department")
            qs=qs.filter(department=value)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)

    @action(methods=["get"],detail=False)
    def departments(self,request,*args,**kwargs):
        qs=Employees.objects.all().values_list("department",flat=True).distinct()
        return Response(data=qs)