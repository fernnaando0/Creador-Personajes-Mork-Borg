import tkinter as tk
from tkinter import (
    messagebox,
    scrolledtext,
)

import character  # Tu módulo de lógica


def generar_personaje():
    # 1. Generar lógica del personaje
    p = character.Character()

    # Leemos el valor de la opción seleccionada (1 = Simple, 2 = Extenso)
    if var_modo.get() == 1:
        p.roll_simple()
        texto_personaje = p.get_simple_str()
    else:
        p.roll_stats()
        p.set_derived_stats()
        p.set_starting_equipment()
        p.set_flavor()
        texto_personaje = str(p)

    # 2. CÁLCULO DE DIMENSIONES
    lineas = texto_personaje.split("\n")
    nueva_altura = len(lineas) + 1
    anchura_maxima = max(len(linea) for linea in lineas)
    nueva_anchura = max(anchura_maxima + 4, 50)

    # 3. Aplicar configuración
    text_area.config(width=nueva_anchura, height=nueva_altura)

    # 4. Limpiar e Insertar
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.INSERT, texto_personaje)


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
