
CHARACTER_CLASSES = {
    "Guerrero": {"vida": 150, "mana": 50, "vel": 10, "def": 20, "ataque": 30},
    "Arquero": {"vida": 100, "mana": 30, "vel": 20, "def": 10, "ataque": 25},
    "Mago": {"vida": 80, "mana": 100, "vel": 15, "def": 5, "ataque": 40}
}

SPELLS = {
    "Bola de Fuego": {"dano": 25, "costo_mana": 20},
    "Carámbano de Hielo": {"dano": 20, "costo_mana": 15},
    "Rayo": {"dano": 30, "costo_mana": 25},
    "Cura": {"cura": 30, "costo_mana": 10},
    "Berserk": {"vida": 20, "velocidad": -5, "ataque": 10, "defensa": -10}
}

BUFFS = {"daño": 5, "defensa": 5, "velocidad": 5}
DEBUFFS = {"ataque": -5, "defensa": -5, "velocidad": -5}


ENEMIES = {
    "Esqueleto": {"arma": ["espada", "arco"], "monedas": (1, 5), "vida": 60},
    "Goblin": {"arma": ["espada", "arco"], "monedas": (1, 5), "vida": 50},
    "Trol": {"arma": ["espada"], "monedas": (5, 10), "vida": 100},
    "Fantasma": {"arma": ["mele"], "monedas": 1, "vida": 40},
    "Zombie": {"arma": ["mele"], "monedas": (1, 3), "vida": 55},
    "Bandido": {"arma": ["espada", "arco"], "monedas": (5, 10), "vida": 65},
    "Vaca": {"arma": None, "drop": "carne", "vida": 20},
    "Gallina": {"arma": None, "drop": "carne", "vida": 10},
    "Jabalí": {"arma": ["mele"], "drop": "carne", "vida": 30}
}

BOSSES = {
    "Rey Esqueleto": {"arma": ["espada y escudo", "arco"], "monedas": (15, 25), "vida": 200},
    "Orco": {"arma": ["espada"], "monedas": (10, 20), "vida": 150},
    "Lich Esqueleto": {"arma": ["varita"], "monedas": (20, 40), "vida": 180},
    "Mago Orco": {"arma": ["varita"], "monedas": (15, 30), "vida": 160}
}

ITEMS = {
    "pocion_vida": {"tipo": "pocion", "efecto": "vida", "valor": 50},
    "pocion_mana": {"tipo": "pocion", "efecto": "mana", "valor": 30},
    "espada_grande": {"tipo": "arma", "dano": 20},
    "espada_normal": {"tipo": "arma", "dano": 10},
    "arco_grande": {"tipo": "arma", "dano": 15},
    "arco_normal": {"tipo": "arma", "dano": 10},
    "escudo_grande": {"tipo": "escudo", "defensa": 15},
    "escudo_normal": {"tipo": "escudo", "defensa": 10},
    "bara_magica": {"tipo": "arma", "dano": 25},
    "moneda": {"tipo": "moneda", "valor": 1},
    "flechas": {"tipo": "municion", "cantidad": 20},
    "carne": {"tipo": "comida", "valor": 10}
}
