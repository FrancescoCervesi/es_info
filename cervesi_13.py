class Casa:
    def __init__(self, indirizzo, proprietario):
        self.indirizzo = indirizzo
        self.proprietario = proprietario
        self.stanze = []  # Lista per contenere le stanze associate alla casa

    # Getter e setter per gli attributi di Casa
    def get_indirizzo(self):
        return self.indirizzo

    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def get_proprietario(self):
        return self.proprietario

    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    # Metodo per aggiungere una stanza alla casa
    def aggiungi_stanza(self, stanza):
        self.stanze.append(stanza)

class Stanza:
    def __init__(self, nome, superficie):
        self.nome = nome
        self.superficie = superficie

    # Getter e setter per gli attributi di Stanza
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_superficie(self):
        return self.superficie

    def set_superficie(self, superficie):
        self.superficie = superficie

# Creazione dell'istanza di Casa
casa = Casa("Via delle Rose 15", "Maria Rossi")

# Creazione delle istanze di Stanza
soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

# Aggiunta delle stanze alla casa
casa.aggiungi_stanza(soggiorno)
casa.aggiungi_stanza(cucina)
casa.aggiungi_stanza(camera)

# Verifica dell'associazione
print(f"Casa di {casa.proprietario} situata in {casa.indirizzo} contiene le seguenti stanze:")
for stanza in casa.stanze:
    print(f"- {stanza.nome} ({stanza.superficie} mq)")
