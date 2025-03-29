import streamlit as st

def convertir_attrs(attrs):
    # Extraemos las condiciones del atributo 'invisible'
    condiciones = attrs.strip("{'invisible' : }").strip("[]").split("),(")
    
    # Inicializamos la lista de condiciones
    result = []
    
    # Determinamos el operador, si es el primer elemento y contiene '|', se usa OR
    operador = 'and'
    
    # Si el primer elemento contiene '|', el operador entre las condiciones será 'or'
    if '|' in condiciones[0]:
        operador = 'or'
        condiciones[0] = condiciones[0].replace("|", "")  # Limpiamos el '|' para evitar que se duplique
    
    # Convertir cada condición a la forma que se quiere
    for cond in condiciones:
        campos = cond.strip('()').split(", ")
        field = campos[0]
        operator = campos[1]
        values = campos[2].strip('[]').replace("'", "")  # Eliminar los ' de las listas
        
        # Si el valor de 'values' no es una lista (solo un valor), lo convertimos
        if ',' not in values:
            condition = f"{field} {operator} ({values})"
        else:
            condition = f"{field} {operator} ({values})"
        
        result.append(condition)

    # Unimos las condiciones con el operador adecuado (AND/OR)
    return f" {operador} ".join(result)


# Título y descripción
st.title("Conversor de condiciones")
st.write("Introduce el valor de `attrs` en el siguiente cuadro de texto, y se convertirá en el formato adecuado.")

# Cuadro de texto para que el usuario ingrese el `attrs`
attrs_input = st.text_area("Introduce los valores de attrs", "{'invisible' : [('move_type','not in',['out_invoice','in_invoice']),('state','=','posted')]}")
    
# Botón para ejecutar la conversión
if st.button("Convertir"):
    # Ejecutamos la conversión
    resultado = convertir_attrs(attrs_input)
    st.write("Resultado:")
    st.code(f'invisible = "{resultado}"')
