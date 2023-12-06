import streamlit as st
from pymongo import MongoClient

# Use your MongoDB Atlas connection string here
mongo_uri = st.secrets["mongo_uri"]
# Create a MongoClient using the provided URI
client = MongoClient(mongo_uri)
# Specify the database and collection
db = client["ScalingUP"]
collection = db["Companies"]

def indice_solvencia(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        prefill_data = company_data.get("s7_metricas_efectivo", {})
        activo_circulante = prefill_data.get("activo_circulante", 0)
        pasivo_corto_plazo = prefill_data.get("pasivo_corto_plazo", 0)

        try:
            activo_circulante = float(activo_circulante)
            pasivo_corto_plazo = float(pasivo_corto_plazo)
            if pasivo_corto_plazo != 0:
                indice_solvencia_resultado = activo_circulante / pasivo_corto_plazo
                st.markdown(f'Indice de solvencia = :orange[{indice_solvencia_resultado}]')
                st.markdown(f'Por cada peso que debo tengo :orange[**${indice_solvencia_resultado}**] para hacer frente a mis deudas.')
            else:
                st.write("Pasivo a corto plazo es cero, no se puede calcular el índice de solvencia.")
        except ValueError:
            st.write("Los datos de activo circulante o pasivo a corto plazo no son numéricos.")

def dias_cartera(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        prefill_data = company_data.get("s7_metricas_efectivo", {})
        promedio_cuentas_por_cobrar_clientes = prefill_data.get("promedio_cuentas_por_cobrar_clientes", 0)
        ventas_netas = prefill_data.get("ventas_netas", 0)

        try:
            promedio_cuentas_por_cobrar_clientes = float(promedio_cuentas_por_cobrar_clientes)
            ventas_netas = float(ventas_netas)
            if ventas_netas !=0:
                dias_cartera_resultado = (promedio_cuentas_por_cobrar_clientes/ventas_netas)*365
                st.markdown(f'Dias Cartera = :orange[{dias_cartera_resultado}]')
                st.markdown(f'Entre la venta y la cobranza, transcurren :orange[**{dias_cartera_resultado}**] días.')
                st.markdown('Nota: Mientras más chico el número de días es mejor')
            else:
                st.write('Ventas Netas es cero, no se pueden calcular los días cartera')
        except ValueError:
            st.write('Los datos del promedio cuentas por cobrar a clientes o ventas netas no son numéricos')

def dias_proveedor(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        prefill_data = company_data.get("s7_metricas_efectivo", {})
        promedio_cuentas_por_pagar_proveedores = prefill_data.get("promedio_cuentas_por_pagar_proveedores", 0)
        compras_netas = prefill_data.get("compras_netas", 0)

        try:
            promedio_cuentas_por_pagar_proveedores = float(promedio_cuentas_por_pagar_proveedores)
            compras_netas = float(compras_netas)
            if compras_netas !=0:
                dias_proveedor_resultado = (promedio_cuentas_por_pagar_proveedores/compras_netas)*365
                st.markdown(f'Dias Proveedor = :orange[{dias_proveedor_resultado}]')
                st.markdown(f'Entre la compra de mercancía y su pago, transcurren :orange[**{dias_proveedor_resultado}**] días.')
                st.markdown('Nota: Mientras más grande el número de días es mejor. Sin embargo debe analizarse junto con apalancamiento')
            else:
                st.write('Compras Netas es cero, no se pueden calcular los días proveedor')
        except ValueError:
            st.write('Los datos del promedio cuentas por pagar a proveedores o compras netas no son numéricos')

def rentabilidad_ventas(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        prefill_data = company_data.get("s7_metricas_efectivo", {})
        utilidad_neta = prefill_data.get("utilidad_neta", 0)
        ventas_netas = prefill_data.get("ventas_netas", 0)

        try:
            utilidad_neta = float(utilidad_neta)
            ventas_netas = float(ventas_netas)
            if ventas_netas !=0:
                rentabilidad_ventas_resultado = (utilidad_neta/ventas_netas)*100
                st.markdown(f'Rentabilidad de las ventas = :orange[{rentabilidad_ventas_resultado}]')
                st.markdown(f'De cada \$100 que vendo tengo una utilidad después de impuestos y PTU de :orange[**\${rentabilidad_ventas_resultado}**]')
                st.markdown('Nota: Entre mayor utilidad mejor')
            else:
                st.write('Ventas Netas es cero, no se puede calcular la rentabilidad de las ventas')
        except ValueError:
            st.write('Los datos del utilidad neta o ventas netas no son numéricos')

def dias_inventario(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        prefill_data = company_data.get("s7_metricas_efectivo", {})
        promedio_inventarios = prefill_data.get("promedio_inventarios", 0)
        costo_ventas = prefill_data.get("costo_ventas", 0)

        try:
            promedio_inventarios = float(promedio_inventarios)
            costo_ventas = float(costo_ventas)
            if costo_ventas !=0:
                dias_inventario_resultado = (promedio_inventarios/costo_ventas)*365
                st.markdown(f'Días inventario = :orange[{dias_inventario_resultado}]')
                st.markdown(f'Entre la compra y la venta del inventario, transcurren :orange[**{dias_inventario_resultado}**] días')
                st.markdown('Nota: Mientras más chico el número de días es mejor')
            else:
                st.write('Costo de ventas es cero, no se pueden calcular los días inventario')
        except ValueError:
            st.write('Los datos del promedio de inventarios o costo de ventas no son numéricos')

def apalancamiento(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        prefill_data = company_data.get("s7_metricas_efectivo", {})
        pasivo_total = prefill_data.get("pasivo_total", 0)
        activo_total = prefill_data.get("activo_total", 0)

        try:
            pasivo_total = float(pasivo_total)
            activo_total = float(activo_total)
            if activo_total !=0:
                apalancamiento_resultado = (pasivo_total/activo_total)
                st.markdown(f'Apalancamiento = :orange[{apalancamiento_resultado}]')
                st.markdown(f'De cada \$1 que tenemos en activo :orange[**\${apalancamiento_resultado}**] se deben.')
                st.markdown('Nota: Número menor es mejor')
            else:
                st.write('Activo total es cero, no se puede calcular el apalancamiento')
        except ValueError:
            st.write('Los datos del pasivo total o activo total no son numéricos')

def utilidad_neta(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        prefill_data = company_data.get("s7_metricas_efectivo", {})
        ventas_netas = prefill_data.get("ventas_netas", 0)
        costo_ventas = prefill_data.get("costo_ventas", 0)
        gastos_totales = prefill_data.get("gastos_totales", 0)

        try:
            ventas_netas = float(ventas_netas)
            costo_ventas = float(costo_ventas)
            gastos_totales = float(gastos_totales)
            
            utilidad_neta_resultado = ventas_netas - costo_ventas - gastos_totales
            st.markdown(f'Utilidad neta = :orange[{utilidad_neta_resultado}]')
        except ValueError:
            st.write('Los datos del pasivo total o activo total no son numéricos')

