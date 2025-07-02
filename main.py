import nest_asyncio
nest_asyncio.apply()
import os
from nicegui import app, ui

app.add_static_files('/static', os.path.join(os.path.dirname(__file__), 'static'))

# Palabras disponibles y claves de frases
palabras = [
    'Decision Split',
    'Audience Paths',
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
    'f3': ('Divide hasta en 8 rutas con base en atributos del usuario. {}', 'Audience Paths'),
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
popup_resultados = None
popup_instrucciones = None

# CSS responsivo
ui.add_head_html('''
<style>
    /* Responsive Design */
    @media (max-width: 768px) {
        .mobile-title {
            font-size: 24px !important;
        }
        .mobile-subtitle {
            font-size: 18px !important;
        }
        .mobile-button {
            font-size: 14px !important;
            padding: 6px 10px !important;
        }
        .mobile-text {
            font-size: 14px !important;
        }
        .mobile-frase {
            font-size: 16px !important;
        }
        .mobile-logo {
            height: 25px !important;
        }
    }
    
    @media (min-width: 769px) and (max-width: 1024px) {
        .tablet-title {
            font-size: 36px !important;
        }
        .tablet-logo {
            height: 35px !important;
        }
    }
    
    @media (min-width: 1025px) {
        .desktop-title {
            font-size: 45px !important;
        }
        .desktop-logo {
            height: 40px !important;
        }
    }
    
    /* Logo responsive */
    .logo-img {
        height: 40px;
        width: auto;
        object-fit: contain;
        flex-shrink: 0;
    }
</style>
<script>
function handleLogoError(img) {
    img.style.display = 'none';
    const fallback = img.nextElementSibling;
    if (fallback) fallback.style.display = 'inline';
}
</script>
''')

# Función para mostrar popup de instrucciones
def mostrar_popup_instrucciones():
    global popup_instrucciones
    
    # Cerrar popup anterior si existe
    if popup_instrucciones:
        popup_instrucciones.close()
    
    with ui.dialog().props('persistent') as popup:
        popup_instrucciones = popup
        
        with ui.card().classes('p-6').style('min-width: 90vw; max-width: 500px; position: relative;'):
            # Botón X en esquina superior derecha
            ui.button('×', on_click=lambda: cerrar_popup_instrucciones()).style(
                'position: absolute; '
                'top: 10px; '
                'right: 10px; '
                'background-color: #ef4444 !important; '
                'color: white !important; '
                'border-radius: 50%; '
                'width: 30px; '
                'height: 30px; '
                'font-size: 18px; '
                'font-weight: bold; '
                'border: none !important; '
                'cursor: pointer; '
                'display: flex; '
                'align-items: center; '
                'justify-content: center; '
                'padding: 0;'
            )
            
            ui.label('📋 Instrucciones del Juego').style('font-weight: bold; margin-bottom: 15px; color: #991b1b; font-size: 20px;')
            ui.label('1. Haz clic en una palabra para seleccionarla').style('margin-bottom: 8px; font-size: 16px;')
            ui.label('2. Haz clic en "Asignar aquí" junto a la frase donde quieres colocar la palabra').style('margin-bottom: 8px; font-size: 16px;')
            ui.label('3. Presiona "✅ Revisar respuestas" para ver si acertaste').style('margin-bottom: 8px; font-size: 16px;')
            ui.label('4. Las respuestas correctas se mostrarán en verde 💚').style('margin-bottom: 8px; font-size: 16px;')
            ui.label('5. ¡Completa todas las frases correctamente!').style('margin-bottom: 15px; font-size: 16px;')
            
            ui.label('💡 Tip: Si hay respuestas correctas e incorrectas, al corregir solo se borrarán las incorrectas.').style(
                'font-style: italic; color: #6b7280; font-size: 14px; background-color: #f3f4f6; padding: 10px; border-radius: 6px;'
            )
    
    popup.open()

def cerrar_popup_instrucciones():
    global popup_instrucciones
    if popup_instrucciones:
        popup_instrucciones.close()
        popup_instrucciones = None

# Función para mostrar popup de resultados
def mostrar_popup_resultados(correcto, total):
    global popup_resultados
    
    # Cerrar popup anterior si existe
    if popup_resultados:
        popup_resultados.close()
    
    with ui.dialog().props('persistent') as popup:
        popup_resultados = popup
        
        with ui.card().classes('p-6 text-center').style('min-width: 90vw; max-width: 400px; position: relative;'):
            # Botón X en esquina superior derecha
            ui.button('×', on_click=lambda: cerrar_popup()).style(
                'position: absolute; '
                'top: 10px; '
                'right: 10px; '
                'background-color: #ef4444 !important; '
                'color: white !important; '
                'border-radius: 50%; '
                'width: 30px; '
                'height: 30px; '
                'font-size: 18px; '
                'font-weight: bold; '
                'border: none !important; '
                'cursor: pointer; '
                'display: flex; '
                'align-items: center; '
                'justify-content: center; '
                'padding: 0;'
            )
            
            if correcto == total:
                ui.label('🎉 ¡PERFECTO!').style('font-size: 24px; font-weight: bold; color: #22c55e; margin-bottom: 10px;')
                ui.label('¡Todas las respuestas son correctas!').style('font-size: 18px; color: #22c55e; margin-bottom: 20px;')
            else:
                ui.label('📊 Resultados').style('font-size: 24px; font-weight: bold; color: #dc2626; margin-bottom: 10px;')
                ui.label(f'✅ Correctas: {correcto}').style('font-size: 18px; color: #22c55e; margin-bottom: 5px;')
                ui.label(f'❌ Incorrectas: {total - correcto}').style('font-size: 18px; color: #ef4444; margin-bottom: 20px;')
                ui.label('¡Sigue intentando!').style('font-size: 16px; color: #6b7280; margin-bottom: 20px;')
            
            # Botón de reintentar
            if correcto == total:
                ui.button('🎉 Jugar de nuevo', on_click=lambda: reintentar_desde_popup()).style(
                    'background-color: #22c55e !important; '
                    'color: white !important; '
                    'font-weight: bold; '
                    'padding: 10px 20px; '
                    'border-radius: 8px; '
                    'border: 2px solid #22c55e !important; '
                    'cursor: pointer; '
                    'font-size: 16px; '
                    'margin-top: 10px;'
                )
            else:
                ui.button('🔄 Corregir errores', on_click=lambda: reintentar_desde_popup()).style(
                    'background-color: #dc2626 !important; '
                    'color: white !important; '
                    'font-weight: bold; '
                    'padding: 10px 20px; '
                    'border-radius: 8px; '
                    'border: 2px solid #dc2626 !important; '
                    'cursor: pointer; '
                    'font-size: 16px; '
                    'margin-top: 10px;'
                )
    
    popup.open()

def cerrar_popup():
    global popup_resultados
    if popup_resultados:
        popup_resultados.close()
        popup_resultados = None

def reintentar_desde_popup():
    cerrar_popup()
    # Verificar si hay alguna respuesta incorrecta
    hay_incorrectas = False
    correctas_count = 0
    
    for clave, (_, respuesta_correcta) in frases.items():
        palabra_asignada = asignaciones.get(clave, '___')
        if palabra_asignada != '___':
            if palabra_asignada == respuesta_correcta:
                correctas_count += 1
            else:
                hay_incorrectas = True
    
    if hay_incorrectas and correctas_count > 0:
        # Solo limpiar las incorrectas, mantener las correctas
        reiniciar_solo_incorrectas()
    else:
        # Si todas están bien o todas están mal, reiniciar completamente
        reiniciar()

def reiniciar_solo_incorrectas():
    global palabra_arrastrada
    palabra_arrastrada = None
    
    palabras_a_reactivar = []
    
    for clave, (plantilla, respuesta_correcta) in frases.items():
        palabra_asignada = asignaciones.get(clave, '___')
        
        if palabra_asignada != '___' and palabra_asignada != respuesta_correcta:
            # Esta asignación es incorrecta, la removemos
            palabras_a_reactivar.append(palabra_asignada)
            del asignaciones[clave]
            
            # Actualizar la frase para mostrar ___
            labels_por_frase[clave].set_text(plantilla.format('___'))
            labels_por_frase[clave].style('color: #000000; font-size: 18px; font-weight: normal;')
        elif palabra_asignada == respuesta_correcta:
            # Esta asignación es correcta, mantenerla con estilo de éxito
            labels_por_frase[clave].set_text(plantilla.format(palabra_asignada))
            labels_por_frase[clave].style('color: #22c55e; font-size: 18px; font-weight: bold;')
    
    # Reactivar botones de palabras que fueron removidas
    for palabra in palabras_a_reactivar:
        if palabra in botones_palabras:
            botones_palabras[palabra].enable()
            botones_palabras[palabra].style(
                'background-color: #dc2626 !important; '
                'color: white !important; '
                'font-weight: bold; '
                'font-size: 16px; '
                'padding: 8px 12px; '
                'margin: 4px; '
                'border-radius: 6px; '
                'border: 2px solid #dc2626 !important; '
                'box-shadow: 0 2px 4px rgba(0,0,0,0.1); '
                'cursor: pointer; '
                'transition: all 0.2s ease;'
            )
    
    mensaje_final.set_text('')
    status_label.set_text('✅ Se mantuvieron las respuestas correctas. Corrige las incorrectas.')

# Contenedor principal responsivo
with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
    
    # Título con logo responsivo
    with ui.row().classes('w-full justify-center items-center mb-6').style('gap: 15px; flex-wrap: wrap;'):
        # Intentar cargar el logo con manejo de errores
        logo_container = ui.element('div').style('display: flex; align-items: center;')
        
        # Agregar JavaScript para el manejo de errores del logo
        ui.add_head_html('''
        <script>
        function handleLogoError(img) {
            img.style.display = 'none';
            const fallback = img.nextElementSibling;
            if (fallback) fallback.style.display = 'inline';
        }
        </script>
        ''')
        
        with logo_container:
            ui.html('''
                <img src="/static/logo-davivienda.png" 
                     alt="Davivienda Logo" 
                     class="logo-img mobile-logo tablet-logo desktop-logo"
                     onerror="handleLogoError(this)"
                     style="height: 40px; width: auto; object-fit: contain;">
                <span style="display: none; font-size: 30px;">🏦</span>
            ''')
        
        ui.label('Canvas - Juego Minders').classes('mobile-title tablet-title desktop-title').style(
            'font-size: 45px; font-weight: bold; color: #dc2626; text-align: center; flex-shrink: 0;'
        )

    # Botón de instrucciones
    with ui.row().classes('w-full justify-center mb-6'):
        ui.button('📋 Ver Instrucciones', on_click=mostrar_popup_instrucciones).classes('mobile-button').style(
            'background-color: #dc2626 !important; '
            'color: white !important; '
            'font-weight: bold; '
            'padding: 8px 16px; '
            'border-radius: 8px; '
            'border: 2px solid #dc2626 !important; '
            'cursor: pointer; '
            'font-size: 14px; '
            'transition: all 0.2s ease;'
        )

    # Mensaje de estado
    status_label = ui.label('Selecciona una palabra y luego haz clic en una frase.').classes('mobile-text').style(
        'font-size: 16px; color: #b91c1c; margin-bottom: 20px; text-align: center;'
    )

    # Funciones (sin cambios)
    def seleccionar_palabra(palabra):
        global palabra_arrastrada
        palabra_arrastrada = palabra
        status_label.set_text(f'Palabra seleccionada: {palabra}. Ahora haz clic en una frase.')

    def asignar_a_frase(clave):
        global palabra_arrastrada
        if palabra_arrastrada:
            # Si había una palabra asignada anteriormente a esta frase, reactivar su botón
            if clave in asignaciones:
                palabra_anterior = asignaciones[clave]
                if palabra_anterior in botones_palabras:
                    botones_palabras[palabra_anterior].enable()
                    # Restaurar estilo del botón reactivado
                    botones_palabras[palabra_anterior].style(
                        'background-color: #dc2626 !important; '
                        'color: white !important; '
                        'font-weight: bold; '
                        'font-size: 16px; '
                        'padding: 8px 12px; '
                        'margin: 4px; '
                        'border-radius: 6px; '
                        'border: 2px solid #dc2626 !important; '
                        'box-shadow: 0 2px 4px rgba(0,0,0,0.1); '
                        'cursor: pointer; '
                        'transition: all 0.2s ease;'
                    )
            
            # Asignar la nueva palabra
            asignaciones[clave] = palabra_arrastrada
            actualizar_frases()
            status_label.set_text(f'¡{palabra_arrastrada} asignada a la frase!')
            
            # Desactivar el botón de la palabra recién asignada
            if palabra_arrastrada in botones_palabras:
                botones_palabras[palabra_arrastrada].disable()
            
            palabra_arrastrada = None

    def actualizar_frases():
        for clave, (plantilla, _) in frases.items():
            palabra = asignaciones.get(clave, '___')
            etiqueta = labels_por_frase[clave]
            etiqueta.set_text(plantilla.format(palabra))
            
            # Si hay palabra asignada, ponerla en negrita; si no, peso normal
            if palabra != '___':
                etiqueta.style('color: #000000; font-size: 18px; font-weight: bold;')
            else:
                etiqueta.style('color: #000000; font-size: 18px; font-weight: normal;')

    def verificar_respuestas():
        correcto = 0
        total = len(frases)
        
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

        # Mostrar popup con resultados
        mostrar_popup_resultados(correcto, total)

    # Palabras disponibles con diseño responsivo
    ui.label('🎯 Palabras disponibles (haz clic para seleccionar):').classes('mobile-subtitle').style(
        'font-weight: bold; margin-top: 20px; font-size: 18px; text-align: center;'
    )

    with ui.row().classes('bg-red-50 p-4 rounded shadow justify-center flex-wrap gap-2'):
        def crear_boton_palabra(palabra_texto):
            boton = ui.button(text=palabra_texto, on_click=lambda: seleccionar_palabra(palabra_texto)).classes('mobile-button').style(
                'background-color: #dc2626 !important; '
                'color: white !important; '
                'font-weight: bold; '
                'font-size: 16px; '
                'padding: 8px 12px; '
                'margin: 4px; '
                'border-radius: 6px; '
                'border: 2px solid #dc2626 !important; '
                'box-shadow: 0 2px 4px rgba(0,0,0,0.1); '
                'cursor: pointer; '
                'transition: all 0.2s ease;'
            )
            botones_palabras[palabra_texto] = boton

        for palabra in palabras:
            crear_boton_palabra(palabra)

    # Frases con diseño responsivo
    ui.label('📝 Frases (haz clic en "Asignar aquí"):').classes('mobile-subtitle').style(
        'font-weight: bold; margin-top: 20px; margin-bottom: 15px; font-size: 18px; text-align: center;'
    )

    with ui.column().classes('mt-4 w-full'):
        for clave, (plantilla, _) in frases.items():
            with ui.row().classes('items-center mb-4 flex-wrap gap-2'):
                # Frase en un contenedor flex
                with ui.element('div').classes('flex-1 min-w-0'):
                    etiqueta = ui.label(plantilla.format('___')).classes('mobile-frase').style(
                        'font-size: 18px; color: #000000; font-weight: normal; line-height: 1.4; word-wrap: break-word;'
                    )
                    labels_por_frase[clave] = etiqueta

                # Botón en contenedor flex-shrink-0
                ui.button('Asignar aquí', on_click=lambda c=clave: asignar_a_frase(c)).classes('mobile-button').style(
                    'background-color: #dc2626 !important; '
                    'color: white !important; '
                    'font-weight: bold; '
                    'padding: 6px 12px; '
                    'border-radius: 6px; '
                    'border: 2px solid #dc2626 !important; '
                    'cursor: pointer; '
                    'transition: all 0.2s ease; '
                    'white-space: nowrap; '
                    'flex-shrink: 0;'
                )

    # Botones de acción con diseño responsivo
    with ui.row().classes('w-full justify-center gap-4 mt-6 flex-wrap'):
        ui.button('✅ Revisar respuestas', on_click=verificar_respuestas).classes('mobile-button').style(
            'background-color: #dc2626 !important; '
            'color: white !important; '
            'font-weight: bold; '
            'padding: 10px 16px; '
            'border-radius: 8px; '
            'border: 2px solid #dc2626 !important; '
            'cursor: pointer; '
            'transition: all 0.2s ease; '
            'font-size: 16px;'
        )

        # Botón reiniciar
        def reiniciar():
            global palabra_arrastrada, popup_resultados, popup_instrucciones
            palabra_arrastrada = None
            asignaciones.clear()
            
            # Cerrar popups si están abiertos
            if popup_resultados:
                popup_resultados.close()
                popup_resultados = None
            if popup_instrucciones:
                popup_instrucciones.close()
                popup_instrucciones = None
            
            for clave, (plantilla, _) in frases.items():
                labels_por_frase[clave].set_text(plantilla.format('___'))
                labels_por_frase[clave].style('color: #000000; font-size: 18px; font-weight: normal;')
            for boton in botones_palabras.values():
                boton.enable()
                # Restaurar estilo original del botón
                boton.style(
                    'background-color: #dc2626 !important; '
                    'color: white !important; '
                    'font-weight: bold; '
                    'font-size: 16px; '
                    'padding: 8px 12px; '
                    'margin: 4px; '
                    'border-radius: 6px; '
                    'border: 2px solid #dc2626 !important; '
                    'box-shadow: 0 2px 4px rgba(0,0,0,0.1); '
                    'cursor: pointer; '
                    'transition: all 0.2s ease;'
                )
            mensaje_final.set_text('')
            status_label.set_text('Selecciona una palabra y luego haz clic en una frase.')

        ui.button('🔁 Reiniciar Juego', on_click=reiniciar).classes('mobile-button').style(
            'background-color: #dc2626 !important; '
            'color: white !important; '
            'font-weight: bold; '
            'padding: 10px 16px; '
            'border-radius: 8px; '
            'border: 2px solid #dc2626 !important; '
            'cursor: pointer; '
            'transition: all 0.2s ease; '
            'font-size: 16px;'
        )

    # Resultado
    mensaje_final = ui.label('').style('font-size: 20px; margin-top: 20px; color: #4b5563; text-align: center;')

# Run App
if __name__ == '__main__':
    print("🚀 Iniciando Business Decision Game...")
    print("🌐 El juego estará disponible en: http://localhost:8080")
    print("📂 Buscando logo en: static/logo-davivienda.png")
    print("💡 Asegúrate de que el archivo logo-davivienda.png esté en la carpeta 'static'")
    ui.run(
        title='Business Decision Game - Davivienda',
        port=8080,
        show=True,
        reload=False
    )
