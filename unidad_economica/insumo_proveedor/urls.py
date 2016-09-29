"""
Sistema Integral de Gestión para las Industrias y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/
"""
## @package insumo_proveedor.urls
#
# Urls del módulo maquinaria_equipos
# @author Hugo Ramírez (hramirez at cenditel.gob.ve)
# @author <a href='​http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @date 14-09-2016
# @version 2.0
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import InsumoProveedorCreate

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"


urlpatterns = [
    url(r'^registro$', login_required(InsumoProveedorCreate.as_view()) ,name="insumos_proveedores"),
    #url(r'^registro_$', login_required(.as_view()) ,name="bienes_registro_create"),
    #url(r'^registro_$', login_required(.as_view()) ,name="cliente_registro_create"),
]
