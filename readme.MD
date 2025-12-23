# 💀 ScvmGenerator - MÖRK BORG Character Generator

Un generador de personajes automatizado para el juego de rol **Mörk Borg**. Crea "Nameless Scum" en segundos, calculando estadísticas, equipo, presagios y peculiaridades, respetando las reglas de del juwgo y corrupción mágica.

## ⚔️ Características

- **Generación completa:** Stats (3d6), HP, Plata y Presagios.
- **Lógica de Equipo:** Asigna armas y armaduras compatibles. Si el personaje tiene un Pergamino (Scroll), el sistema asegura que no lleve armadura media ni armas a dos manos (regla de sacrificio).
- **Inventario:** Gestión de mochilas y capacidad.
- **Detalles Narrativos:** Genera nombres, rasgos, cuerpos rotos y hábitos terribles automáticamente.
- **Exportación:** Guarda los personajes generados en un archivo `.txt` para imprimir o compartir.
- **Interfaz Gráfica:** GUI oscura y temática construida con Tkinter.

## 🚀 Cómo usarlo

### Opción A: Ejecutable (Windows)
Descarga el archivo `TheGrinder.exe` desde la sección de Releases (o la carpeta dist) y ejecútalo. No requiere instalación.

### Opción B: Ejecutar desde el código (Python)
Si prefieres correr el script o modificarlo:

1. Asegúrate de tener Python instalado.
2. Clona este repositorio.
3. Ejecuta el archivo de interfaz:
   ```bash
   python interface.py 