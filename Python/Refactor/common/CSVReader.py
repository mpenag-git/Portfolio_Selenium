import csv
import random

class CSV_Reader:

    def __init__(self, name):
        self.filepath = name

    def read_random_row(self):
        data = []
        with open(self.filepath, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    "item": row["item"],
                    "price": float(row["price"]),
                    "rate": float(row["rate"])
                })
        # Selecciona un registro aleatorio
        return random.choice(data)

