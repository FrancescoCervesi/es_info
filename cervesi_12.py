class Auto:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        self.motore = None  # Attributo per mantenere il riferimento al motore

    # Getter e setter per gli attributi di Auto
    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modello(self):
        return self.modello

    def set_modello(self, modello):
        self.modello = modello

    # Metodo per associare un motore all'auto
    def associa_motore(self, motore):
        self.motore = motore
        motore.associa_auto(self)  # Associa l'auto al motore (associazione bi-direzionale)

class Motore:
    def __init__(self, numero_seriale, tipo):
        self.numero_seriale = numero_seriale
        self.tipo = tipo
        self.auto = None  # Attributo per mantenere il riferimento all'auto

    # Getter e setter per gli attributi di Motore
    def get_numero_seriale(self):
        return self.numero_seriale

    def set_numero_seriale(self, numero_seriale):
        self.numero_seriale = numero_seriale

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    # Metodo per associare un'auto al motore
    def associa_auto(self, auto):
        self.auto = auto

# Creazione delle istanze
auto1 = Auto("Fiat", "500")
motore1 = Motore("ENG123456", "Benzina")

# Associazione tra auto e motore
auto1.associa_motore(motore1)

# Verifica dell'associazione
print(f"{auto1.marca} {auto1.modello} ha il motore: {auto1.motore.numero_seriale}")
print(f"Il motore {motore1.numero_seriale} appartiene a: {motore1.auto.marca} {motore1.auto.modello}")
