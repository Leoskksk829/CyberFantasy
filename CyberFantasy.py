import time
import random
import os
import sys

#EFFETTO SCRITTA 
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
        print("curato!")
        print ()

player = Player_Health(100)

#pozioni
class Pozione:
    def __init__(self, tipo, hp):
        self.tipo = tipo
        self.hp = hp

    def usa(self, player, messaggio=True):
        player.aggiungi(self.hp)
        if messaggio:
            print(f"Hai usato una {self.tipo} e hai recuperato {self.hp} HP!")

pozione_MASTER = Pozione("Master", 100)
pozione_big = Pozione("Master", 75)
pozione_middle = Pozione("Middle", 50)
pozione_small = Pozione("Small", 25)
pozione_tiny = Pozione("Tiny", 10)

#armi
class Armi:
    def __init__(self, tipo, danno):
        self.tipo = tipo
        self.danno = danno

    def attacca(self, nemico):
        print()
        print(f"Hai attaccato il {nemico.tipo} e hai inflitto {self.danno} danni!")
        return nemico.rimuovi(self.danno)

armi_spadaInfuocata = Armi("Spada Infuocata", 100)
armi_martello = Armi("Martello", 35)
armi_spada = Armi("Spada", 20)
armi_coltello = Armi("Coltello", 5)
armi_ascia = Armi("Ascia", 40)

#PREMIO FINALE
class premio:
    def __init__(self, tipo, valore=100):
        self.tipo = tipo
        self.valore = valore

    def aggiungi(self, player):
        print()
        printsys(f"Hai ottenuto il premio finale: {self.tipo}!")
        print()
        return player.aggiungi(self.valore)

premio_finale = premio("Cuore di Drago", 100)

#LOOT NEMICI
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

#INVENTARIO
class inventario:
    def __init__(self):
        self.items = []

    def aggiungi(self, item, messaggio=True):
        self.items.append(item)
        if messaggio:
            if isinstance(item, Pozione):
                print()
                print(f"[ ! ] Aggiunto {item.tipo} all'inventario! e ti può curare di: {item.hp} HP")
            else:
                print(f"[ ! ]Aggiunto {item.tipo} all'inventario! e ti può aiutare infliggendo: {item.danno} Danni")
                print ("")

    def rimuovi(self, item, messaggio=True):
        if item in self.items:
            self.items.remove(item)
            if messaggio:
                print(f"{item.tipo} rimosso dall'inventario.")
        else:
            if messaggio:
                print()
                print(f"{item.tipo} non è presente nell'inventario.")
                print()

    def usa_pozione(self, pozione, player, messaggio=True):
        if pozione in self.items:
            pozione.usa(player, messaggio=messaggio)
            self.rimuovi(pozione, messaggio=messaggio)
        else:
            if messaggio:
                print()
                print(f"{pozione} non è presente nell'inventario.")
                print()


#mostri: goblin, zombie, vampiro, orco, drago
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
            print(f"Hai sconfitto: {self.tipo}!")
            print()

    def attacca(self, player):
        print(f"Hai subito {self.danno} danni dal {self.tipo}!")
        return player.rimuovi(self.danno)

nemico_goblin = nemico("Goblin", 25, 5)
nemico_zombie = nemico("Zombie", 50, 10)
nemico_vampiro = nemico("Vampiro", 75, 15)
nemico_orco = nemico("Orco", 100, 20)
nemico_drago = nemico("Drago", 200, 25)

#ESTRAZIONE LOOT
def estrai_loot(loot_dizionario):
    numero = random.randint(1, 100)
    soglia = 0
    for oggetto, percentuale in loot_dizionario.items():
        soglia += percentuale
        if numero <= soglia:
            return oggetto
    return None

#INPUT GIOCATORE
printsys("Benvenuto in CyberFantasy!")
time.sleep(0.5)
input("Premi Enter per iniziare...")
print()
print("Sei un coraggioso avventuriero che si trova in un mondo pieno di mostri e pericoli.")
time.sleep(4)
print("Il tuo obiettivo è sopravvivere e sconfiggere il drago che incontrerai lungo il cammino.")
time.sleep(4)
print()
input("Premi Enter per continuare...")
print()
print("sei davanti al primo mostro, un Goblin!")
time.sleep(3.5)
print("per fortuna hai un coltello e una pozione tiny!")
print()
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')
printsys("cosa hai intenzione di fare?")
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
    printsys("Scegli un'azione:")
    printsys("1. Attacca il nemico")
    printsys("2. Usa una pozione")
    printsys("3. Controlla l'inventario")
    printsys("4. Esci dal gioco")
    print()

    scelta = input("Inserisci il numero dell'azione che vuoi compiere: ")

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
                    print(f"Sei passato al prossimo nemico: {lista_nemici[indice_nemico].tipo}!")
                    print()
                else:
                    print()
                    print("Hai sconfitto il drago! Complimenti!")
                    print()
                    time.sleep(1)
                    printsys("Grazie per aver giocato a CyberFantasy!")
                    print()
                    time.sleep(1)
                    input("Premi Enter per uscire...")
                    break
        else:
            print("l'hai sconfitto! al prossimo nemico!")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

    elif scelta == "2":
        pozioni_possedute = [item for item in player.inventario.items if isinstance(item, Pozione)]
        if len(pozioni_possedute) == 0:
            print("Non hai pozioni nell'inventario!")
        else:
            for i, pozione in enumerate(pozioni_possedute):
                print(f"{i + 1}. {pozione.tipo}")
            scelta_pozione = input("Quale pozione vuoi usare? (numero): ")
            try:
                numero = int(scelta_pozione)
            except ValueError:
                print("Devi scrivere un numero!")
                numero = -1
            if numero >= 1 and numero <= len(pozioni_possedute):
                pozione_scelta = pozioni_possedute[numero - 1]
                player.inventario.usa_pozione(pozione_scelta, player)
            else:
                print("Numero non valido!")

    elif scelta == "3":
        print("Il tuo inventario contiene:")
        for item in player.inventario.items:
            print(f"- {item.tipo}")
        input("Premi Enter per continuare...")

    elif scelta == "4":
        printsys("sei sicuro di voler lasciare il gioco? (sì/no)")
        conferma = input()
        if conferma.lower() == "sì":
            printsys("Grazie per aver giocato a CyberFantasy!")
            time.sleep(1)
            printsys("Alla prossima!")
            time.sleep(0.8)
            break
        elif conferma.lower() == "no":
            printsys("Continuiamo a giocare!")
            print()
            input("Premi Enter per continuare...")
        else:
            print("Opzione non valida.")

    else:
        print("Scelta non valida. Riprova.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
