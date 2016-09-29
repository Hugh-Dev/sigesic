from django.db import models
from base.models import Pais
# Create your models here.


class InsumoModel(models.Model):
    """!
    Clase que gestiona los datos para el registro de los insumos y proveedores del modulo insumo-proveedor

    @author Hugo Ramirez (hramirez at cenditel.gob.ve)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 14-09-2016
    @version 2.0
    """

    ## Nombre del Producto
    nombre_producto = models.CharField(max_length=45)

    ## Nombre del Insumo
    nombre_insumo = models.CharField(max_length=45)

    ## Especificación Técnica del Insumo
    especificacion_tecnica = models.CharField(max_length=45)

    ## Marca del Insumo
    marca = models.CharField(max_length=45)

    ## Numero de Proveedores
    numero_proveedor = models.IntegerField()

    ## Establece la Relación con el Código Arancelario
    #codigo_arancelario = models.ForeignKey()

class ProveedorModel(models.Model):

    ## Establece pais de origen del proveedor
    pais_origen = models.ForeignKey(Pais)


class InsumoProveedorModel(models.Model):

    ## Establece la relacion del insumo con proveedor
    proveedor = models.ForeignKey(InsumoModel)

    ## Instancia la clase InsumoModel
    insumo = InsumoModel()

    ## Instancia la clase ProveedorModel
    proveedor = ProveedorModel()


