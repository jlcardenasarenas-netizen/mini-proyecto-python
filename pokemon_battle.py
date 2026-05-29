import pandas as pd

# ==========================================
# CLASE POKEMON
# ==========================================
class Pokemon:
    def __init__(self, nombre, tipo1, tipo2, hp, ataque, defensa, sp_ataque, sp_defensa, velocidad):
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.hp_actual = hp
        self.ataque = ataque
        self.defensa = defensa
        self.sp_ataque = sp_ataque
        self.sp_defensa = sp_defensa
        self.velocidad = velocidad

    def esta_vivo(self):
        return self.hp_actual > 0

    def recibir_dano(self, dano):
        self.hp_actual -= dano
        if self.hp_actual < 0:
            self.hp_actual = 0

    def atacar(self, enemigo):
        dano = max(1, self.ataque - enemigo.defensa)
        enemigo.recibir_dano(dano)
        return dano

    def mostrar_tarjeta(self):
        print(f"\n{'='*40}")
        print(f"  {self.nombre}")
        print(f"  Tipo: {self.tipo1} / {self.tipo2}")
        print(f"  HP: {self.hp_actual}/{self.hp}")
        print(f"  Ataque: {self.ataque} | Defensa: {self.defensa}")
        print(f"  Velocidad: {self.velocidad}")
        print(f"{'='*40}")

# ==========================================
# CLASE SISTEMA DE POKÉMONS
# ==========================================
class SistemaPokemon:
    def __init__(self):
        self.pokemones = {}
        self.cargar_csv()

    def cargar_csv(self):
        try:
            datos = pd.read_csv("data/pokemon.csv")
            for _, fila in datos.iterrows():
                nombre = fila["name"]
                self.pokemones[nombre] = Pokemon(
                    nombre=nombre,
                    tipo1=fila["type_1"],
                    tipo2=str(fila["type_2"]) if pd.notna(fila["type_2"]) else "Ninguno",
                    hp=int(fila["hp"]),
                    ataque=int(fila["attack"]),
                    defensa=int(fila["defense"]),
                    sp_ataque=int(fila["sp_attack"]),
                    sp_defensa=int(fila["sp_defense"]),
                    velocidad=int(fila["speed"])
                )
            print(f"Se cargaron {len(self.pokemones)} pokémons.")
        except Exception as e:
            print(f"Error cargando CSV: {e}")

    def agregar_pokemon(self, nombre, tipo1, tipo2, hp, ataque, defensa, sp_ataque, sp_defensa, velocidad):
        self.pokemones[nombre] = Pokemon(nombre, tipo1, tipo2, hp, ataque, defensa, sp_ataque, sp_defensa, velocidad)
        print(f"{nombre} agregado exitosamente.")

    def eliminar_pokemon(self, nombre):
        if nombre in self.pokemones:
            del self.pokemones[nombre]
            print(f"{nombre} eliminado.")
        else:
            print(f"{nombre} no encontrado.")

    def modificar_hp(self, nombre, nuevo_hp):
        if nombre in self.pokemones:
            self.pokemones[nombre].hp = nuevo_hp
            print(f"HP de {nombre} actualizado a {nuevo_hp}.")
        else:
            print(f"{nombre} no encontrado.")

    def buscar_pokemon(self, nombre):
        if nombre in self.pokemones:
            self.pokemones[nombre].mostrar_tarjeta()
        else:
            print(f"{nombre} no encontrado.")

    def batalla(self, nombre1, nombre2):
        if nombre1 not in self.pokemones or nombre2 not in self.pokemones:
            print("Uno o ambos pokémons no existen.")
            return

        p1 = Pokemon(
            self.pokemones[nombre1].nombre, self.pokemones[nombre1].tipo1,
            self.pokemones[nombre1].tipo2, self.pokemones[nombre1].hp,
            self.pokemones[nombre1].ataque, self.pokemones[nombre1].defensa,
            self.pokemones[nombre1].sp_ataque, self.pokemones[nombre1].sp_defensa,
            self.pokemones[nombre1].velocidad
        )
        p2 = Pokemon(
            self.pokemones[nombre2].nombre, self.pokemones[nombre2].tipo1,
            self.pokemones[nombre2].tipo2, self.pokemones[nombre2].hp,
            self.pokemones[nombre2].ataque, self.pokemones[nombre2].defensa,
            self.pokemones[nombre2].sp_ataque, self.pokemones[nombre2].sp_defensa,
            self.pokemones[nombre2].velocidad
        )

        print(f"\n*** BATALLA: {p1.nombre} vs {p2.nombre} ***")
        ronda = 1
        while p1.esta_vivo() and p2.esta_vivo():
            print(f"\n-- Ronda {ronda} --")
            dano = p1.atacar(p2)
            print(f"{p1.nombre} ataca a {p2.nombre} por {dano} de daño. HP restante: {p2.hp_actual}")
            if not p2.esta_vivo():
                break
            dano = p2.atacar(p1)
            print(f"{p2.nombre} ataca a {p1.nombre} por {dano} de daño. HP restante: {p1.hp_actual}")
            ronda += 1

        ganador = p1.nombre if p1.esta_vivo() else p2.nombre
        print(f"\n¡{ganador} GANA LA BATALLA!")

# ==========================================
# MENÚ PRINCIPAL
# ==========================================
sistema = SistemaPokemon()

while True:
    print("\n===== MENÚ POKEMON =====")
    print("1. Buscar Pokémon")
    print("2. Agregar Pokémon")
    print("3. Eliminar Pokémon")
    print("4. Modificar HP")
    print("5. Batalla")
    print("6. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del Pokémon: ")
        sistema.buscar_pokemon(nombre)
    elif opcion == "2":
        nombre = input("Nombre: ")
        tipo1 = input("Tipo 1: ")
        tipo2 = input("Tipo 2: ")
        hp = int(input("HP: "))
        ataque = int(input("Ataque: "))
        defensa = int(input("Defensa: "))
        sp_ataque = int(input("SP Ataque: "))
        sp_defensa = int(input("SP Defensa: "))
        velocidad = int(input("Velocidad: "))
        sistema.agregar_pokemon(nombre, tipo1, tipo2, hp, ataque, defensa, sp_ataque, sp_defensa, velocidad)
    elif opcion == "3":
        nombre = input("Nombre del Pokémon a eliminar: ")
        sistema.eliminar_pokemon(nombre)
    elif opcion == "4":
        nombre = input("Nombre del Pokémon: ")
        nuevo_hp = int(input("Nuevo HP: "))
        sistema.modificar_hp(nombre, nuevo_hp)
    elif opcion == "5":
        nombre1 = input("Pokémon 1: ")
        nombre2 = input("Pokémon 2: ")
        sistema.batalla(nombre1, nombre2)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")