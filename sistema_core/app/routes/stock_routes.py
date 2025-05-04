from flask import Blueprint, render_template, request, redirect,  url_for, flash
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from app.db import engine 
from app.routes.form_helpers import get_form_data
from app.forms import ProductoFormStock

stock = Blueprint('stock', __name__)


@stock.route('/stock/nuevo', methods=['GET', 'POST'])
def agregar_producto():
    
    # instancio una clase de formulario producto
    form = ProductoFormStock()
    
    #print("Form Data Cargada", form_data)
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        precio_costo =  request.form.get('precio_costo')
        precio_venta = request.form.get('precio_venta')
        stock_actual = request.form.get('stock_actual')
        codigo_barras = request.form.get('codigo_barras')
        categoria = request.form.get('categoria_id') or None
        proveedor_id = request.form.get('proveedor_id') or None
        talle_id = request.form.get('talle_id') or None
        impuestos = request.form.get('impuestos') or 0
        # Revisar que ya no hay mas columna sucursal en la tabla productos. Este insert debe ir a producto y stock.
        sucursal_id = request.form.get('sucursal_id') or None #este deberia ser obligatorio
        
        
        query = text("""
                     INSERT INTO productos (
                         nombre, descripcion, precio_costo, precio_venta, stock_actual,
                         codigo_barras, categoria_id, proveedor_id, talle_id, impuestos
                        ) VALUES (
                             :nombre, :descripcion, :precio_costo, :precio_venta, :stock_actual, 
                             :codigo_barras, :categoria, :proveedor_id, :talle_id, :impuestos
                        )""")
        try:
            with engine.connect() as conn:
                conn.execute(query, {
                    "nombre":nombre, 
                    "descripcion": descripcion,
                    "precio_costo": precio_costo,
                    "precio_venta": precio_venta,
                    "stock_actual": stock_actual,
                    "codigo_barras": codigo_barras,
                    "categoria_id": categoria,
                    "proveedor_id": proveedor_id,
                    "talle_id": talle_id,
                    "impuestos": impuestos
                })
                conn.commit()
                flash("Producto agregado correctamente", "success")
                return redirect(url_for("stock.agregar_producto"))
            
        except IntegrityError as e:
            if 'unique constraint' in str(e).lower() or 'duplicate key' in str(e).lower():
                flash("El código de barras ya está en uso. Intente con otro.", "danger")
            else:
                flash("Ocurrió un error al guardar el producto.", "danger")
                return redirect(url_for("stock.agregar_producto"))
        
    return render_template('stock/agregar_producto.html', form=form) # paso el form, como contexto
