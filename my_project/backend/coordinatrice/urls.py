from django.urls import path
from .views import UpdateMaitreWithApprentiView, UpdateTuteurWithApprentiView

urlpatterns = [
    path('update-maitre/<int:maitre_pk>/<int:apprenti_pk>/', UpdateMaitreWithApprentiView.as_view(), name='update-maitre'),
    path('update-tuteur/<int:tuteur_pk>/<int:apprenti_pk>/', UpdateTuteurWithApprentiView.as_view(), name='update-tuteur'),
    
]