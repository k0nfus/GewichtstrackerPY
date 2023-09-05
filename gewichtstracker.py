import sqlite3

# Verbindung zur SQLite-Datenbank herstellen oder erstellen
conn = sqlite3.connect("gewicht.db")

# Ein Cursor-Objekt erstellen, um SQL-Operationen auszuführen
cursor = conn.cursor()

# Tabelle "gewicht" erstellen, falls sie nicht existiert
cursor.execute('''CREATE TABLE IF NOT EXISTS gewicht (
                    id INTEGER PRIMARY KEY,
                    gewicht TEXT NOT NULL,
                    datum DATE
                )''')

# Änderungen in der Datenbank speichern
conn.commit()

# Funktion zum Hinzufügen eines Eintrags in die Datenbank
def eintrag_hinzufuegen(gewicht, datum):
    cursor.execute("INSERT INTO gewicht (gewicht, datum) VALUES (?, ?)",
                   (gewicht, datum))
    conn.commit()

# Funktion zum Anzeigen aller Einträge in der Datenbank
def eintraege_anzeigen():
    cursor.execute("SELECT * FROM gewicht")
    eintraege = cursor.fetchall()
    for eintrag in eintraege:
        print(eintrag)

# Funktion zum Aktualisieren eines Eintrags in der Datenbank
def eintrag_aktualisieren(id, gewicht, datum):
    cursor.execute("UPDATE gewicht SET gewicht=?, datum=? WHERE id=?",
                   (gewicht, datum, id))
    conn.commit()

# Funktion zum Löschen eines Eintrags aus der Datenbank
def eintrag_loeschen(id):
    cursor.execute("DELETE FROM gewicht WHERE id=?", (id,))
    conn.commit()

# Funktion zum Anzeigen des Hauptmenüs
def menue_anzeigen():
    print("\nGewichtstrackerPY:")
    print("C - Eintrag hinzufügen")
    print("R - Einträge anzeigen")
    print("U - Eintrag aktualisieren")
    print("D - Eintrag löschen")
    print("X - Programm beenden")

# Hauptprogrammschleife
while True:
    menue_anzeigen()
    auswahl = input("\nBitte wählen Sie eine Option (C/R/U/D/X): ")
    
    if auswahl == "C" or auswahl == "c":
        gewicht = input("Gewicht (123.45): ")
        datum = input("Datum (JJJJ-MM-TT): ")
        eintrag_hinzufuegen(gewicht, datum)
        print("\nEintrag hinzugefügt.")
    elif auswahl == "R" or auswahl == "r":
        eintraege_anzeigen()
    elif auswahl == "U" or auswahl == "u":
        id = input("Geben Sie die ID des zu aktualisierenden Eintrags ein: ")
        gewicht = input("Gewicht (123.45): ")
        datum = input("Datum (JJJJ-MM-TT): ")
        eintrag_aktualisieren(id, gewicht, datum)
        print("\nEintrag aktualisiert.")
    elif auswahl == "D" or auswahl == "d":
        id = input("Geben Sie die ID des zu löschenden Eintrags ein: ")
        eintrag_loeschen(id)
        print("\nEintrag gelöscht.")
    elif auswahl == "X" or auswahl == "x":
        print("\nProgramm beendet.")
        break
    else:
        print("\nUngültige Auswahl. Bitte wählen Sie eine gültige Option (Möglich sind: \"C\", \"R\", \"U\", \"D\" und \"X\"): ")
