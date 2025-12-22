import tkinter as tk
from tkinter import scrolledtext  # Para la caja de texto con scroll
from tkinter import messagebox    # Para ventanas emergentes
import character                  # Tu módulo de lógica

def generar_personaje():
    # 1. Generar lógica del personaje
    p = character.Character()
    p.roll_stats()
    p.set_derived_stats()
    p.set_starting_equipment()
    p.set_flavor()
    
    texto_personaje = str(p)
    
    # 2. CÁLCULO DE DIMENSIONES (Alto y Ancho)
    # Dividimos el texto en una lista de líneas
    lineas = texto_personaje.split('\n')
    
    # A) Altura: Contamos cuántas líneas hay (+ un margen pequeño)
    nueva_altura = len(lineas) + 1
    
    # B) Anchura: Buscamos la línea más larga de todas
    anchura_maxima = max(len(linea) for linea in lineas)
    
    # Le damos un margen extra de seguridad (+4 caracteres)
    nueva_anchura = anchura_maxima + 4
    
    # Establecemos un mínimo para que la ventana no sea ridículamente estrecha
    if nueva_anchura < 50:
        nueva_anchura = 50

    # 3. Aplicar configuración a la caja de texto
    # Al cambiar el tamaño de text_area, la ventana (app) se adaptará sola
    text_area.config(width=nueva_anchura, height=nueva_altura)

    # 4. Limpiar e Insertar
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.INSERT, texto_personaje)

def guardar_archivo():
    """Guarda lo que haya en la caja de texto en un archivo .txt"""
    contenido = text_area.get('1.0', tk.END)
    
    # Si la caja está vacía (solo tiene el salto de línea final), no guardamos
    if len(contenido) < 2:
        messagebox.showwarning("Cuidado", "Primero genera un personaje.")
        return

    try:
        with open("personaje_guardado.txt", "w", encoding="utf-8") as f:
            f.write(contenido)
        messagebox.showinfo("Éxito", "Personaje guardado en 'personaje_guardado.txt'")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")

# --- CONFIGURACIÓN DE LA VENTANA PRINCIPAL ---

app = tk.Tk()
app.title("Generador MÖRK BORG")
app.configure(bg="#202020")

# 1. ETIQUETA DE TÍTULO (Primero para que salga arriba)
title_label = tk.Label(
    app, 
    text=" SCUM GENERATOR ", 
    font=("Old English Text MT", 24, "bold"),
    bg="#202020",
    fg="#F1C40F" # Amarillo Mörk Borg
)
title_label.pack(pady=20) 

# 2. CAJA DE TEXTO
text_area = scrolledtext.ScrolledText(
    app, 
    width=50,  # Valor inicial
    height=10, # Valor inicial
    font=("Consolas", 10), 
    bg="#000000", 
    fg="#00FF00"
)
# Auto-ajuste de ancho funcione bien
text_area.configure(wrap=tk.NONE) 
text_area.pack(padx=20, pady=10)

# 3. BOTONES (Abajo del todo)
button_frame = tk.Frame(app, bg="#202020")
button_frame.pack(pady=20)

# Botón Generar
btn_generate = tk.Button(
    button_frame, 
    text="INVOCAR DESGRACIADO", 
    font=("Chiller", 12, "bold"),
    bg="#800000", # Rojo sangre
    fg="white",
    command=generar_personaje 
)
btn_generate.pack(side=tk.LEFT, padx=20)

# Botón Guardar
btn_save = tk.Button(
    button_frame, 
    text="GUARDAR TXT", 
    font=("Chiller", 12, "bold"),
    bg="#404040", 
    fg="white",
    command=guardar_archivo
)
btn_save.pack(side=tk.LEFT, padx=20)

# 4. INICIAR EL BUCLE
app.mainloop()