# Codice Python per la realizzazione del Progetto di Metodi Matematici e Statistici
# Davide Casano, matricola n. X81000862
# Progetto MMS: "Il banco vince sempre"

# Lo scopo di questo esperimento è rispondere a una semplice domanda: "se una persona inizia con €10.000
# e gioca a questo gioco un "n" numero di volte e piazza una scommessa di €100 in ogni gioco, in media,
# con quanti soldi si terminerebbe?".

# Simuliamo diversi scenari in Python per visualizzare e commentare i diversi risultati.

# Importiamo le librerie necessarie:
import random
import matplotlib.pyplot as plt

# Creiamo una funzione per simulare l'uscita del colore.
# Se il numero è compreso tra 0 e 18, il casinò vince.
# Se il numero è compreso tra 19 e 36, il giocatore vince.

def roulette():
    
    ball = random.randint(0,36)
    
    if ball <=18:
        return False
    elif ball >18 & ball <=36:
        return True

# 4. Definiamo una funzione per il gioco che richiede 3 argomenti
# 1) total_funds = denaro totale in mano con cui il giocatore inizia
# 2) wager_amount = l'importo della puntata ogni volta che il giocatore gioca
# 3) total_games = numero di volte che il giocatore ha scommesso sul gioco

def play(total_funds, wager_amount, total_plays):
    
    # Creiamo una lista vuota per :
    # 1.Play_number and 
    # 2.Funds available
    # 3.Final Fund
    Play_num = []
    Funds = []
# Partiamo con il numero 1
    play = 1
    
# Se il numero di giocate è minore del numero massimo che abbiamo stabilito
    while play < total_plays:

        # Se vince il giocatore
        if roulette():
            # Aggiungi i soldi al budget attuale
            total_funds = total_funds + wager_amount
            # Aumenta il numero di partite
            Play_num.append(play)
            # Aggiorna il nuovo budget attuale
            Funds.append(total_funds)

        # Se vince il banco
        else:
            # Sottrai i soldi al budget attuale
            total_funds = total_funds - wager_amount 
            # Aumenta il numero di partite
            Play_num.append(play)
            # Aggiorna il nuovo budget attuale
            Funds.append(total_funds)
            
        # Aumenta il numero di giocate

        play = play + 1
        
    # Resoconto dei fondi totali
    plt.plot(Play_num,Funds)
    Final_funds.append(Funds[-1])
    return(Final_funds)

# Chiamiamo la funzione per simulare le giocate e calcoliamo i fondi del giocatore rimanenti dopo tutte le scommesse.
# Inizializziamo la variabile x a 1
x=1
# Creiamo la lista per calcolare i fondi totali
Final_funds= []
while x<=100:
    ending_fund = play(10000,100,5)
    x=x+1
# Tracciamo la retta del "Saldo del conto" vs "Numero di giocate"
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')
plt.show()
# Stampiamo con quanti soldi il giocatore termina
print("Il giocatore ha iniziato con €10.000 e ha terminato con €" + str(sum(ending_fund)/len(ending_fund)))

# Visualizziamo 5 diversi scenari utilizzando i seguenti grafici. In ogni scenario, Tom scommette un numero n di volte.

ending_fund = play(10000,100,5)

Asse x: il numero di scommesse che Tom effettua
Asse y: saldo del conto di Tom dopo ogni scommessa

Ogni grafico mostra il saldo del conto di Tom mentre continua a giocare. Per scoprirlo, calcoliamo la media del saldo dalle 100 diverse simulazioni.


# Scenario n.1 -> Numero di giocate: 5
# Chiamiamo la funzione per simulare le giocate e calcoliamo i fondi del giocatore rimanenti dopo tutte le scommesse.
# Inizializziamo la variabile x a 1
x=1
# Creiamo la lista per calcolare i fondi totali
Final_funds= []
while x<=100:
    ending_fund = play(10000,100,5)
    x=x+1
# Tracciamo la retta del "Saldo del conto" vs "Numero di giocate"
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')
plt.show()
# Stampiamo con quanti soldi il giocatore termina
print("Il giocatore ha iniziato con €10.000 e ha terminato con €" + str(sum(ending_fund)/len(ending_fund)))

# Scenario n.2 -> Numero di giocate: 10
# Chiamiamo la funzione per simulare le giocate e calcoliamo i fondi del giocatore rimanenti dopo tutte le scommesse.
# Inizializziamo la variabile x a 1
x=1
# Creiamo la lista per calcolare i fondi totali
Final_funds= []
while x<=100:
    ending_fund = play(10000,100,10)
    x=x+1
# Tracciamo la retta del "Saldo del conto" vs "Numero di giocate"
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')
plt.show()
# Stampiamo con quanti soldi il giocatore termina
print("Il giocatore ha iniziato con €10.000 e ha terminato con €" + str(sum(ending_fund)/len(ending_fund)))

# Scenario n.3 -> Numero di giocate: 100
# Chiamiamo la funzione per simulare le giocate e calcoliamo i fondi del giocatore rimanenti dopo tutte le scommesse.
# Inizializziamo la variabile x a 1
x=1
# Creiamo la lista per calcolare i fondi totali
Final_funds= []
while x<=100:
    ending_fund, total_funds = play(10000,100,100)
    x=x+1
# Tracciamo la retta del "Saldo del conto" vs "Numero di giocate"
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')
plt.show()

# Stampiamo con quanti soldi il giocatore termina e il relativo intervallo di confidenza
print("Il giocatore ha iniziato con €10,000, ha terminato con una media di €" + str(np.mean(total_funds)))

# Stampiamo il grafico
x = np.arange(len(total_funds))
dy = 100
y = total_funds

plt.plot(x, y)
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')

plt.errorbar(x, y, yerr=dy, fmt='', ecolor='green', elinewidth=2, capsize=5, errorevery=15);

# Scenario n.4 -> Numero di giocate: 1000
# Chiamiamo la funzione per simulare le giocate e calcoliamo i fondi del giocatore rimanenti dopo tutte le scommesse.
# Inizializziamo la variabile x a 1
x=1
# Creiamo la lista per calcolare i fondi totali
Final_funds= []
while x<=100:
    ending_fund, total_funds = play(10000,100,1000)
    x=x+1
# Tracciamo la retta del "Saldo del conto" vs "Numero di giocate"
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')
plt.show()

# Stampiamo con quanti soldi il giocatore termina e il relativo intervallo di confidenza
print("Il giocatore ha iniziato con €10,000, ha terminato con una media di €" + str(np.mean(total_funds)))

# Stampiamo i grafici
x = np.arange(len(total_funds))
dy = 350
y = total_funds

plt.plot(x, y)
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')

plt.errorbar(x, y, yerr=dy, fmt='', color="blue", ecolor='red', elinewidth=2, capsize=5, errorevery=100);

# Scenario n.5 -> Numero di giocate: 10000
# Chiamiamo la funzione per simulare le giocate e calcoliamo i fondi del giocatore rimanenti dopo tutte le scommesse.
# Inizializziamo la variabile x a 1
x=1
# Creiamo la lista per calcolare i fondi totali
Final_funds= []
while x<=100:
    ending_fund, total_funds = play(10000,100,10000)
    x=x+1
# Tracciamo la retta del "Saldo del conto" vs "Numero di giocate"
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')
plt.show()

# Stampiamo con quanti soldi il giocatore termina e il relativo intervallo di confidenza
print("Il giocatore ha iniziato con €10,000, ha terminato con una media di €" + str(np.mean(total_funds)))

# Stampiamo il grafico
x = np.arange(len(total_funds))
dy = 1250
y = total_funds

plt.plot(x, y)
plt.ylabel('Saldo del giocatore in €')
plt.xlabel('Numero di giocate')

plt.errorbar(x, y, yerr=dy, fmt='', color="grey", ecolor='black', elinewidth=2, capsize=5, errorevery=1200);
