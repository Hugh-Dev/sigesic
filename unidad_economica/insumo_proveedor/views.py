"""
Sistema Integral de Gestión para la Industria y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/wiki
"""
## @namespace unidad_economica.insumo_proveedores.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas del módulo de insumos y proveedores
# @author Hugo Ramirez (hramirez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @date 14-09-2016
# @version 2.0

import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
from django import forms
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from base.constant import CREATE_MESSAGE
from .models import InsumoProveedorModel
from .forms import InsumoProveedorForm
class InsumoProveedorCreate(SuccessMessageMixin,CreateView):
    """!
    Clase que registra los insumos y proveedores

    @author Hugo Ramirez (hramirez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 14-09-2016
    @version 2.0.0
    """
    model = InsumoProveedorModel
    form_class = InsumoProveedorForm
    template_name = "insumos.proveedores.template.html"
    success_url = reverse_lazy('insumos_proveedores')
    success_message = CREATE_MESSAGE