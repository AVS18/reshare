from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('addProfile',views.addProfile,name="addProfile"),
    path('updateProfile',views.updateProfile,name="updateProfile"),
    path('addResource',views.addResource,name="addResource"),
    path('viewResource',views.viewResource,name="viewResource")
]