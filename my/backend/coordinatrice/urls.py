from django.urls import path
from .views import UpdateMaitreWithApprentiView, UpdateTuteurWithApprentiView

urlpatterns = [
    path('update-maitre/<int:pk>/<int:pk>/', UpdateMaitreWithApprentiView.as_view(), name='update-maitre'),
    path('update-tuteur/<int:pk>/<int:pk>/', UpdateTuteurWithApprentiView.as_view(), name='update-tuteur'),
    
]