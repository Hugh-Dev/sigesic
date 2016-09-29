"""
Sistema Integral de Gestión para la Industria y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/wiki
"""
## @namespace unidad_economica.insumo_proveedor.forms
#
# Contiene las clases, atributos y métodos para los formularios a implementar en el módulo de insumos y proveedores
# @author Hugo Ramirez (hramirez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @date 14-09-2016
# @version 2.0

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, NumberInput, ChoiceField
)
from unidad_economica.sub_unidad_economica.models import SubUnidadEconomica
from .models import InsumoModel, ProveedorModel, InsumoProveedorModel
from base.fields import RifField
from base.models import *
from base.constant import UNIDAD_MEDIDA
from base.widgets import RifWidgetReadOnly, RifWidget
from base.functions import cargar_pais

CAPACIDAD_INSTALADA_MEDIDA = (('','Seleccione...'),("GR","Gramo"),("KG","Kilogramo"),("TN","Tonelada"))

class InsumoForm(forms.ModelForm):

    """!
    Clase para el formulario insumos proveedores

    @author Hugo Ramirez (hramirez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 14-09-2016
    @version 2.0.0
    """

    """ def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(InsumoForm, self).__init__(*args, **kwargs)
        self.fields['ubicacion_proveedor'].choices = cargar_pais()
        #Se carga una lista con todas las subunidades relacionadas al usuario
        lista = [('','Selecione...')]
        for l in SubUnidadEconomica.objects.filter(rif=self.user.username).values_list('id','nombre_sub'):
            lista.append(l)
        self.fields['subunidad'].choices = lista"""

    ## Listado de las subunidades disponibles
    subunidad = forms.ChoiceField(
        label=_("Sub-Unidad Economica"), widget=Select(attrs={
            'class': 'form-control input-md', 'required':'required',
            'data-toggle': 'tooltip','title': _("Seleccione Sub-Unidad Economica"), 'size': '50',
            'style': 'width: 250px;',
        }),
    )

    ## Nombre del insumo
    nombre_insumo = forms.CharField(
        label=_("Nombre del insumo"), widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'min-width: 0; width: auto; display: inline;',
            'data-toggle': 'tooltip','title': _("Indique el nombre del insumo"), 'size': '50',
            'style': 'width: 250px;',
        }), required = True,
    )

    ## Nombre del producto
    nombre_producto = forms.CharField(
        label=_("Nombre del Producto"), widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'min-width: 0; width: auto; display: inline;',
            'data-toggle': 'tooltip','title': _("Indique el nombre del producto"), 'size': '50',
            'style': 'width: 250px;',
        }), required = True,
    )

    ## Especificación técnica del producto
    especificacion_tecnica = forms.CharField(
        label=_("Especificación Técnica"), widget=Textarea(attrs={
            'class': 'form-control input-md','style': 'min-width: 0; width: auto; display: inline;',
            'data-toggle': 'tooltip','title': _("Indique la especificación técnica"), 'size': '50',
            'style': 'width: 250px;',
        }),required = False,
    )

    ## Marca del producto
    marca = forms.CharField(
        label=_("Marca"), widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'min-width: 0; width: auto; display: inline;',
            'data-toggle': 'tooltip','title': _("Indique la marca"), 'size': '50',
            'style': 'width: 250px;',
        }), required = False,
    )

    ## Relacion insumo-proveedor
    insumo_proveedor = forms.IntegerField(
        label=_("Relacion insumo-proveedor"), widget=NumberInput(attrs={
            'class': 'form-control input-md', 'style': 'min-width: o; width: auto; display: inline;',
            'data-toggle': 'tooltip', 'title': _("Indique la relacion insumo-proveedor"), 'size': '50',
            'style': 'width: 250px;',
        })
    )


    ## Numero de proveedores
    numero_proveedor = forms.IntegerField(
        label=_("Numero de proveedores"), widget=NumberInput(attrs={
            'class': 'form-control input-md', 'style': 'min-width: o; width: auto; display: inline;',
            'data-toggle': 'tooltip', 'title': _("Indique el numero de proveedores"), 'size': '50',
            'style': 'width: 250px;',
        })
    )



    class Meta:
        model = InsumoModel
        fields = '__all__'


class ProveedorForm(forms.ModelForm):

    """!
    Clase para el formulario insumos proveedores

    @author Hugo Ramirez (hramirez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 14-09-2016
    @version 2.0.0
    """

    ## Origen del insumo
    pais_origen = ChoiceField(
        label=_("País de origen: "), widget=Select(attrs={
            'class': 'form-control input-md', 'required':'required',
            'data-toggle': 'tooltip','title': _("Seleccione Sub-Unidad Economica"), 'size': '50',
            'style': 'width: 250px;',
        }),
        required=False
    )

    ## Listado de insumos
    insumo = forms.ChoiceField(
        label=_("Insumo"), widget=Select(attrs={
            'class': 'form-control input-md', 'required':'required',
            'data-toggle': 'tooltip','title': _("Seleccione el insumo correspondiente al proveedor"), 'size': '50',
            'style': 'width: 250px;',
        }),
    )

    ## R.I.F. del proveedor
    rif = RifField(required = False)
    rif.widget = RifWidgetReadOnly()

    ## Tipo de cambio
    tipo_cambio = forms.CharField(
        label=_("Tipo de cambio"), widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'min-width: 0; width: auto; display: inline;',
            'data-toggle': 'tooltip','title': _("Indique el tipo de cambio"), 'size': '50',
            'style': 'width: 250px;',
        }),required = False,
    )

    ## Cantidad comprada
    cantidad_comprada = forms.CharField(
        label=_("Cantidades Comprada"), widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'min-width: 0; width: auto; display: inline;',
            'data-toggle': 'tooltip','title': _("Indique la cantidad de Compra"), 'size': '50',
            'style': 'width: 250px;',
        }), required = False,
    )

    ## Unidad de medida
    unidad_de_medida = forms.ChoiceField(
        label=_("Unidad de Medida"), widget=Select(attrs={
            'class': 'form-control input-md','style': 'min-width: 0; width: auto; display: inline;',
            'data-toggle': 'tooltip','title': _("Seleccione la unidad de medida"), 'size': '50',
            'style': 'width: 250px;',
        }), choices = (('','Seleccione...'),)+UNIDAD_MEDIDA, required = False,
    )

    ## Nombre del insumo
    nombre_proveedor = forms.CharField(
        label=_("Nombre del proveedor"), widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'min-width: 0; width: auto; display: inline;',
            'data-toggle': 'tooltip','title': _("Indique el nombre del proveedor"), 'size': '50',
            'style': 'width: 250px;',
        }), required = True,
    )

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)

        self.fields['pais_origen'].choices = cargar_pais()

    class Meta:
        model = ProveedorModel
        fields = '__all__'


class InsumoProveedorForm(InsumoForm, ProveedorForm):

    class Meta:

        model = InsumoProveedorModel
        fields = '__all__'