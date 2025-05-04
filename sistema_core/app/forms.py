from wtforms import Form, StringField, DecimalField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange
from app.routes.form_helpers import get_form_data


class ProductoFormStock(Form):
    nombre = StringField('Nombre', validators=[InputRequired(message="El nombre es obligatorio."),
                                               Length(min=2, max=30)])
    descripcion = TextAreaField('Descripcion', validators=[Length(min=2, max=30)])
    codigo = StringField('Codigo de Barras', validators=[InputRequired(message="Se necesita agregar un codigo.")])
    precio_costo = IntegerField('Precio Costo', validators=[InputRequired(message="Se debe ingresar un valor.")])
    precio_venta = IntegerField('Precio Venta', validators=[InputRequired(message="Se debe ingresar un valor.")])
    impuestos = IntegerField('Impuestos')
    stock_actual = IntegerField('Stock Actual', validators=[InputRequired(message="Se debe agregar un valor.")])    
    
    # Obtengo data de las tablas para los campos Select
    data = get_form_data("categorias", 'talles', 'proveedores', 'sucursales')
    categorias_choices = [("0", "Seleccionar categoria")] + [(str(cat[0]), cat[1].title()) for cat in data.get("categorias", [])]
    proveedor_choices = [("0", "Seleccionar proveedor")] + [(str(prov[0]), prov[1]) for prov in data.get("proveedores", [])]
    talles_choices = [("None", "Seleccionar talle")] + [(str(talle[0]), talle[1]) for talle in data.get("talles", [])]
    sucursal_choices = [("None", "Seleccionar Sucursal")] + [(str(suc[0]), suc[1]) for suc in data.get("sucursales", [])]
    
    # Asignar las opciones al campo SelectField
    categoria = SelectField('Categoria', validators=[InputRequired(message="Se debe agregar una categoria")] ,choices=categorias_choices)
    proveedor = SelectField('Proveedor', choices=proveedor_choices)
    talle = SelectField('Talles', choices=talles_choices)
    sucursal = SelectField('Talles', choices=talles_choices)


form = ProductoFormStock()
