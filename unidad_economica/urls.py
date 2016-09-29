"""
Sistema Integral de Gestión para las Industrias y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/
"""
## @package unidad_economica.urls
#
# Urls del módulo unidad_economica
# @author Eveli Ramírez (eramirez at cenditel.gob.ve)
# @author <a href='​http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @date 04-05-2016
# @version 2.0
from __future__ import unicode_literals
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import UnidadEconomicaCreate

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"

urlpatterns = [
    url(r'^directorio/', include('unidad_economica.directorio.urls')),
    url(r'^informacion-general/registro/$', login_required(UnidadEconomicaCreate.as_view()), name="registro_ue"),
    url(r'^registro-mercantil/', include('unidad_economica.informacion_mercantil.urls')),
    url(r'^sub-unidad/', include('unidad_economica.sub_unidad_economica.urls')),
    url(r'^maquinaria-equipos/', include('unidad_economica.maquinaria_equipo.urls')),
    url(r'^bienes-prod-comer/', include('unidad_economica.bienes_prod_comer.urls')),
    url(r'^insumo-proveedor/', include('unidad_economica.insumo_proveedor.urls')),
    url(r'^servicios/', include('unidad_economica.servicios.urls')),
]
