{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "989fdcd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "Usage:   \n",
      "  C:\\Users\\claud\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install [options] <requirement specifier> [package-index-options] ...\n",
      "  C:\\Users\\claud\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install [options] -r <requirements file> [package-index-options] ...\n",
      "  C:\\Users\\claud\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install [options] [-e] <vcs project url> ...\n",
      "  C:\\Users\\claud\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install [options] [-e] <local project path> ...\n",
      "  C:\\Users\\claud\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install [options] <archive url/path> ...\n",
      "\n",
      "no such option: -u\n"
     ]
    }
   ],
   "source": [
    "pip install nicegui -quit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2c593812",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nicegui in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (2.20.0)\n",
      "Requirement already satisfied: Pygments<3.0.0,>=2.15.1 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (2.19.1)\n",
      "Requirement already satisfied: aiofiles>=23.1.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (24.1.0)\n",
      "Requirement already satisfied: aiohttp>=3.10.2 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (3.12.13)\n",
      "Requirement already satisfied: certifi>=2024.07.04 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (2025.6.15)\n",
      "Requirement already satisfied: docutils>=0.19.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (0.21.2)\n",
      "Requirement already satisfied: fastapi>=0.109.1 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (0.115.14)\n",
      "Requirement already satisfied: h11>=0.16.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (0.16.0)\n",
      "Requirement already satisfied: httpx>=0.24.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (0.28.1)\n",
      "Requirement already satisfied: ifaddr>=0.2.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (0.2.0)\n",
      "Requirement already satisfied: itsdangerous<3.0.0,>=2.1.2 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (2.2.0)\n",
      "Requirement already satisfied: jinja2<4.0.0,>=3.1.6 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (3.1.6)\n",
      "Requirement already satisfied: markdown2!=2.4.11,>=2.4.7 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (2.5.3)\n",
      "Requirement already satisfied: orjson>=3.9.15 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (3.10.18)\n",
      "Requirement already satisfied: python-engineio>=4.12.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (4.12.2)\n",
      "Requirement already satisfied: python-multipart>=0.0.18 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (0.0.20)\n",
      "Requirement already satisfied: python-socketio>=5.10.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from python-socketio[asyncio-client]>=5.10.0->nicegui) (5.13.0)\n",
      "Requirement already satisfied: requests>=2.32.4 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (2.32.4)\n",
      "Requirement already satisfied: starlette>=0.45.3 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (0.46.2)\n",
      "Requirement already satisfied: typing-extensions>=4.0.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (4.14.0)\n",
      "Requirement already satisfied: urllib3!=2.0.0,!=2.0.1,!=2.0.2,!=2.0.3,!=2.0.4,!=2.0.5,!=2.0.6,!=2.0.7,!=2.1.0,!=2.2.0,!=2.2.1,>=1.26.18 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (2.5.0)\n",
      "Requirement already satisfied: uvicorn>=0.22.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from uvicorn[standard]>=0.22.0->nicegui) (0.35.0)\n",
      "Requirement already satisfied: vbuild>=0.8.2 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (0.8.2)\n",
      "Requirement already satisfied: watchfiles>=0.18.1 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nicegui) (1.1.0)\n",
      "Requirement already satisfied: aiohappyeyeballs>=2.5.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from aiohttp>=3.10.2->nicegui) (2.6.1)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from aiohttp>=3.10.2->nicegui) (1.3.2)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from aiohttp>=3.10.2->nicegui) (25.3.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from aiohttp>=3.10.2->nicegui) (1.7.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from aiohttp>=3.10.2->nicegui) (6.6.2)\n",
      "Requirement already satisfied: propcache>=0.2.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from aiohttp>=3.10.2->nicegui) (0.3.2)\n",
      "Requirement already satisfied: yarl<2.0,>=1.17.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from aiohttp>=3.10.2->nicegui) (1.20.1)\n",
      "Requirement already satisfied: pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from fastapi>=0.109.1->nicegui) (2.11.7)\n",
      "Requirement already satisfied: anyio in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from httpx>=0.24.0->nicegui) (4.9.0)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from httpx>=0.24.0->nicegui) (1.0.9)\n",
      "Requirement already satisfied: idna in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from httpx>=0.24.0->nicegui) (3.10)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from jinja2<4.0.0,>=3.1.6->nicegui) (3.0.2)\n",
      "Requirement already satisfied: simple-websocket>=0.10.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from python-engineio>=4.12.0->nicegui) (1.1.0)\n",
      "Requirement already satisfied: bidict>=0.21.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from python-socketio>=5.10.0->python-socketio[asyncio-client]>=5.10.0->nicegui) (0.23.1)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from requests>=2.32.4->nicegui) (3.4.2)\n",
      "Requirement already satisfied: click>=7.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from uvicorn>=0.22.0->uvicorn[standard]>=0.22.0->nicegui) (8.2.1)\n",
      "Requirement already satisfied: colorama>=0.4 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from uvicorn[standard]>=0.22.0->nicegui) (0.4.6)\n",
      "Requirement already satisfied: httptools>=0.6.3 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from uvicorn[standard]>=0.22.0->nicegui) (0.6.4)\n",
      "Requirement already satisfied: python-dotenv>=0.13 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from uvicorn[standard]>=0.22.0->nicegui) (1.1.1)\n",
      "Requirement already satisfied: pyyaml>=5.1 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from uvicorn[standard]>=0.22.0->nicegui) (6.0.2)\n",
      "Requirement already satisfied: websockets>=10.4 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from uvicorn[standard]>=0.22.0->nicegui) (15.0.1)\n",
      "Requirement already satisfied: pscript<0.8.0,>=0.7.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from vbuild>=0.8.2->nicegui) (0.7.7)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from anyio->httpx>=0.24.0->nicegui) (1.3.1)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi>=0.109.1->nicegui) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.33.2 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi>=0.109.1->nicegui) (2.33.2)\n",
      "Requirement already satisfied: typing-inspection>=0.4.0 in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi>=0.109.1->nicegui) (0.4.1)\n",
      "Requirement already satisfied: wsproto in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from simple-websocket>=0.10.0->python-engineio>=4.12.0->nicegui) (1.2.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.0 -> 25.1.1\n",
      "[notice] To update, run: C:\\Users\\claud\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install --upgrade nicegui"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4b5f6990",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: nicegui\n",
      "Version: 2.20.0\n",
      "Summary: Create web-based user interfaces with Python. The nice way.\n",
      "Home-page: \n",
      "Author: Zauberzeug GmbH\n",
      "Author-email: info@zauberzeug.com\n",
      "License: MIT\n",
      "Location: C:\\Users\\claud\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\n",
      "Requires: aiofiles, aiohttp, certifi, docutils, fastapi, h11, httpx, ifaddr, itsdangerous, jinja2, markdown2, orjson, Pygments, python-engineio, python-multipart, python-socketio, requests, starlette, typing-extensions, urllib3, uvicorn, vbuild, watchfiles\n",
      "Required-by: \n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip show nicegui"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d2da1da3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nest_asyncio in c:\\users\\claud\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (1.6.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.0 -> 25.1.1\n",
      "[notice] To update, run: C:\\Users\\claud\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install nest_asyncio\n",
    "import nest_asyncio\n",
    "nest_asyncio.apply()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e7ad4517",
   "metadata": {},
   "outputs": [],
   "source": [
    "from nicegui import ui"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0c70eeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "from nicegui import ui\n",
    "\n",
    "# Palabras disponibles y claves de frases\n",
    "palabras = [\n",
    "    'Decision Split',\n",
    "    'Audience Splits',\n",
    "    'Action Paths',\n",
    "    'Experiment Paths',\n",
    "    'Exit Criteria',\n",
    "    'Re-eligibility',\n",
    "    'Delivery Settings'\n",
    "]\n",
    "\n",
    "# Frases con espacios y respuestas correctas\n",
    "frases = {\n",
    "    'f1': ('Prueba rutas al azar y elige la mejor tras un periodo. {}', 'Experiment Paths'),\n",
    "    'f2': ('Saca al usuario del Canvas si cumple una condición clave. {}', 'Exit Criteria'),\n",
    "    'f3': ('Divide hasta en 8 rutas con base en atributos del usuario. {}', 'Audience Splits'),\n",
    "    'f4': ('Divide rutas según eventos completados en un plazo. {}', 'Action Paths'),\n",
    "    'f5': ('Define tras cuánto tiempo un usuario puede reentrar al Canvas. {}', 'Re-eligibility'),\n",
    "    'f6': ('Divide en 2 rutas según un atributo verdadero o falso. {}', 'Decision Split'),\n",
    "    'f7': ('Vuelve a validar si el usuario sigue en el segmento. {}', 'Delivery Settings'),\n",
    "}\n",
    "\n",
    "# Variables globales\n",
    "asignaciones = {}\n",
    "labels_por_frase = {}\n",
    "palabra_arrastrada = None\n",
    "botones_palabras = {}\n",
    "\n",
    "# Título\n",
    "ui.label('🚦 Business Decision Game').style('font-size: 34px; font-weight: bold; margin-bottom: 10px; color: #991b1b;')\n",
    "\n",
    "# 📋 Instrucciones\n",
    "with ui.card().classes('mt-6 p-4 bg-red-50'):\n",
    "    ui.label('📋 Instrucciones:').style('font-weight: bold; margin-bottom: 10px; color: #991b1b')\n",
    "    ui.label('1. Haz clic en una palabra para seleccionarla')\n",
    "    ui.label('2. Haz clic en \"Asignar aquí\" junto a la frase donde quieres colocar la palabra')\n",
    "    ui.label('3. Presiona \"✅ Revisar respuestas\" para ver si acertaste')\n",
    "    ui.label('4. Las respuestas correctas se mostrarán en verde 💚')\n",
    "    ui.label('5. ¡Completa todas las frases correctamente!')\n",
    "\n",
    "# 💬 Mensaje de estado\n",
    "status_label = ui.label('Selecciona una palabra y luego haz clic en una frase.').style(\n",
    "    'font-size: 16px; color: #b91c1c; margin-bottom: 20px;'\n",
    ")\n",
    "\n",
    "# 💡 Función para seleccionar palabra\n",
    "def seleccionar_palabra(palabra):\n",
    "    global palabra_arrastrada\n",
    "    palabra_arrastrada = palabra\n",
    "    status_label.set_text(f'Palabra seleccionada: {palabra}. Ahora haz clic en una frase.')\n",
    "\n",
    "def asignar_a_frase(clave):\n",
    "    global palabra_arrastrada\n",
    "    if palabra_arrastrada:\n",
    "        asignaciones[clave] = palabra_arrastrada\n",
    "        actualizar_frases()  # 👈 actualiza la frase en el momento\n",
    "        status_label.set_text(f'¡{palabra_arrastrada} asignada a la frase!')\n",
    "        if palabra_arrastrada in botones_palabras:\n",
    "            botones_palabras[palabra_arrastrada].disable()\n",
    "        palabra_arrastrada = None\n",
    "\n",
    "def actualizar_frases():\n",
    "    for clave, (plantilla, _) in frases.items():\n",
    "        palabra = asignaciones.get(clave, '___')\n",
    "        etiqueta = labels_por_frase[clave]\n",
    "        etiqueta.set_text(plantilla.format(palabra))\n",
    "        etiqueta.style('color: #4b5563; font-size: 18px')  # color neutro\n",
    "\n",
    "# 🧠 Función para verificar las respuestas\n",
    "def verificar_respuestas():\n",
    "    correcto = 0\n",
    "    for clave, (plantilla, respuesta) in frases.items():\n",
    "        palabra = asignaciones.get(clave, '___')\n",
    "        etiqueta = labels_por_frase[clave]\n",
    "        etiqueta.set_text(plantilla.format(palabra))\n",
    "\n",
    "        if palabra == '___':\n",
    "            etiqueta.style('color: #4b5563; font-size: 18px')\n",
    "        elif palabra == respuesta:\n",
    "            etiqueta.style('color: green; font-weight: bold; font-size: 18px')\n",
    "            correcto += 1\n",
    "        else:\n",
    "            etiqueta.style('color: red; font-weight: bold; font-size: 18px')\n",
    "\n",
    "    if correcto == len(frases):\n",
    "        mensaje_final.set_text('🎉 ¡Lo lograste! Todas las respuestas son correctas.')\n",
    "    else:\n",
    "        mensaje_final.set_text('🔍 Algunas respuestas aún no son correctas. ¡Sigue intentando!')\n",
    "\n",
    "# 🎯 Palabras disponibles\n",
    "ui.label('🎯 Palabras disponibles (haz clic para seleccionar):').style('font-weight: bold; margin-top: 20px;')\n",
    "\n",
    "with ui.row().classes('bg-red-50 p-4 rounded shadow'):\n",
    "    def crear_boton_palabra(palabra_texto):\n",
    "        boton = ui.button(text=palabra_texto, on_click=lambda: seleccionar_palabra(palabra_texto)).style(\n",
    "            'color: #b91c1c; font-weight: bold; font-size: 16px; background-color: #fff; '\n",
    "            'padding: 8px 12px; margin: 4px; border-radius: 6px; border: 1px solid #fca5a5; '\n",
    "            'box-shadow: 1px 1px 5px rgba(0,0,0,0.1);'\n",
    "        )\n",
    "        botones_palabras[palabra_texto] = boton\n",
    "\n",
    "    for palabra in palabras:\n",
    "        crear_boton_palabra(palabra)\n",
    "\n",
    "# 📝 Frases\n",
    "ui.label('📝 Frases (haz clic en el espacio en blanco):').style('font-weight: bold; margin-top: 20px; margin-bottom: 10px;')\n",
    "\n",
    "with ui.column().classes('mt-4'):\n",
    "    for clave, (plantilla, _) in frases.items():\n",
    "        with ui.row().classes('items-center mb-4'):\n",
    "            etiqueta = ui.label(plantilla.format('___')).style('font-size: 18px')\n",
    "            labels_por_frase[clave] = etiqueta\n",
    "\n",
    "            ui.button('Asignar aquí', on_click=lambda c=clave: asignar_a_frase(c)).classes(\n",
    "                'ml-4 bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700 transition'\n",
    "            )\n",
    "\n",
    "# ✅ Botón para verificar\n",
    "ui.button('✅ Revisar respuestas', on_click=verificar_respuestas).classes(\n",
    "    'mt-4 bg-red-500 text-white rounded shadow-lg hover:bg-red-600 transition font-bold'\n",
    ")\n",
    "\n",
    "# 🔁 Botón para reiniciar\n",
    "def reiniciar():\n",
    "    global palabra_arrastrada\n",
    "    palabra_arrastrada = None\n",
    "    asignaciones.clear()\n",
    "    for clave, (plantilla, _) in frases.items():\n",
    "        labels_por_frase[clave].set_text(plantilla.format('___'))\n",
    "        labels_por_frase[clave].style('color: #4b5563; font-size: 18px')\n",
    "    for boton in botones_palabras.values():\n",
    "        boton.enable()\n",
    "    mensaje_final.set_text('')\n",
    "    status_label.set_text('Selecciona una palabra y luego haz clic en una frase.')\n",
    "\n",
    "ui.button('🔁 Reiniciar Juego', on_click=reiniciar).classes(\n",
    "    'color: #b91c1c; font-weight: bold; font-size: 16px; background-color: #fff; padding: 8px 12px; margin: 4px; border-radius: 6px; box-shadow: 1px 1px 5px rgba(0,0,0,0.1);'\n",
    ")\n",
    "\n",
    "# Resultado final\n",
    "mensaje_final = ui.label('').style('font-size: 20px; margin-top: 20px; color: #4b5563')\n",
    "\n",
    "\n",
    "# 🖥️ Iniciar app\n",
    "if __name__ == '__main__':\n",
    "    print(\"🚀 Iniciando Business Decision Game...\")\n",
    "    print(\"🌐 El juego estará disponible en: http://localhost:8080\")\n",
    "    ui.run(\n",
    "        title='Business Decision Game',\n",
    "        port=8080,\n",
    "        show=True,\n",
    "        reload=False\n",
    "    )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
