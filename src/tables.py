"""
tables.py
Almacena todos los datos estáticos del juego (tablas de texto).
Usamos diccionarios o listas según convenga.
"""

armors = [
    {"name": "Sin armadura", "tier": 0, "dr_dice": None},          # 1
    {"name": "Sin armadura", "tier": 0, "dr_dice": None},          # 2
    {"name": "Pelaje/Cuero", "tier": 1, "dr_dice": 2},  # 3
    {"name": "Pelaje/Cuero", "tier": 1, "dr_dice": 2},  # 4
    {"name": "Acero/Malla", "tier": 2, "dr_dice": 4},  # 6
    {"name": "Acero/Malla", "tier": 2, "dr_dice": 4} # 6
]

# Armas (Weapons) - Tabla inicial básica
weapons = [
    {"name": "Fémur", "damage_dice": 2},#1
    {"name": "Bastón de lucha", "damage_dice": 4},#2
    {"name": "Espada corta", "damage_dice": 4},#3
    {"name": "Cuchillo", "damage_dice": 4},#4
    {"name": "Martillo de guerra", "damage_dice": 6},#5
    {"name": "Espada", "damage_dice": 6},#6
    {"name": "Arco (Presencia y 10 flechas)", "damage_dice": 6},#7
    {"name": "Maza", "damage_dice": 8},#8
    {"name": "Ballesta (Presencia y 10 proyectiles)", "damage_dice": 8},#9
    {"name": "Mandoble", "damage_dice": 8}#10
]
    
# Tabla de Modificadores de Habilidad (Ability Mods)
# Formato: (min, max, modificador)
ability_modifiers = [
    (1, 4, -3),
    (5, 6, -2),
    (7, 8, -1),
    (9, 12, 0),
    (13, 14, 1),
    (15, 16, 2),
    (17, 20, 3)
]

#Tablas de nombres
names = [
    "Aerg-Tval", "Agn", "Arzog", "Brint", "Bodd", "Copernicus", 
    "Daeru", "Drak", "Eldar", "Felban", "Gitt", "Haerü", 
    "Kurg", "Lom", "Malok", "Nagl", "Prife", "Rulf", 
    "Ssun", "Tor", "Ulaf", "Varg", "Wemut"
]

#Tabla de "traits"
traits = [
    "Eternamente enfadado", "Complejo de inferioridad", "Problemas con la autoridad", "Bocazas", "Egocéntrico", "Nihilista", "Politoxicómano", "Conflictivo", "Ladino",
    "Vengativo", "Cobarde", "Vago", "Desconfiado", "Despiadado", "Aprensivo", "Resentido", "Mentiroso", "Derrochador", "Arrogante"
]

#Tabla de broken bodies
broken_bodies = [
    "Mirada maníaca y fija.",
    "Cubierto de tatuajes blasfemos (para algunos).",
    "Rostro podrido. Lleva una máscara.",
    "Perdió tres dedos del pie, cojea.",
    "Famélico: demacrado y pálido.",
    "Una mano reemplazada por un garfio oxidado (d6 de daño).",
    "Dientes en descomposición.",
    "De una belleza inquietante, sobrenaturalmente limpio.",
    "Manos cubiertas de llagas.",
    "Cataratas extendiéndose lenta pero firmemente en ambos ojos.",
    "Pelo largo y enredado, con al menos una cucaracha residiendo en él.",
    "Orejas rotas y aplastadas.",
    "Temblores y tartamudeo por daño nervioso o estrés.",
    "Corpulento, voraz, baboso.",
    "A una mano le faltan los dedos pulgar e índice, agarra como una langosta.",
    "Nariz de alcohólico, roja e hinchada.",
    "Rostro de maníaco en reposo, hacer amigos es difícil.",
    "Pie de atleta crónico. Apesta.",
    "Ojo recientemente acuchillado y maloliente cubierto con un parche.",
    "Uñas agrietadas y negras, quizá a punto de caerse."
]

#Tabla de malos hábitos
bad_habits = [
    "Coleccionas obsesivamente piedras pequeñas y afiladas.",
    "No usas una hoja sin probarla antes en tu propia carne. Brazos cubiertos de cicatrices.",
    "Incapaz de dejar de beber una vez que has empezado.",
    "Adicto al juego. Debes apostar cada día. Si pierdes, sube la apuesta y vuelve a jugar.",
    "Intolerante a cualquier tipo de crítica. Provoca ira y llanto.",
    "Incapaz de ir al grano. Nunca has terminado de contar una historia.",
    "Tu mejor amigo es una calavera. La llevas contigo, se lo cuentas todo; no confías en nadie más.",
    "Te hurgas la nariz tan profundamente que sangras.",
    "Ríes histéricamente de tus propios chistes, los cuales explicas después en detalle.",
    "Nihilista. Insistes en decirle a todo el mundo que lo eres y en explicar por qué.",
    "Devorador de insectos inveterados.",
    "Tu respuesta al estrés es el exhibicionismo estético. Cuanto peor van las cosas, más elegante necesitas estar.",
    "Depósito permanente de flema en la garganta. Toses, resoplas, escupes y tragas continuamente.",
    "Pirómano.",
    "Pierdes objetos importantes y olvidas datos vitales constantemente.",
    "Agitador/metemierda inseguro. Hablarás mal de cualquiera que acabe de salir de la habitación.",
    "Tartamudeas cuando mientes.",
    "Sueltas risitas dementes en los peores momentos posibles.",
    "Silbas cuando intentas esconderte. Lo negarás. Silbas cuando sale 5, 7, 9, 11 o 13 en un d20.",
    "Haces joyería con los dientes de los muertos."
]

#Tabla de problemas
troubling_tales = [
    "Perseguido por homicidio involuntario. Hay una recompensa por tu cabeza.",
    "En deuda masiva. La deuda está siendo vendida a grupos cada vez más despiadados.",
    "Posees un objeto raro y muy codiciado.",
    "Tienes una herida maldita que nunca sana.",
    "Tuviste un romance ilegal, inmoral y secreto con un miembro de la familia real. Tienes pruebas.",
    "Miembro fugitivo de una secta. Aterrado y paranoico. Otros cultistas están en todas partes.",
    "Un ladrón de identidad que recientemente mató y reemplazó a esta persona.",
    "Desterrado y repudiado por actos no especificados. Nunca podrás volver a casa.",
    "Desertor militar tras presenciar una masacre. Precio por tu cabeza. Tus antiguos amigos te dan caza.",
    "Has asesinado a un pariente cercano muy recientemente. Muy recientemente.",
    "Un cubo rompecabezas ha sido calibrado incorrectamente (¿o no?), despertando a una abominación durmiente.",
    "Las criaturas malvadas aman el olor de tu rastro y se sienten atraídas por él, sembrando el desastre a tu paso.",
    "Una herida de batalla dejó un fragmento de metal que se acerca lentamente a tu corazón. Cada día hay un 2% de probabilidad de que lo alcance.",
    "La violencia te obligó a exiliarte en la naturaleza. Crees que los árboles que se mecen susurran. Hablas, gritas y atacas a los árboles.",
    "Estás maldito y compartes las pesadillas de los demás; duermes muy, muy lejos de cualquier otra persona.",
    "En guerra permanente contra todos los cuervos. No hay contacto sin violencia. Siempre llevas una honda.",
    "Después de soñar con un templo enterrado a un dios olvidado entiendes las canciones de los insectos y los gusanos.",
    "Eres seguido y observado por un golem despues de un trato que no puedes recordar.",
    "Quemar o ser quemado es tu ley.",
    "Tus heridas se recuperan el doble de rápido, las de tus compañeros en cambio el doble de lento."
]

#Tabla de mochilas
backpacks = [
    {"name" : "Nada", "capacidad" : 0},
    {"name" : "Mochila", "capacidad" : 7},
    {"name" : "Saco", "capacidad" : 10},
    {"name" : "Carro pequeño", "capacidad" : 100},
    {"name" : "Burro", "capacidad" : 200},
]

#Tablas de objetos 1 y 2
objetos_lista1 = [
    "Cuerda de 10 metros", "Presencia + 4 antorchas", "Linterna con aceite para Presencia + 6 horas", "Barra de magnesio", "Unclean Scroll aleatorio", 
    "Aguja muy afilada", "Un botiquín con presencia +4 usos", "Plancha de metal y clavos", "Trampa para osos (DR14 para ponerla, D8 daño)", "Bomba (D10 daño)", 
    "Veneno D4 dosis (D10 daño)", "Crucifijo de plata"
]

objetos_lista2 = [
    "1 elixir de la vida D4 dosis (Recuperas HP6 y cura infección)", "Scroll sagrado aleatorio", "Perro pequeño y vicioso que solo te obedece a ti (D6 + 2 HP, D4 daño)",
    "Perfume de gran calidad (valorado en 25 de plata)", "Caja de herramientas con 10 clavos, pinzas, martillo, sierra pequeña y taladro manual", "Pesada cadena de 5 metros",
    "Gancho de agarre", "Escudo (-1 HP damage o romperlo para parar un ataque)", "Palanca (D4 daño)", "Grasa animal (Equivale a 5 días de comida)", "Tienda de campaña"
]

#Tablas de pergaminos
unclean_scrolls = [
    "Las Palmas Abren la Puerta Sur: Una bola de fuego impacta a d2 criaturas infligiendo d8 de daño a cada una.",
    "Lengua de Eris: Una criatura a tu elección queda confundida durante 10 minutos.",
    "Te-le-qui-ne-sis: Mueve un objeto hasta d10×10 pies durante d6 minutos.",
    "Levitación de Lucy-fuego: Flota en el aire durante Presencia + d10 rondas.",
    "Demonio de los Capilares: Una criatura se asfixia durante d6 rondas, perdiendo d4 HP por ronda.",
    "Nueve Signos Violetas Desanudan la Tormenta: Produce d2 rayos que infligen d6 de daño cada uno.",
    "Metzhuotl Ciega tu Ojo: Una criatura se vuelve invisible por d6 rondas o hasta ser dañada (DR6 para golpear/defender).",
    "Psicopompo Pútrido: Invoca (d6) 1–3: d4 esqueletos, 4–6: d4 zombis.",
    "El Párpado Ciega la Mente: d4 criaturas caen dormidas una hora a menos que superen una prueba de DR14.",
    "Muerte: Todas las criaturas en un radio de 30 pies pierden un total de 4d10 HP."
]

sacred_scrolls = [
    "Gracia de un Santo Muerto: d2 criaturas recuperan d10 HP cada una.",
    "Gracia para un Pecador: Una criatura a tu elección obtiene +d6 en una tirada (daño, pruebas, etc.).",
    "Susurros Cruzan el Umbral: Haz tres preguntas a una criatura fallecida.",
    "Égida del Dolor: Una criatura a tu elección gana 2d6 HP extra durante 10 rondas.",
    "Destino Inconcluso: Una criatura, muerta hace no más de una semana, es despertada con recuerdos terribles.",
    "Habla Bestial: Puedes hablar con los animales durante d20 minutos.",
    "Falso Amanecer / Carro de la Noche: Luz u oscuridad total durante 3d10 minutos.",
    "Paso Hermético: Encuentras todas las trampas en tu camino durante 2d10 minutos.",
    "Mirada Consuntiva de Roskoe: d4 criaturas pierden d8 HP cada una.",
    "Sintaxis Enociana: Una criatura obedece ciegamente una sola orden."
]