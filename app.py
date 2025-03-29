import streamlit as st

def convertir_attrs(attrs):
    # Extraemos las condiciones del atributo 'invisible'
    condiciones = attrs.strip("{'invisible' : }").strip("[]").split("),(")
    
    # Inicializamos la lista de condiciones
    result = []
    
    # Comprobamos si hay un '|' entre las condiciones
    if '|' in condiciones[0]:  # Si hay un '|' en alguna de las condiciones
        operador = '|'
    else:
        operador = 'and'
    
    # Convertir cada condición a la forma que se quiere
    for cond in condiciones:
        campos = cond.strip('()').split(", ")
        field = campos[0]
        operator = campos[1]
        values = campos[2].strip('[]')
        
        # Creamos la cadena para la condición
        if operator == "not in":
            condition = f"{field} not in ({values})"
        else:
            condition = f"{field} {operator} ({values})"
        
        result.append(condition)

    # Unimos las condiciones con el operador adecuado
    return f"{operador} ".join(result)


# Título y descripción
st.title("Conversor de condiciones")
st.write("Introduce el valor de `attrs` en el siguiente cuadro de texto, y se convertirá en el formato adecuado.")

# Cuadro de texto para que el usuario ingrese el `attrs`
attrs_input = st.text_area("Introduce los valores de attrs", "{'invisible' : [('type', 'not in', ['sale','purchase','general'])]}")

# Botón para ejecutar la conversión
if st.button("Convertir"):
    # Ejecutamos la conversión
    resultado = convertir_attrs(attrs_input)
    st.write("Resultado:")
    st.code(resultado)
