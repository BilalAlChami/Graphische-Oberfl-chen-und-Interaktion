import tkinter as tk  # für die Erstellung von GUI
from tkcalendar import DateEntry  # für ein Datumsauswahl-Widget
from tkinter import messagebox, filedialog  # für Dialogfenster
from datetime import datetime, timedelta
from Patient import Patient
from fpdf import FPDF # für die Erstellung von PDF-Dokumenten

class BlutzuckerDokumentationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blutzucker Dokumentation")
        self.root.geometry("350x350")

        # Menüleiste
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Datei-Menü
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Beenden", command=self.root.destroy)
        menubar.add_cascade(label="Datei", menu=file_menu)

        # Maßeinheit-Menü
        measurement_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Maßeinheit festlegen", menu=measurement_menu)

        # Variable für die Maßeinheit
        self.masseinheit = tk.StringVar()
        self.masseinheit.set("mg/dl")  # Standardwert

        # Optionen für Radiobuttons
        options = ["mg/dl", "mmol/l"]

        # Radiobuttons für die Maßeinheit
        for i, option in enumerate(options):
            measurement_menu.add_radiobutton(label=option, variable=self.masseinheit, value=option)

        # Patienteninitialisierung
        self.patient = None

        tk.Label(root, text="Name*:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Vorname*:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(root, text="Geburtstag*:").grid(row=2, column=0, padx=5, pady=5)

        # Eingabefelder für Patientendaten
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.vorname_entry = tk.Entry(root)
        self.vorname_entry.grid(row=1, column=1, padx=5, pady=5)
        self.geburtstag_entry = DateEntry(root, date_pattern='dd.MM.yyyy')
        self.geburtstag_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Blutzuckerwert*:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(root, text="Mahlzeitengröße:").grid(row=4, column=0, padx=5, pady=5)
        tk.Label(root, text="Medikation:").grid(row=5, column=0, padx=5, pady=5)
        tk.Label(root, text="Aktivitäten:").grid(row=6, column=0, padx=5, pady=5)

        # Eingabefelder für Blutzuckerdaten
        self.blutzuckerwert_entry = tk.Entry(root)
        self.blutzuckerwert_entry.grid(row=3, column=1, padx=5, pady=5)
        self.mahlzeitengroesse_entry = tk.Entry(root)
        self.mahlzeitengroesse_entry.grid(row=4, column=1, padx=5, pady=5)
        self.medikation_entry = tk.Entry(root)
        self.medikation_entry.grid(row=5, column=1, padx=5, pady=5)
        self.aktivitaeten_entry = tk.Entry(root)
        self.aktivitaeten_entry.grid(row=6, column=1, padx=5, pady=5)

        # Buttons für Aktionen
        tk.Button(root, text="Dokumentieren", command=self.dokumentiere_blutzucker).grid(row=7, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Auswerten", command=self.auswerten_und_exportieren).grid(row=11, column=15, columnspan=2, pady=5)
        tk.Button(root, text="Tabelle anzeigen", command=self.show_table).grid(row=12, column=15, columnspan=2, pady=5)


    def set_measurement_unit(self, unit):
        self.masseinheit.set(unit)
        messagebox.showinfo("Maßeinheit festgelegt", f"Maßeinheit wurde auf {unit} festgelegt.")

    def update_measurement_unit(self):
        messagebox.showinfo("Maßeinheit festgelegt", f"Maßeinheit wurde auf {self.masseinheit.get()} festgelegt.")

    def dokumentiere_blutzucker(self):
        name = self.name_entry.get()
        vorname = self.vorname_entry.get()
        geburtstag = self.geburtstag_entry.get()

        if not name or not vorname or not geburtstag:
            messagebox.showwarning("Fehler", "Bitte füllen Sie alle Felder aus.")
            return

        blutzuckerwert = self.blutzuckerwert_entry.get()
        mahlzeitengroesse = self.mahlzeitengroesse_entry.get()
        medikation = self.medikation_entry.get()
        aktivitaeten = self.aktivitaeten_entry.get()

        if not blutzuckerwert:
            messagebox.showwarning("Fehler", "Bitte geben Sie einen Blutzuckerwert ein.")
            return

        # Umrechnungsfaktor je nach Maßeinheit
        conversion_factor = 1.0
        if self.masseinheit.get() == "mmol/l":
            conversion_factor = 0.0555

        blutzuckerwert = float(blutzuckerwert) * conversion_factor

        timestamp = datetime.now()
        if self.patient is None:
            self.patient = Patient(name, vorname, geburtstag)

        self.patient.add_blutzuckerwert(blutzuckerwert, timestamp, mahlzeitengroesse, medikation, aktivitaeten)

        messagebox.showinfo("Erfolg", "Blutzuckerwerte erfolgreich dokumentiert.")

    def auswerten_und_exportieren(self):
        if not self.patient:
            messagebox.showwarning("Fehler", "Bitte dokumentieren Sie zuerst Blutzuckerwerte.")
            return

        last_31_days_data = self.patient.get_last_31_days_data()

        if not last_31_days_data:
            messagebox.showwarning("Fehler", "Es liegen keine Daten der letzten 31 Tage vor.")
            return

        self.export_to_pdf(last_31_days_data)

    def export_to_pdf(self, data):

        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not filename:
	        return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=12)

        pdf.cell(200, 10, txt="Blutzuckerwerte der letzten 31 Tage", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)

        headers = ["Zeitstempel", "Blutzuckerwert", "Status"]
        col_widths = [60, 60, 30]
        #for header, width in zip(headers, col_widths): alle spalten
        for header, width in zip(headers[:2], col_widths[:2] ):
	        pdf.cell(width, 10, txt=header, border=1, align='C')
        pdf.ln()
        umrechn_faktor = 1.0
        if self.masseinheit.get() == "mmol/l":
            umrechn_faktor = 18.0182

        for entry in data:
	        timestamp_str = entry["timestamp"].strftime("%d-%m-%Y %H:%M:%S")
	        wert = float(entry["wert"])
	        status = self.get_status(wert)


	        pdf.cell(col_widths[0], 10, txt=timestamp_str, border=1, align='C')
	        pdf.cell(col_widths[1], 10, txt=f"{wert * umrechn_faktor:.2f} {self.masseinheit.get()}", border=1, align='C')


	        # Set background color based on status
	        if status == "Rot":
		        pdf.set_fill_color(255, 0, 0)
	        elif status == "Grün":
		        pdf.set_fill_color(0, 255, 0)
	        elif status == "Gelb":
		        pdf.set_fill_color(255, 255, 0)
	        else:
		        pdf.set_fill_color(255, 255, 255)  # Default color is white

	        pdf.cell(col_widths[2], 10, border=1, fill=True)
	        pdf.ln()

        pdf.output(filename)
        messagebox.showinfo("Erfolg", f"Daten erfolgreich als PDF exportiert: {filename}")

    def show_table(self):
        if not self.patient or not self.patient.blutzuckerwerte:
            messagebox.showwarning("Fehler", "Es liegen keine Daten vor.")
            return

        table = tk.Toplevel(self.root)
        table.title("Blutzuckerwerte Tabelle")

        headers = ["Name", "Vorname", "Geburtstag", "Blutzuckerwert (" + self.masseinheit.get() + ")",
                   "Mahlzeitengröße", "Medikation", "Aktivitäten", "Status"]

        for col, header in enumerate(headers):
            tk.Label(table, text=header, relief=tk.SOLID, width=20).grid(row=0, column=col)

        for row, entry in enumerate(self.patient.blutzuckerwerte, start=1):
            name_label = tk.Label(table, text=self.patient.name, relief=tk.SOLID, width=20)
            name_label.grid(row=row, column=0)

            vorname_label = tk.Label(table, text=self.patient.vorname, relief=tk.SOLID, width=20)
            vorname_label.grid(row=row, column=1)

            geburtstag_label = tk.Label(table, text=self.patient.geburtstag, relief=tk.SOLID, width=20)
            geburtstag_label.grid(row=row, column=2)

            # Umrechnungsfaktor je nach Maßeinheit
            conversion_factor = 1.0
            if self.masseinheit.get() == "mmol/l":
                conversion_factor = 18.0182

            wert_label = tk.Label(table, text=f"{entry['wert'] * conversion_factor:.2f}", relief=tk.SOLID,
                                  width=20)
            wert_label.grid(row=row, column=3)

            mahlzeitengroesse_label = tk.Label(table, text=entry["mahlzeitengroesse"], relief=tk.SOLID,
                                               width=20)
            mahlzeitengroesse_label.grid(row=row, column=4)

            medikation_label = tk.Label(table, text=entry["medikation"], relief=tk.SOLID, width=20)
            medikation_label.grid(row=row, column=5)

            aktivitaeten_label = tk.Label(table, text=entry["aktivitaeten"], relief=tk.SOLID, width=20)
            aktivitaeten_label.grid(row=row, column=6)

            status = self.get_status(entry["wert"])
            status_label = tk.Label(table, text="", relief=tk.SOLID, width=20)

            # Set background color based on status
            if status == "Rot":
                status_label.configure(background="red")
            elif status == "Grün":
                status_label.configure(background="green")
            elif status == "Gelb":
                status_label.configure(background="yellow")

            status_label.grid(row=row, column=7)

    def get_status(self, wert):
        wert = float(wert)
        if wert < 70:
            return "Rot"
        elif 90 <= wert <= 125:
            return "Grün"
        elif wert > 160:
            return "Gelb"
        else:
            return ""