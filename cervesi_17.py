class Insegnante:
    def __init__(self, nome, cognome, strumento):
        self.nome = nome
        self.cognome = cognome
        self.strumento = strumento
        self.studenti = []

    def aggiungiStudente(self, studente):
        if studente not in self.studenti:
            self.studenti.append(studente)

    def __str__(self):
        return f"Insegnante {self.nome} {self.cognome}, Strumento: {self.strumento}"

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.insegnante = None
        self.corsi = []

    def setInsegnante(self, insegnante):
        self.insegnante = insegnante
        insegnante.aggiungiStudente(self)

    def iscriviCorso(self, corso):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.aggiungiStudente(self)

    def __str__(self):
        corsi_nomi = ", ".join([corso.nome for corso in self.corsi])
        return f"Studente {self.nome} {self.cognome}, Insegnante: {self.insegnante.nome} {self.insegnante.cognome}, Corsi: {corsi_nomi}"

class Corso:
    def __init__(self, nome, durata):
        self.nome = nome
        self.durata = durata
        self.studenti = []

    def aggiungiStudente(self, studente):
        if studente not in self.studenti:
            self.studenti.append(studente)

    def __str__(self):
        return f"Corso: {self.nome}, Durata: {self.durata}"

def main():
    # Creazione degli insegnanti
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")

    # Creazione degli studenti
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")

    # Assegnazione degli insegnanti agli studenti
    studente1.setInsegnante(insegnante1)
    studente2.setInsegnante(insegnante2)

    # Creazione dei corsi
    corso1 = Corso