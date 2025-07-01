import nest_asyncio
nest_asyncio.apply()
from nicegui import ui

#!/usr/bin/env python3
from nicegui import ui

# Palabras disponibles y claves de frases
palabras = [
    'Decision Split',
    'Audience Splits',
    'Action Paths',
    'Experiment Paths',
    'Exit Criteria',
    'Re-eligibility',
    'Delivery Settings'
]

# Frases con espacios y respuestas correctas
frases = {
    'f1': ('Prueba rutas al azar y elige la mejor tras un periodo. {}', 'Experiment Paths'),
    'f2': ('Saca al usuario del Canvas si cumple una condición clave. {}', 'Exit Criteria'),
    'f3': ('Divide hasta en 8 rutas con base en atributos del usuario. {}', 'Audience Splits'),
    'f4': ('Divide rutas según eventos completados en un plazo. {}', 'Action Paths'),
    'f5': ('Define tras cuánto tiempo un usuario puede reentrar al Canvas. {}', 'Re-eligibility'),
    'f6': ('Divide en 2 rutas según un atributo verdadero o falso. {}', 'Decision Split'),
    'f7': ('Vuelve a validar si el usuario sigue en el segmento. {}', 'Delivery Settings'),
}

# Variables globales
asignaciones = {}
labels_por_frase = {}
palabra_arrastrada = None
botones_palabras = {}

# Título
ui.label('🚦 Business Decision Game').style('font-size: 34px; font-weight: bold; margin-bottom: 10px; color: #991b1b;')

# 📋 Instrucciones
with ui.card().classes('mt-6 p-4 bg-red-50'):
    ui.label('📋 Instrucciones:').style('font-weight: bold; margin-bottom: 10px; color: #991b1b')
    ui.label('1. Haz clic en una palabra para seleccionarla')
    ui.label('2. Haz clic en "Asignar aquí" junto a la frase donde quieres colocar la palabra')
    ui.label('3. Presiona "✅ Revisar respuestas" para ver si acertaste')
    ui.label('4. Las respuestas correctas se mostrarán en verde 💚')
    ui.label('5. ¡Completa todas las frases correctamente!')

# 💬 Mensaje de estado
status_label = ui.label('Selecciona una palabra y luego haz clic en una frase.').style(
    'font-size: 16px; color: #b91c1c; margin-bottom: 20px;'
)

# 💡 Función para seleccionar palabra
def seleccionar_palabra(palabra):
    global palabra_arrastrada
    palabra_arrastrada = palabra
    status_label.set_text(f'Palabra seleccionada: {palabra}. Ahora haz clic en una frase.')

def asignar_a_frase(clave):
    global palabra_arrastrada
    if palabra_arrastrada:
        asignaciones[clave] = palabra_arrastrada
        actualizar_frases()  # 👈 actualiza la frase en el momento
        status_label.set_text(f'¡{palabra_arrastrada} asignada a la frase!')
        if palabra_arrastrada in botones_palabras:
            botones_palabras[palabra_arrastrada].disable()
        palabra_arrastrada = None

def actualizar_frases():
    for clave, (plantilla, _) in frases.items():
        palabra = asignaciones.get(clave, '___')
        etiqueta = labels_por_frase[clave]
        etiqueta.set_text(plantilla.format(palabra))
        etiqueta.style('color: #4b5563; font-size: 18px')  # color neutro

# 🧠 Función para verificar las respuestas
def verificar_respuestas():
    correcto = 0
    for clave, (plantilla, respuesta) in frases.items():
        palabra = asignaciones.get(clave, '___')
        etiqueta = labels_por_frase[clave]
        etiqueta.set_text(plantilla.format(palabra))

        if palabra == '___':
            etiqueta.style('color: #4b5563; font-size: 18px')
        elif palabra == respuesta:
            etiqueta.style('color: green; font-weight: bold; font-size: 18px')
            correcto += 1
        else:
            etiqueta.style('color: red; font-weight: bold; font-size: 18px')

    if correcto == len(frases):
        mensaje_final.set_text('🎉 ¡Lo lograste! Todas las respuestas son correctas.')
    else:
        mensaje_final.set_text('🔍 Algunas respuestas aún no son correctas. ¡Sigue intentando!')

# 🎯 Palabras disponibles
ui.label('🎯 Palabras disponibles (haz clic para seleccionar):').style('font-weight: bold; margin-top: 20px;')

with ui.row().classes('bg-red-50 p-4 rounded shadow'):
    def crear_boton_palabra(palabra_texto):
        boton = ui.button(text=palabra_texto, on_click=lambda: seleccionar_palabra(palabra_texto)).style(
            'color: #b91c1c; font-weight: bold; font-size: 16px; background-color: #fff; '
            'padding: 8px 12px; margin: 4px; border-radius: 6px; border: 1px solid #fca5a5; '
            'box-shadow: 1px 1px 5px rgba(0,0,0,0.1);'
        )
        botones_palabras[palabra_texto] = boton

    for palabra in palabras:
        crear_boton_palabra(palabra)

# 📝 Frases
ui.label('📝 Frases (haz clic en el espacio en blanco):').style('font-weight: bold; margin-top: 20px; margin-bottom: 10px;')

with ui.column().classes('mt-4'):
    for clave, (plantilla, _) in frases.items():
        with ui.row().classes('items-center mb-4'):
            etiqueta = ui.label(plantilla.format('___')).style('font-size: 18px')
            labels_por_frase[clave] = etiqueta

            ui.button('Asignar aquí', on_click=lambda c=clave: asignar_a_frase(c)).classes(
                'ml-4 bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700 transition'
            )

# ✅ Botón para verificar
ui.button('✅ Revisar respuestas', on_click=verificar_respuestas).classes(
    'mt-4 bg-red-500 text-white rounded shadow-lg hover:bg-red-600 transition font-bold'
)

# 🔁 Botón para reiniciar
def reiniciar():
    global palabra_arrastrada
    palabra_arrastrada = None
    asignaciones.clear()
    for clave, (plantilla, _) in frases.items():
        labels_por_frase[clave].set_text(plantilla.format('___'))
        labels_por_frase[clave].style('color: #4b5563; font-size: 18px')
    for boton in botones_palabras.values():
        boton.enable()
    mensaje_final.set_text('')
    status_label.set_text('Selecciona una palabra y luego haz clic en una frase.')

ui.button('🔁 Reiniciar Juego', on_click=reiniciar).classes(
    'color: #b91c1c; font-weight: bold; font-size: 16px; background-color: #fff; padding: 8px 12px; margin: 4px; border-radius: 6px; box-shadow: 1px 1px 5px rgba(0,0,0,0.1);'
)

# Resultado final
mensaje_final = ui.label('').style('font-size: 20px; margin-top: 20px; color: #4b5563')


# 🖥️ Iniciar app
if __name__ == '__main__':
    print("🚀 Iniciando Business Decision Game...")
    print("🌐 El juego estará disponible en: http://localhost:8080")
    ui.run(
        title='Business Decision Game',
        port=8080,
        show=True,
        reload=False
    )
