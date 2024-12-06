```Mermaid
classDiagram
    class Insegnante {
        +String nome
        +String cognome
        +String strumento
        +Studente[] studenti
        +void aggiungiStudente(Studente studente)
    }

    class Studente {
        +String nome
        +String cognome
        +Insegnante insegnante
        +Corso[] corsi
        +void setInsegnante(Insegnante insegnante)
        +void iscriviCorso(Corso corso)
    }

    class Corso {
        +String nome
        +String durata
        +Studente[] studenti
        +void aggiungiStudente(Studente studente)
    }

    Insegnante "1" -- "*" Studente : "Insegna a"
    Studente "*" -- "*" Corso : "Iscritto a"
