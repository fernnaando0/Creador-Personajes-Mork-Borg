import time

import character


def main():
    print("\n" + "=" * 50)
    print("      GENERADOR DE ESCORIA - MÖRK BORG")
    print("=" * 50)
    print("El fin es inevitable. ¿Cómo quieres morir hoy?")

    #Elección del tipo de generación
    print("\n[1] MODO SIMPLE (Solo mecánica: Stats, HP, Equipo)")
    print("[2] MODO EXTENSO (Completo: Rasgos, Pasado, Nombre)")

    while True:
        opcion = input("\n>>> Selecciona una opción (1 o 2): ")
        if opcion in ["1", "2"]:
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
            new_char.roll_stats()
            new_char.set_derived_stats()
            new_char.set_starting_equipment()
            new_char.set_flavor()

        party.append(new_char)
        print(".", end="", flush=True)

    print("\n\n" + "#" * 40)
    print("      PROCESO COMPLETADO")
    print("#" * 40 + "\n")

    # 4Mostrar y Guardar
    nombre_archivo = "personajes_mork_borg.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"GENERADOS EL: {time.strftime('%d/%m/%Y %H:%M')}\n")
        f.write(f"MODO: {'Simple' if opcion == '1' else 'Extenso'}\n\n")

        for i, char in enumerate(party, 1):
            # Determinamos qué string usar según la opción
            if opcion == "1":
                output = char.get_simple_str()
            else:
                output = str(char)

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
