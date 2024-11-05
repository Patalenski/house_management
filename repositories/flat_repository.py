import json
from typing import List, Optional
from models.flat import Flat

class FlatRepository:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.flats: List[Flat] = []
        self.load()

    def add_flat(self, flat: Flat):
        self.flats.append(flat)
        self.save()

    def delete_flat(self, flat_number: int) -> bool:
        flat = self.get_flat_by_number(flat_number)
        if flat:
            self.flats.remove(flat)
            self.save()
            return True
        return False

    def get_flat_by_number(self, flat_number: int) -> Optional[Flat]:
        for flat in self.flats:
            if flat.flat_number == flat_number:
                return flat
        return None

    def load(self):
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                self.flats = [Flat(**flat) for flat in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.flats = []

    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump([flat.__dict__ for flat in self.flats], file, indent=4)
