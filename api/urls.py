from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
from .views import GerarTabela

urlpatterns = [
    path('clientes', views.listar_clientes),
    path('usuarios', views.ClientesView.as_view()),
    path('usuario/<int:pk>', views.ClientesDetailView.as_view()),
    path('gerar-tabela', GerarTabela.as_view(), name='gerar_tabela'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


