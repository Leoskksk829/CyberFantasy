import time
import random
import os
import sys

#TYPEWRITER EFFECT 
def printsys(testo, velocita=0.03):
    for lettera in testo:
        sys.stdout.write(lettera)
        sys.stdout.flush()
        time.sleep(velocita)
    print()

#HP
class Player_Health:
    def __init__(self, hp):
        self.hp = hp

    def rimuovi(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.hp = 0
            print()
            print("GAME OVER")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

    def aggiungi(self, hp):
        self.hp += hp
        if self.hp > 100:
            self.hp = 100
        print()
        print("Healed!")
        print ()

player = Player_Health(100)

#POTIONS
class Pozione:
    def __init__(self, tipo, hp):
        self.tipo = tipo
        self.hp = hp

    def usa(self, player, messaggio=True):
        player.aggiungi(self.hp)
        if messaggio:
            print(f"You used a {self.tipo} and recovered {self.hp} HP!")

pozione_MASTER = Pozione("Master", 100)
pozione_big = Pozione("Master", 75)
pozione_middle = Pozione("Middle", 50)
pozione_small = Pozione("Small", 25)
pozione_tiny = Pozione("Tiny", 10)

#WEAPONS
class Armi:
    def __init__(self, tipo, danno):
        self.tipo = tipo
        self.danno = danno

    def attacca(self, nemico):
        print()
        print(f"You attacked the {nemico.tipo} and dealt {self.danno} damage!")
        return nemico.rimuovi(self.danno)

armi_spadaInfuocata = Armi("Spada Infuocata", 100)
armi_martello = Armi("Martello", 35)
armi_spada = Armi("Spada", 20)
armi_coltello = Armi("Coltello", 5)
armi_ascia = Armi("Ascia", 40)

#FINAL REWARD
class premio:
    def __init__(self, tipo, valore=100):
        self.tipo = tipo
        self.valore = valore

    def aggiungi(self, player):
        print()
        printsys(f"You obtained the final reward: {self.tipo}!")
        print()
        return player.aggiungi(self.valore)

premio_finale = premio("Cuore di Drago", 100)

#ENEMY LOOT
loot_goblin_pozioni = {
    pozione_tiny: 60,
    pozione_small: 40
}
loot_goblin_armi = {
    armi_coltello: 60,
    armi_spada: 40
}
loot_zombie_pozioni = {
    pozione_small: 60,
    pozione_middle: 40
}
loot_zombie_armi = {
    armi_spada: 100
}
loot_vampiro_pozioni = {
    pozione_middle: 60,
    pozione_big: 40,
}
loot_vampiro_armi = {
    armi_martello: 100
}
loot_orco_pozioni = {
    pozione_big: 45,
    pozione_middle: 35,
    pozione_MASTER: 10
}
loot_orco_armi = {
    armi_ascia: 90,
    armi_spadaInfuocata: 10
}

lista_loot_pozioni = [loot_goblin_pozioni, loot_zombie_pozioni, loot_vampiro_pozioni, loot_orco_pozioni]
lista_loot_armi = [loot_goblin_armi, loot_zombie_armi, loot_vampiro_armi, loot_orco_armi]

#INVENTORY
class inventario:
    def __init__(self):
        self.items = []

    def aggiungi(self, item, messaggio=True):
        self.items.append(item)
        if messaggio:
            if isinstance(item, Pozione):
                print()
                print(f"[ ! ] Added {item.tipo} to the inventory! It can heal you for: {item.hp} HP")
            else:
                print(f"[ ! ] Added {item.tipo} to the inventory! It can help you by dealing: {item.danno} damage")
                print ("")

    def rimuovi(self, item, messaggio=True):
        if item in self.items:
            self.items.remove(item)
            if messaggio:
                print(f"{item.tipo} removed from the inventory.")
        else:
            if messaggio:
                print()
                print(f"{item.tipo} is not in the inventory.")
                print()

    def usa_pozione(self, pozione, player, messaggio=True):
        if pozione in self.items:
            pozione.usa(player, messaggio=messaggio)
            self.rimuovi(pozione, messaggio=messaggio)
        else:
            if messaggio:
                print()
                print(f"{pozione} is not in the inventory.")
                print()


#MONSTERS: goblin, zombie, vampire, orc, dragon
class nemico:
    def __init__(self, tipo, hp, danno):
        self.tipo = tipo
        self.hp = hp
        self.danno = danno

    def rimuovi(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.hp = 0
            print()
            print(f"You defeated: {self.tipo}!")
            print()

    def attacca(self, player):
        print(f"You took {self.danno} damage from the {self.tipo}!")
        return player.rimuovi(self.danno)

nemico_goblin = nemico("Goblin", 25, 5)
nemico_zombie = nemico("Zombie", 50, 10)
nemico_vampiro = nemico("Vampiro", 75, 15)
nemico_orco = nemico("Orco", 100, 20)
nemico_drago = nemico("Drago", 200, 25)

#LOOT EXTRACTION
def estrai_loot(loot_dizionario):
    numero = random.randint(1, 100)
    soglia = 0
    for oggetto, percentuale in loot_dizionario.items():
        soglia += percentuale
        if numero <= soglia:
            return oggetto
    return None

#PLAYER INPUT
printsys("Welcome to CyberFantasy!")
time.sleep(0.5)
input("Premi Enter per iniziare...")
print()
print("You are a brave adventurer in a world full of monsters and dangers.")
time.sleep(4)
print("Your goal is to survive and defeat the dragon you will encounter along the way.")
time.sleep(4)
print()
input("Press Enter to continue...")
print()
print("You are facing the first monster, a Goblin!")
time.sleep(3.5)
print("Luckily, you have a knife and a Tiny potion!")
print()
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')
printsys("What are you going to do?")
time.sleep(1.5)

player.inventario = inventario()
player.inventario.aggiungi(armi_coltello, messaggio=False)
player.inventario.aggiungi(pozione_tiny, messaggio=False)

lista_nemici = [nemico_goblin, nemico_zombie, nemico_vampiro, nemico_orco, nemico_drago]
indice_nemico = 0


while True:
    if player.hp <= 0:
        break

    printsys(f"\nLa tua salute attuale è: {player.hp} HP")
    print()
    printsys("Choose an action:")
    printsys("1. Attack the enemy")
    printsys("2. Use a potion")
    printsys("3. Check the inventory")
    printsys("4. Exit the game")
    print()

    scelta = input("Enter the number of the action you want to perform: ")

    if scelta == "1":
        if lista_nemici[indice_nemico].hp > 0:
            armi_possedute = [item for item in player.inventario.items if isinstance(item, Armi)]
            arma_migliore = max(armi_possedute, key=lambda arma: arma.danno)
            arma_migliore.attacca(lista_nemici[indice_nemico])
            if lista_nemici[indice_nemico].hp > 0:
                lista_nemici[indice_nemico].attacca(player)
            else:
                indice_nemico += 1

                if lista_nemici[indice_nemico - 1] == nemico_drago:
                    premio_finale.aggiungi(player)
                else:
                    loot_pozione = estrai_loot(lista_loot_pozioni[indice_nemico - 1])
                    if loot_pozione is not None:
                        player.inventario.aggiungi(loot_pozione)
                    loot_arma = estrai_loot(lista_loot_armi[indice_nemico - 1])
                    if loot_arma is not None:
                        player.inventario.aggiungi(loot_arma)

                if indice_nemico < len(lista_nemici):
                    print()
                    print(f"You have moved on to the next enemy: {lista_nemici[indice_nemico].tipo}!")
                    print()
                else:
                    print()
                    print("You defeated the dragon! Congratulations!")
                    print()
                    time.sleep(1)
                    printsys("Thank you for playing CyberFantasy!")
                    print()
                    time.sleep(1)
                    input("Press Enter to exit...")
                    break
        else:
            print("You defeated it! On to the next enemy!")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

    elif scelta == "2":
        pozioni_possedute = [item for item in player.inventario.items if isinstance(item, Pozione)]
        if len(pozioni_possedute) == 0:
            print("You have no potions in your inventory!")
        else:
            for i, pozione in enumerate(pozioni_possedute):
                print(f"{i + 1}. {pozione.tipo}")
            scelta_pozione = input("Which potion do you want to use? (number): ")
            try:
                numero = int(scelta_pozione)
            except ValueError:
                print("You must enter a number!")
                numero = -1
            if numero >= 1 and numero <= len(pozioni_possedute):
                pozione_scelta = pozioni_possedute[numero - 1]
                player.inventario.usa_pozione(pozione_scelta, player)
            else:
                print("Invalid number!")

    elif scelta == "3":
        print("Your inventory contains:")
        for item in player.inventario.items:
            print(f"- {item.tipo}")
        input("Press Enter to continue...")

    elif scelta == "4":
        printsys("Are you sure you want to leave the game? (yes/no)")
        conferma = input()
        if conferma.lower() == "yes":
            printsys("Thank you for playing CyberFantasy!")
            time.sleep(1)
            printsys("See you next time!")
            time.sleep(0.8)
            break
        elif conferma.lower() == "no":
            printsys("Let's keep playing!")
            print()
            input("Press Enter to continue...")
        else:
            print("Invalid option.")

    else:
        print("Invalid choice. Try again.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
