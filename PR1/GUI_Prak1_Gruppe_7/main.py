

"""
Author:    Team 7
        - Hussain Alhussain 11148332
        - Bilal Al Chami 11150744
        - Abdulkarim Darwish 11149323
        - Omar Samig 11149405
Anwendungsbeschreibung:     Das Programm ermöglicht die Dokumentation von Blutzuckerwerten, speichert Patientendaten,
                            und bietet Funktionen zur Auswertung und Exportierung von Daten in ein PDF-Format.
                            Die grafische Benutzeroberfläche wurde mit Tkinter erstellt.
Interpreter:    Python 3.10.0
Compiler:   PyCharm 2021.2.2
Zusätzliche Bibliotheken:   fpdf, tkcalendar (pip install fpdf, pip install tkcalendar)
Abgabe:     05.12.2023
Version:    1.0.0

"""
import tkinter as tk # für die Erstellung von GUI
from BlutzuckerDokumentationGUI import BlutzuckerDokumentationGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = BlutzuckerDokumentationGUI(root)
    root.mainloop()
