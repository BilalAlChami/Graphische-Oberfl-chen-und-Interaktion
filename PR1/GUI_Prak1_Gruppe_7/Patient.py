
from datetime import datetime
from datetime import datetime, timedelta


class Patient:
    def __init__(self, name, vorname, geburtstag):
        self.name = name
        self.vorname = vorname
        self.geburtstag = geburtstag
        self.blutzuckerwerte = []

    def add_blutzuckerwert(self, wert, timestamp, mahlzeitengroesse, medikation, aktivitaeten):
        self.blutzuckerwerte.append({
            "wert": wert,
            "timestamp": timestamp,
            "mahlzeitengroesse": mahlzeitengroesse,
            "medikation": medikation,
            "aktivitaeten": aktivitaeten
        })

    def get_last_31_days_data(self):
        today = datetime.now()
        last_31_days = today - timedelta(days=31)
        filtered_data = [entry for entry in self.blutzuckerwerte if entry["timestamp"] >= last_31_days]
        return filtered_data
