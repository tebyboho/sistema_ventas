from wtforms import Form, StringField, DecimalField, IntegerField, SelectField 
from wtforms.validators import InputRequired, Length, NumberRange
from routes.form_helpers import get_form_data


class ProductoFormStock(Form):
    nombre = StringField('Nombre', validators=[InputRequired(), Length(min=2, max=50)])
    
    data = get_form_data("categorias", 'talles', 'proveedores', 'sucursales')
    
    categorias_choices = [("0", "Seleccionar categoria")] + [(str(cat[0]), cat[1]) for cat in data.get("categorias", [])]
    
    # Asignar las opciones al campo SelectField
    categoria = SelectField('Categoria', choices=categorias_choices)


form = ProductoFormStock()

print(form.categoria.choices)