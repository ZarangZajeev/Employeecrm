from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("v1/employees",views.EmployeesViewSetView,basename="employees")
router.register("v2/employees",views.EmployeesModelViewSetView,basename="employeemodel")

urlpatterns=[
    
] + router.urls