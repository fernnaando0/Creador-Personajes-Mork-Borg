import threading
import tkinter as tk
from tkinter import (
    messagebox,
    scrolledtext,
)

import character  # Tu módulo de lógica

# ============================================================
# MODO NARRATIVO - Configuración de la API de Groq
# Obtén tu API key gratuita en: https://console.groq.com/keys
# ============================================================
GROQ_API_KEY = "TU_API_KEY_AQUI"
GROQ_MODEL = "llama3-8b-8192"
# ============================================================


def generate_lore(char):
    """Llama a la API de Groq para generar el transfondo narrativo del personaje."""
    import urllib.request
    import json

    if GROQ_API_KEY == "TU_API_KEY_AQUI":
        return "[ERROR] Añade tu API key de Groq en la variable GROQ_API_KEY de interface.py"

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": char.get_lore_prompt()}
        ],
        "max_tokens": 300,
        "temperature": 0.9,
    }

    req = urllib.request.Request(
        "https://api.groq.com/openai/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"].strip()
    except urllib.error.HTTPError as e:
        return f"[ERROR HTTP {e.code}] {e.reason}. Comprueba tu API key."
    except Exception as e:
        return f"[ERROR] No se pudo conectar con la API: {e}"


def _actualizar_texto(texto_personaje):
    """Actualiza el área de texto (siempre llamado desde el hilo principal)."""
    lineas = texto_personaje.split("\n")
    nueva_altura = len(lineas) + 1
    anchura_maxima = max(len(linea) for linea in lineas)
    nueva_anchura = max(anchura_maxima + 4, 50)

    text_area.config(width=nueva_anchura, height=nueva_altura)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.INSERT, texto_personaje)


def _generar_con_lore(p):
    """Hilo secundario: llama a la IA y actualiza la UI cuando termina."""
    lore = generate_lore(p)
    p.set_lore(lore)
    texto_final = p.get_lore_str()
    # Volvemos al hilo principal para actualizar la UI
    app.after(0, lambda: _actualizar_texto(texto_final))
    app.after(0, lambda: btn_generate.config(state=tk.NORMAL, text="INVOCAR"))


def generar_personaje():
    # 1. Generar lógica del personaje
    p = character.Character()
    modo = var_modo.get()

    if modo == 1:
        p.roll_simple()
        texto_personaje = p.get_simple_str()
        _actualizar_texto(texto_personaje)

    elif modo == 2:
        p.roll_stats()
        p.set_derived_stats()
        p.set_starting_equipment()
        p.set_flavor()
        texto_personaje = str(p)
        _actualizar_texto(texto_personaje)

    else:
        # Modo 3: Narrativo
        p.roll_stats()
        p.set_derived_stats()
        p.set_starting_equipment()
        p.set_flavor()

        # Mostramos los datos base mientras esperamos la IA
        texto_base = str(p) + (
            "\n========================================\n"
            " TRANSFONDO (GENERADO POR IA)\n"
            "----------------------------------------\n"
            "  [ Invocando al oráculo... ]\n"
            "========================================"
        )
        _actualizar_texto(texto_base)

        # Deshabilitamos el botón mientras la IA trabaja
        btn_generate.config(state=tk.DISABLED, text="CONSULTANDO...")

        # Lanzamos la llamada a la API en un hilo separado para no bloquear la UI
        hilo = threading.Thread(target=_generar_con_lore, args=(p,), daemon=True)
        hilo.start()


def guardar_archivo():
    contenido = text_area.get("1.0", tk.END).strip()
    if not contenido:
        messagebox.showwarning("Cuidado", "Primero genera un personaje.")
        return

    try:
        with open("personaje_guardado.txt", "w", encoding="utf-8") as f:
            f.write(contenido)
        messagebox.showinfo("Éxito", "Escoria guardada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")


# --- CONFIGURACIÓN DE LA VENTANA ---
app = tk.Tk()
app.title("Generador MÖRK BORG")
app.configure(bg="#1a1a1a")

# 1. ETIQUETA DE TÍTULO
title_label = tk.Label(
    app,
    text=" SCUM GENERATOR ",
    font=("Old English Text MT", 24, "bold"),
    bg="#1a1a1a",
    fg="#F1C40F",
)
title_label.pack(pady=10)

# --- NUEVO: SELECTOR DE MODO ---
mode_frame = tk.Frame(app, bg="#1a1a1a")
mode_frame.pack(pady=5)

var_modo = tk.IntVar(value=1)  # 1 por defecto (Simple)

tk.Radiobutton(
    mode_frame,
    text="CARNE DE CAÑÓN (SIMPLE)",
    variable=var_modo,
    value=1,
    bg="#1a1a1a",
    fg="#aaaaaa",
    selectcolor="#000000",
    activebackground="#1a1a1a",
    font=("Consolas", 10),
).pack(side=tk.LEFT, padx=10)

tk.Radiobutton(
    mode_frame,
    text="ESCORIA DETALLADA (EXTENSO)",
    variable=var_modo,
    value=2,
    bg="#1a1a1a",
    fg="#aaaaaa",
    selectcolor="#000000",
    activebackground="#1a1a1a",
    font=("Consolas", 10),
).pack(side=tk.LEFT, padx=10)

tk.Radiobutton(
    mode_frame,
    text="ALMA MALDITA (NARRATIVO+IA)",
    variable=var_modo,
    value=3,
    bg="#1a1a1a",
    fg="#F1C40F",
    selectcolor="#000000",
    activebackground="#1a1a1a",
    font=("Consolas", 10),
).pack(side=tk.LEFT, padx=10)
# ------------------------------

# 2. CAJA DE TEXTO
text_area = scrolledtext.ScrolledText(
    app, width=60, height=15, font=("Consolas", 10), bg="#000000", fg="#C0C0C0"
)
text_area.configure(wrap=tk.NONE)
text_area.pack(padx=20, pady=10)

# 3. BOTONES
button_frame = tk.Frame(app, bg="#1a1a1a")
button_frame.pack(pady=20)

btn_generate = tk.Button(
    button_frame,
    text="INVOCAR",
    font=("Chiller", 14, "bold"),
    bg="#800000",
    fg="white",
    width=15,
    command=generar_personaje,
)
btn_generate.pack(side=tk.LEFT, padx=20)

btn_save = tk.Button(
    button_frame,
    text="GUARDAR",
    font=("Chiller", 14, "bold"),
    bg="#404040",
    fg="white",
    width=15,
    command=guardar_archivo,
)
btn_save.pack(side=tk.LEFT, padx=20)

app.mainloop()