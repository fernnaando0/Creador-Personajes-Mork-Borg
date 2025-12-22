import random

# --- 1. MOTOR LÓGICO (Lo que usan otros archivos) ---

def roll(n, sides) -> int:
    """Tira 'n' dados de 'sides' caras y devuelve la suma (int)."""
    total = 0
    for _ in range(n):
        total += random.randint(1, sides)
    return total

def d4():
    return roll(1, 4)

def d6():
    return roll(1, 6)

def d8():
    return roll(1, 8)

def d10():
    return roll(1, 10)

def d12():
    return roll(1, 12)

def d20():
    return roll(1, 20)

def d66():
    """El d66 en Mörk Borg es Decenas y Unidades (ej: 11 a 66)."""
    tens = d6()
    ones = d6()
    return (tens * 10) + ones


# --- 3. BLOQUE DE PRUEBAS (Solo se ejecuta si lanzas este archivo) ---

if __name__ == "__main__":
    print("--- Probando lógica ---")
    print(f"1d20: {d20()}")
    print(f"d66: {d66()}")
    
    print("\n--- Probando tu Arte Visual ---")
    try:
        num = int(input("¿Cuántos d6 quieres tirar para ver el arte?: "))
        resultados = []
        for _ in range(num):
            resultados.append(d6())
        
        print(f"Resultados numéricos: {resultados}")
        print(f"Suma total: {sum(resultados)}")
    except ValueError:
        print("Por favor, introduce un número válido.")