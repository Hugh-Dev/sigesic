"""
Sistema Integral de Gestión para las Industrias y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/
"""
## @package unidad_economica.models
#
# Clases, atributos y métodos para el modelo de datos de los bienes producidos y comercializados
# @author Rodrigo Boet (rboet at cenditel.gob.ve)
# @author <a href='​http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres 
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @date 13-07-2016
# @version 2.0

from django.db import models
from unidad_economica.sub_unidad_economica.models import SubUnidadEconomica
from base.models import CaevClase, Pais

class Producto(models.Model):
    """!
    Clase que gestiona los datos para el registro de los Productos en los Bienes Producidos y comercializados

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 13-07-2016
    @version 2.0
    """
    
    ## Nombre del Producto
    nombre_producto = models.CharField(max_length=45)
    
    ## Marca del Producto
    marca = models.CharField(max_length=45)
    
    ## Especificación Técnica del Producto
    especificacion_tecnica = models.CharField(max_length=45)
    
    ## Establece la relación con el código CAEV
    caev = models.ForeignKey(CaevClase)
    
    ## Establece la relación con la sub unidad económica
    subunidad = models.ForeignKey(SubUnidadEconomica)
   
class Produccion(models.Model):
    """!
    Clase que gestiona los datos para el registro de la Produccion en los Bienes Producidos y comercializados

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 13-07-2016
    @version 2.0
    """
    
    ## Cantidad Producida
    cantidad_produccion = models.IntegerField()
    
    ## Unidad de medida del producto
    unidad_de_medida = models.CharField(max_length=2)
    
    ## Año de la producción
    anho_produccion = models.IntegerField()
    
    ## Cantidad de clientes
    cantidad_clientes = models.IntegerField()
    
    ## Cantidad de insumos
    cantidad_insumos = models.IntegerField()
    
    ## Establece la relación con el producto
    producto = models.ForeignKey(Producto)

    
class Cliente(models.Model):
    """!
    Clase que gestiona los datos para el registro de los Clientes en los Bienes Producidos y comercializados

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 13-07-2016
    @version 2.0
    """
    
    ## Nombre del Cliente
    nombre = models.CharField(max_length=45)
    
    ## Rif del ciente
    rif = models.CharField(max_length=10)
    
    ## Establece la relación con el país
    pais = models.ForeignKey(Pais)
    
    ## Establece la relación con la producción
    produccion = models.ForeignKey(Produccion)
    
class ProduccionCliente(models.Model):
    """!
    Clase que gestiona los datos para el registro de la Produccion que se necesita del cliente en los Bienes Producidos y comercializados

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 13-07-2016
    @version 2.0
    """
    
    ## Cantidad Producida
    cantidad_produccion = models.IntegerField()
    
    ## Unidad de medida del producto
    unidad_de_medida = models.CharField(max_length=2)
    
    ## Precio de Venta por unidad
    precio_venta = models.DecimalField(max_digits=20,decimal_places=5)
    
    ## Tipo de cambio
    tipo_cambio = models.DecimalField(max_digits=20,decimal_places=5)
    
    ## Establece la relación con el producto
    cliente = models.ForeignKey(Cliente)
