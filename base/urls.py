"""
Sistema Integral de Gestión para la Industria y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/wiki
"""
## @namespace base.urls
#
# Contiene las urls del módulo base
# @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
from __future__ import unicode_literals
from django.conf.urls import url, patterns

from .ajax import get_data_rif, validar_rif_seniat

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"


urlpatterns = [
    url(r'^inicio/$', 'base.views.inicio', name='inicio'),
]


## URLs de peticiones AJAX
urlpatterns += [
    url(r'^ajax/get_data_rif/?$', get_data_rif, name='get_data_rif'),
    url(r'^ajax/validar_rif_seniat/?$', validar_rif_seniat, name='validar_rif_seniat'),
]