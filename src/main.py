import time

import character


def main():
    print("\n" + "=" * 50)
    print("   GENERADOR DE ESCORIA - MÖRK BORG")
    print("=" * 50)
    print("El fin se acerca. ¿Cuántas almas desgraciadas")
    print("necesitas sacrificar hoy?")

    # Input del usuario
    while True:
        try:
            num_str = input("\n>>> Introduce un número (1-100): ")
            num_chars = int(num_str)
            if num_chars > 0:
                break
            print("Debes crear al menos un personaje.")
        except ValueError:
            print("Eso no es un número, inútil.")

    print(f"\nTirando los dados")

    # Lista para guardar los personajes creados
    party = []

    # 3. Bucle de Creación
    for i in range(num_chars):
        # A) Crea el personaje
        new_char = character.Character()

        # B) Ejecutamos todos los pasos
        new_char.roll_stats()
        new_char.set_derived_stats()
        new_char.set_starting_equipment()
        new_char.set_flavor()

        # C) Lo guardamos en la lista
        party.append(new_char)
        print(f".", end="", flush=True)

    print("\n\n" + "#" * 40)
    print("      PROCESO COMPLETADO")
    print("#" * 40 + "\n")

    # 4. Mostrar y Guardar
    # Abrimos un archivo de texto para escribir
    nombre_archivo = "personajes_mork_borg.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"GENERADOS EL: {time.strftime('%d/%m/%Y %H:%M')}\n\n")

        for i, char in enumerate(party, 1):
            # Imprimir en Pantalla (Terminal)
            print(f"PERSONAJE #{i}")
            print(char)
            print("\n")

            # Escribir en el Archivo de Texto
            f.write(f"PERSONAJE #{i}\n")
            f.write(str(char))
            f.write("\n\n" + "-" * 40 + "\n\n")

    print(f"Se han guardado los resultados en '{nombre_archivo}'.")
    print("Que mueran bien.")


if __name__ == "__main__":
    main()
