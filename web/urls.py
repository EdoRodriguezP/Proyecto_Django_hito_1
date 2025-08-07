from django.urls import path
from .views import home, premium, ProductoDetalle

urlpatterns = [
    path('', home, name='home'),
    path('about/', premium, name='premium'),
    path('producto/<int:pk>/', ProductoDetalle.as_view(), name='detalle'),
]
