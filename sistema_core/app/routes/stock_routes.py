from flask import Blueprint, render_template, request, redirect,  url_for, flash
from sqlalchemy import text
from app.db import engine 

stock = Blueprint('stock', __name__)


@stock.route('/stock/nuevo', methods=['GET', 'POST'])
def agregar_producto():
    with engine.connect() as conn:
        categorias = conn.execute(text("SELECT id, nombre FROM categorias")).fetchall()
        talles = conn.execute(text("SELECT id, nombre FROM talles ")).fetchall()
        proveedores = conn.execute(text("SELECT id, nombre FROM proveedores")).fetchall()
        sucursales = conn.execute(text("SELECT id, nombre FROM sucursales"))
        
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            descripcion = request.form.get('descripcion')
            precio_costo =  request.form.get('precio_costo')
            precio_venta = request.form.get('precio_venta')
            stock_actual = request.form.get('stock_actual')
            codigo_barras = request.form.get('codigo_barras')
            categoria_id = request.form.get('categoria_id') or None
            proveedor_id = request.form.get('proveedor_id') or None
            talle_id = request.form.get('talle_id') or None
            impuestos = request.form.get('impuestos') or 0
            sucursal_id = request.form.get('sucursal_id') or None #este deberia ser obligatorio
            
            query = text("""
                        INSERT INTO productos (
                            nombre, descripcion, precio_costo, precio_venta, stock_actual,
                            codigo_barras, categoria_id, proveedor_id, talle_id, impuestos, sucursal_id
                            ) VALUES (
                                :nombre, :descripcion, :precio_costo, :precio_venta, :stock_actual, 
                                :codigo_barras, :categoria_id, :proveedor_id, :talle_id, :impuestos, :sucursal_id
                            )""")


            conn.execute(query, {
                    "nombre":nombre, 
                    "descripcion": descripcion,
                    "precio_costo": precio_costo,
                    "precio_venta": precio_venta,
                    "stock_actual": stock_actual,
                    "codigo_barras": codigo_barras,
                    "categoria_id": categoria_id,
                    "proveedor_id": proveedor_id,
                    "talle_id": talle_id,
                    "impuestos": impuestos,
                    "sucursal_id":sucursal_id
                })
            conn.commit()
            flash("Producto agregado correctamente", "success")
            return redirect(url_for("stock.agregar_producto"))
        
    return render_template('stock/agregar_producto.html', categorias=categorias, talles=talles, proveedores=proveedores, sucursales=sucursales)
