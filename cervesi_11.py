class Ricetta:
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta):
        self.nome = nome
        self.tempo_preparazione = tempo_preparazione
        self.ingredienti = ingredienti
        self.difficolta = difficolta

    
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tempo_preparazione(self):
        return self.tempo_preparazione

    def set_tempo_preparazione(self, tempo):
        self.tempo_preparazione = tempo

    def get_ingredienti(self):
        return self.ingredienti

    def set_ingredienti(self, ingredienti):
        self.ingredienti = ingredienti

    def get_difficolta(self):
        return self.difficolta

    def set_difficolta(self, difficolta):
        self.difficolta = difficolta

   
    def aggiungi_ingrediente(self, ingrediente):
        if ingrediente not in self.ingredienti:
            self.ingredienti.append(ingrediente)

    
    @staticmethod
    def tempo_totale(ricette):
        return sum([ricetta.get_tempo_preparazione() for ricetta in ricette])

    
    @staticmethod
    def verifica_ingredienti(ricette, ingredienti_disponibili):
        ricette_possibili = []
        for ricetta in ricette:
            if all(ingrediente in ingredienti_disponibili for ingrediente in ricetta.get_ingredienti()):
                ricette_possibili.append(ricetta)
        return ricette_possibili

    
    @staticmethod
    def stampa_ricette(ricette):
        for ricetta in ricette:
            print(ricetta)

    
    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"


class Primo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_pasta, sugo):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

    
    def get_tipo_pasta(self):
        return self.tipo_pasta

    def set_tipo_pasta(self, tipo_pasta):
        self.tipo_pasta = tipo_pasta

    def get_sugo(self):
        return self.sugo

    def set_sugo(self, sugo):
        self.sugo = sugo

    
    def __str__(self):
        return f"Primo: {self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta} - Tipo Pasta: {self.tipo_pasta} - Sugo: {self.sugo}"


class Secondo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_carne, cottura):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

   
    def get_tipo_carne(self):
        return self.tipo_carne

    def set_tipo_carne(self, tipo_carne):
        self.tipo_carne = tipo_carne

    def get_cottura(self):
        return self.cottura

    def set_cottura(self, cottura):
        self.cottura = cottura

    
    def __str__(self):
        return f"Secondo: {self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta} - Tipo Carne: {self.tipo_carne} - Cottura: {self.cottura}"


class Dolce(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, zucchero, tipo_dolce):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.zucchero = zucchero
        self.tipo_dolce = tipo_dolce

    
    def get_zucchero(self):
        return self.zucchero

    def set_zucchero(self, zucchero):
        self.zucchero = zucchero

    def get_tipo_dolce(self):
        return self.tipo_dolce

    def set_tipo_dolce(self, tipo_dolce):
        self.tipo_dolce = tipo_dolce

 
    def __str__(self):
        return f"Dolce: {self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta} - Zucchero: {self.zucchero}g - Tipo Dolce: {self.tipo_dolce}"


primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")


ricette = [primo, secondo, dolce]


ingredienti_disponibili = ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"]
ricette_possibili = Ricetta.verifica_ingredienti(ricette, ingredienti_disponibili)
print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")

print("\nInformazioni sulle ricette:")
Ricetta.stampa_ricette(ricette)


