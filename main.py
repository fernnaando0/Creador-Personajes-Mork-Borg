import time

import character

# ============================================================
# Configuración de la API de Groq
# ============================================================
GROQ_API_KEY = "TU_API_KEY_AQUI"
GROQ_MODEL = "llama3-8b-8192" 
# ============================================================


def generate_lore(char):
    """Llama a la API de Groq para generar el transfondo narrativo del personaje."""
    import urllib.request
    import json

    if GROQ_API_KEY == "TU_API_KEY_AQUI":
        return "[ERROR] Añade tu API key de Groq en la variable GROQ_API_KEY de main.py"

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


def main():
    print("\n" + "=" * 50)
    print("      GENERADOR DE ESCORIA - MÖRK BORG")
    print("=" * 50)
    print("El fin es inevitable. ¿Cómo quieres morir hoy?")

    #Elección del tipo de generación
    print("\n[1] MODO SIMPLE (Solo mecánica: Stats, HP, Equipo)")
    print("[2] MODO EXTENSO (Completo: Rasgos, Pasado, Nombre)")
    print("[3] MODO NARRATIVO (Extenso + Transfondo generado por IA)")

    while True:
        opcion = input("\n>>> Selecciona una opción (1, 2 o 3): ")
        if opcion in ["1", "2", "3"]:
            break
        print("Esa no es una opción válida, miserable.")

    # Input de cantidad
    while True:
        try:
            num_str = input("\n>>> ¿Cuántas almas necesitas? (1-100): ")
            num_chars = int(num_str)
            if num_chars > 0:
                break
            print("Debes crear al menos un personaje.")
        except ValueError:
            print("Eso no es un número, inútil.")

    print(f"\nTirando los dados", end="")

    party = []

    #Bucle de Creación
    for i in range(num_chars):
        new_char = character.Character()

        if opcion == "1":
            new_char.roll_simple()
        else:
            # Opciones 2 y 3 comparten la misma base de generación
            new_char.roll_stats()
            new_char.set_derived_stats()
            new_char.set_starting_equipment()
            new_char.set_flavor()

        if opcion == "3":
            print(f"\n  Invocando a la IA para #{i+1}", end="", flush=True)
            lore = generate_lore(new_char)
            new_char.set_lore(lore)
            print(" ✓")

        party.append(new_char)
        print(".", end="", flush=True)

    print("\n\n" + "#" * 40)
    print("      PROCESO COMPLETADO")
    print("#" * 40 + "\n")

    # 4Mostrar y Guardar
    nombre_archivo = "personajes_mork_borg.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        modo_nombre = "Simple" if opcion == "1" else ("Extenso" if opcion == "2" else "Narrativo (IA)")
        f.write(f"GENERADOS EL: {time.strftime('%d/%m/%Y %H:%M')}\n")
        f.write(f"MODO: {modo_nombre}\n\n")

        for i, char in enumerate(party, 1):
            # Determinamos qué string usar según la opción
            if opcion == "1":
                output = char.get_simple_str()
            elif opcion == "2":
                output = str(char)
            else:
                output = char.get_lore_str()

            # Imprimir en Pantalla
            print(f"PERSONAJE #{i}")
            print(output)
            print("\n")

            # Escribir en el Archivo
            f.write(f"PERSONAJE #{i}\n")
            f.write(output)
            f.write("\n\n" + "-" * 40 + "\n\n")

    print(f"Se han guardado los resultados en '{nombre_archivo}'.")
    print("Que mueran bien.")


if __name__ == "__main__":
    main()