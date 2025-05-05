# Blutzucker-Dokumentationssystem

## 📋 Kurzbeschreibung  
Diese Anwendung dient der Erfassung und Verwaltung von Blutzuckerwerten verschiedener Patienten. Über eine grafische Benutzeroberfläche (GUI) können Daten einfach eingegeben, angezeigt und gespeichert werden. Das Projekt wurde im Rahmen der Lehrveranstaltung *Graphische Oberflächen und Interaktion* an der Hochschule entwickelt.

---

## 💻 Verwendete Technologien  
- **Programmiersprache**: Python 3  
- **GUI-Toolkit**: Tkinter (in Python integriert)  
- **Modularisierung**: Eigenständige Klassen für Patientendaten (`Patient.py`) und GUI-Logik (`BlutzuckerDokumentationGUI.py`)  
- **Entwicklungsumgebung**: z. B. PyCharm  

---

## 🚀 Anleitung zur lokalen Ausführung  

1. **Repository klonen oder herunterladen**  
   ```bash
   git clone https://github.com/BilalAlChami/Graphische-Oberfl-chen-und-Interaktion
   ```

2. **In das Projektverzeichnis wechseln**  
   ```bash
   cd PR1/GUI_Prak1_Gruppe_7
   ```

3. **Abhängigkeiten installieren**  
   > Es sind keine externen Bibliotheken notwendig – Tkinter ist bei Python standardmäßig enthalten.

4. **Anwendung starten**  
   ```bash
   python main.py
   ```

---

## 📁 Projektstruktur (Auszug)  
```
GUI_Prak1_Gruppe_7/
├── main.py                     # Einstiegspunkt der Anwendung
├── BlutzuckerDokumentationGUI.py # Enthält die GUI-Logik
└── Patient.py                  # Implementiert die Patientenklasse
```

---

## 🛠️ Funktionen  
- Erfassen und Verwalten von Patientendaten  
- Speichern von Blutzuckerwerten mit Datum und Uhrzeit  
- Anzeige der Werte übersichtlich in einer Tabelle  
- Speichern der Daten lokal (z. B. JSON oder CSV)

---

## 📝 Bedienung  
1. Starte die Anwendung mit: `python main.py`  
2. Über die GUI kannst du:  
   - Neue Patienten anlegen  
   - Blutzuckerwerte eingeben  
   - Alle Messwerte anzeigen  
   - Die Daten speichern und erneut laden  

---

> ⚠ Hinweis: Momentan werden die Daten lokal in einer Datei gespeichert (z. B. JSON). Bei Bedarf kann dies später durch eine Datenbank ersetzt werden.

---
