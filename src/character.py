import dice
import tables
import random

class Character:
    #Inicializamos el personaje
    def __init__(self):
        self.name = "Nameless Scum"
        
        # Stats
        self.strength = 0
        self.agility = 0
        self.presence = 0
        self.toughness = 0
        
        # Estado
        self.hp = 0
        self.silver = 0
        
        # Equipo (Huecos específicos)
        self.weapon = None
        self.armor = None
        self.backpack = None
        self.objeto1 = ""
        self.objeto2 = ""

        # Narrativa
        self.name = ""
        self.omens = 0
        self.traits = []

        # Detalles
        self.broken_body = ""
        self.troubling_tale = ""
        self.bad_habits = ""

    # Esta funcion recibe la suma de los 3 d6 y devuelve su valor 
    def get_ability_modifier(self, value_3d6):
        if 1 <= value_3d6 <= 4: return -3
        elif 5 <= value_3d6 <= 6: return -2
        elif 7 <= value_3d6 <= 8: return -1
        elif 9 <= value_3d6 <= 12: return 0
        elif 13 <= value_3d6 <= 14: return 1
        elif 15 <= value_3d6 <= 16: return 2
        elif 17 <= value_3d6 <= 20: return 3
        return 0

    #Esta funcion genera los 4 stats principales
    def roll_stats(self):
        self.strength = self.get_ability_modifier(dice.roll(3, 6))
        self.agility = self.get_ability_modifier(dice.roll(3, 6))
        self.presence = self.get_ability_modifier(dice.roll(3, 6))
        self.toughness = self.get_ability_modifier(dice.roll(3, 6))
    
    def set_starting_equipment(self):
        # 1. Asignación inicial básica
        self.weapon = random.choice(tables.weapons)
        self.armor = random.choice(tables.armors)
        self.backpack = random.choice(tables.backpacks)
        
        # Elegimos los objetos "brutos" (puede salir "Scroll aleatorio")
        raw_obj1 = random.choice(tables.objetos_lista1)
        raw_obj2 = random.choice(tables.objetos_lista2)

        # 2. RESOLUCIÓN DE SCROLLS (La Magia)
        # Si salió el texto genérico de scroll unclean, elegimos uno específico
        if "Unclean Scroll aleatorio" in raw_obj1:
            scroll = random.choice(tables.unclean_scrolls)
            self.objeto1 = f"Unclean Scroll - {scroll}"
        else:
            self.objeto1 = raw_obj1

        # Lo mismo para el objeto 2 (que tiene los sacred scrolls)
        if "Scroll sagrado aleatorio" in raw_obj2:
            scroll = random.choice(tables.sacred_scrolls)
            self.objeto2 = f"Sacred Scroll - {scroll}"
        else:
            self.objeto2 = raw_obj2


        # 3. REGLA DE RESTRICCIÓNç
        # Verificamos si finalmente tenemos algún scroll en el inventario final
        has_scroll = "Scroll" in self.objeto1 or "Scroll" in self.objeto2

        if has_scroll:
            # Restricción de arma: Máximo d6 de daño.
            while self.weapon.get('damage_dice', 0) > 6:
                self.weapon = random.choice(tables.weapons)

            # Restricción de armadura: Máximo Tier 1 (Light).
            while self.armor.get('tier', 0) >= 2:
                self.armor = random.choice(tables.armors)
    
    #Calcula HP y Plata
    def set_derived_stats(self):
        self.hp = self.toughness + dice.d8()
        if self.hp < 1:
            self.hp = 1     
        self.silver = dice.roll(2, 6) * 10

    #Define la personalidad y el transfondo del personaje
    def set_flavor(self):
        self.name = random.choice(tables.names)
        self.omens = random.randint(1,2)
        self.traits = random.sample(tables.traits, 2)
        
        self.broken_body = random.choice(tables.broken_bodies)
        self.bad_habits = random.choice(tables.bad_habits) 
        self.troubling_tale = random.choice(tables.troubling_tales)


    def __str__(self):
        # --- FORMATEO CADENA DE DATOS ---

        # Arma
        if self.weapon:
            dmg = self.weapon.get("damage_dice", 0)
            w_str = f"{self.weapon['name']} (Dmg: {dmg})"
        else:
            w_str = "None"

        # Armadura
        if self.armor:
            tier = self.armor.get("tier", 0)
            dr = self.armor.get("dr_dice") 
            if dr:
                a_str = f"{self.armor['name']} (-d{dr})"
            else:
                a_str = f"{self.armor['name']} (Tier {tier})"
        else:
            a_str = "None"

        # Mochila
        if self.backpack:
            bp_name = self.backpack['name']
            bp_capacidad = self.backpack['capacidad']
            bp_str = f"{bp_name} (Cap: {bp_capacidad})"    
        else:
            bp_str = "None"
                 
        # Traits
        traits_str = " y ".join(self.traits)
        

        # --- IMPRESIÓN FINAL ---
        return (
            f"========================================\n"
            f" NOMBRE: {self.name}\n"
            f"========================================\n"
            f" HP: {self.hp}  |  Plata: {self.silver}  |  Omens: {self.omens}\n"
            f"----------------------------------------\n"
            f" Fuerza: {self.strength:2}  |  AGI: {self.agility:2}  |  PRE: {self.presence:2}  |  DUR: {self.toughness:2}\n"
            f"----------------------------------------\n"
            f" Arma:     {w_str}\n"
            f" Armadura: {a_str}\n"
            f" Mochila:  {bp_str}\n"
            f"----------------------------------------\n"
            f" Inventario:\n"
            f"   - {self.objeto1}\n"
            f"   - {self.objeto2}\n"
            f"----------------------------------------\n"
            f" RASGOS: {traits_str}\n"
            f"----------------------------------------\n"
            f" BROKEN BODY:    {self.broken_body}\n"
            f" BAD HABIT:      {self.bad_habits}\n"
            f" TROUBLING TALE: {self.troubling_tale}\n"
            f"========================================"
        )
    
# --- PRUEBA ---
if __name__ == "__main__":
    p = Character()
    p.roll_stats()       
    p.set_derived_stats()
    p.set_starting_equipment()
    p.set_flavor()
    print(p)