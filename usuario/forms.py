"""
Sistema Integral de Gestión para la Industria y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/wiki
"""
## @namespace usuario.forms
#
# Contiene las clases, atributos y métodos para los formularios a implementar en el módulo de usuario
# @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
from __future__ import unicode_literals, absolute_import

import logging

from base.constant import (
    TIPO_PERSONA_LIST,
    SHORT_TIPO_PERSONA)
from base.fields import RifField, CedulaField
from base.functions import verificar_rif
from base.classes import Seniat
from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.contrib.auth.models import User
from django.forms import (
    ModelForm, TextInput, EmailInput, CharField, EmailField, PasswordInput,
    Select)
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .models import UserProfile

"""!
Contiene el objeto que registra la vitacora de eventos del módulo usuario.
(configuración en el settings de la aplicación)
"""
logger = logging.getLogger("usuario")

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"


@python_2_unicode_compatible
class AutenticarForm(forms.Form):
    """!
    Clase que muestra el formulario de registro de usuarios

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 21-04-2016
    @version 2.0.0
    """

    ## R.I.F. de la Unidad Económica que identifica al usuario en el sistema
    rif = RifField()

    ## Contraseña del usuario
    clave = CharField(
        label=_("Contraseña"), max_length=30, widget=PasswordInput(attrs={
            'class': 'form-control input-sm', 'placeholder': _("contraseña de acceso"), 'data-toggle': 'tooltip',
            'title': _("Indique la contraseña de acceso al sistema"), 'size': '28'
        })
    )

    ## Campo de validación de captcha
    captcha = CaptchaField(
        label=_("Captcha"), widget=CaptchaTextInput(attrs={
            'class': 'form-control input-sm', 'placeholder': _("texto de la imagen"),
            'style': 'min-width: 0; width: auto; display: inline;', 'data-toggle': 'tooltip',
            'title': _("Indique el texto de la imagen")
        })
    )

    def clean_rif(self):
        """!
        Método que permite validar el campo de rif

        @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 27-04-2016
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve un mensaje de error en caso de que el rif no sea válido o no se encuentre registrado en el
                sistema, en caso contrario devuelve el valor actual del campo
        """
        rif = self.cleaned_data['rif']

        if not verificar_rif(rif):
            raise forms.ValidationError(_("El RIF es inválido"))
        elif not User.objects.filter(username=rif):
            raise forms.ValidationError(_("Usuario no registrado"))

        return

    def clean_clave(self):
        """!
        Método que permite validar el campo de contraseña

        @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 27-04-2016
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve un mensaje de error en caso de que la contraseña sea incorrecta, en caso contrario devuelve
                el valor actual del campo
        """
        clave = self.cleaned_data['clave']
        rif = "%s%s%s" % (self.data['rif_0'], self.data['rif_1'], self.data['rif_2'])

        if User.objects.filter(username=rif) and User.objects.get(username=rif).check_password(clave):
            raise forms.ValidationError(_("Contraseña incorrecta"))

        return clave


@python_2_unicode_compatible
class RegistroForm(ModelForm):
    """!
    Clase que muestra el formulario de registro de usuarios

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 21-04-2016
    @version 2.0.0
    """

    ## R.I.F. de la Unidad Económica que identifica al usuario en el sistema
    rif = RifField()

    ## Nombre de la Unidad Economica
    nombre_ue = CharField(
        label=_("Nombre de la Unidad Económica: "),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip',
                'title': _("Nombre de la Unidad Económica a registrar"), 'readonly': 'readonly', 'size': '50'
            }
        ), required=False
    )

    ## Cédula de Identidad del usuario
    cedula = CedulaField()

    ## Cargo del usuario dentro de la Unidad Económica
    cargo = CharField(
        label=_("Cargo que ocupa en la U.E.:"),
        max_length=175,
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Cargo en la Empresa"), 'data-rule-required': 'true',
                'data-toggle': 'tooltip', 'title': _("Indique el cargo del usuario en la empresa"), 'size': '50'
            }
        )
    )

    ## Nombre del usuario
    nombre = CharField(
        label=_("Nombre"),
        max_length=30,
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Nombres del usuario"), 'data-rule-required': 'true',
                'data-toggle': 'tooltip', 'title': _("Indique el Nombre"), 'size': '50'
            }
        )
    )

    ## Apellido del usuario
    apellido = CharField(
        label=_("Apellido"),
        max_length=30,
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Apellidos del usuario"), 'data-rule-required': 'true',
                'data-toggle': 'tooltip', 'title': _("Indique el Apellido"), 'size': '50'
            }
        )
    )

    ## Número telefónico de contacto con el usuario
    telefono = CharField(
        label=_("Teléfono"),
        max_length=15,
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Número telefónico"), 'data-rule-required': 'true',
                'data-toggle': 'tooltip', 'title': _("Indique el número telefónico de contacto con el usuario"),
                'size': '12'
            }
        )
    )

    ## Correo electrónico de contacto con el usuario
    correo = EmailField(
        label=_("Correo Electrónico"),
        max_length=15,
        widget=EmailInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Correo de contacto"), 'data-rule-required': 'true',
                'data-toggle': 'tooltip', 'size': '50',
                'title': _("Indique el correo electrónico de contacto con el usuario. "
                           "No se permiten correos de hotmail")
            }
        )
    )

    ## Contraseña del usuario
    contrasenha = CharField(
        label=_("Contraseña"),
        max_length=128,
        widget=PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Contraseña de acceso"),
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'size': '50',
                'title': _("Indique una contraseña de aceso al sistema"), 'onkeyup': 'passwordStrength(this.value)'
            }
        )
    )

    ## Confirmación de contraseña de acceso
    verificar_contrasenha = CharField(
        label=_("Verificar Contraseña"),
        max_length=128,
        widget=PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Contraseña de acceso"),
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'size': '50',
                'title': _("Indique nuevamente la contraseña de aceso al sistema")
            }
        )
    )

    ## Campo para la validación del captcha
    captcha = CaptchaField(
        label=_(u"Captcha"), widget=CaptchaTextInput(attrs={
            'class': 'form-control input-sm', 'placeholder': _("Texto de la imagen"),
            'style': 'min-width: 0; width: auto; display: inline;', 'data-toggle': 'tooltip',
            'title': _(u"Indique el texto de la imagen")
        })
    )

    class Meta:
        model = UserProfile
        exclude = ['fecha_modpass',]


    def clean_rif(self):
        """!
        Método que permite validar el campo de rif

        @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 27-04-2016
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve un mensaje de error en caso de que el rif no sea válido o no se encuentre registrado en el
                SENIAT, en caso contrario devuelve el valor actual del campo
        """
        rif = self.cleaned_data['rif']

        if rif[0] not in TIPO_PERSONA_LIST:
            raise forms.ValidationError(_("Tipo de RIF incorrecto"))
        elif not verificar_rif(rif):
            raise forms.ValidationError(_("El RIF es inválido"))
        elif User.objects.filter(username=rif):
            raise forms.ValidationError(_("El RIF ya se encuentra registrado"))
        elif not rif[1:].isdigit():
            raise  forms.ValidationError(_("El RIF no es correcto"))
        else:
            validar_rif = Seniat()
            rif_valido = validar_rif.buscar_rif(rif)
            if not rif_valido:
                raise forms.ValidationError(_("El RIF no existe"))

        return rif

    def clean_cedula(self):
        pass

    def clean_cargo(self):
        pass

    def clean_nombre(self):
        pass

    def clean_apellido(self):
        pass

    def clean_correo(self):
        pass

    def clean_telefono(self):
        pass

    def clean_contrasenha(self):
        pass

    def clean_verificar_contrasenha(self):
        pass
