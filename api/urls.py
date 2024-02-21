from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("v1/employees",views.EmployeesViewSetView,basename="employees")
router.register("v2/employees",views.EmployeesModelViewSetView,basename="employeemodel")
router.register("v2/tasks",views.TaskView,basename="tasks")

urlpatterns=[
    path("v2/token/",ObtainAuthToken.as_view()),
] + router.urls