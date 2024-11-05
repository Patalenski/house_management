from repositories.flat_repository import FlatRepository
from models.flat import Flat
from typing import List, Optional

class FlatController:
    def __init__(self, flat_repo: FlatRepository):
        self.flat_repo = flat_repo

    def add_flat(self, flat_number: int, floor: int, room_type: str) -> Flat:
        flat = Flat(
            flat_number=flat_number,
            floor=floor,
            room_type=room_type
        )
        self.flat_repo.add_flat(flat)
        return flat

    def delete_flat(self, flat_number: int) -> bool:
        return self.flat_repo.delete_flat(flat_number)

    def get_all_flats(self) -> List[Flat]:
        return self.flat_repo.flats

    def get_flat(self, flat_number: int) -> Optional[Flat]:
        return self.flat_repo.get_flat_by_number(flat_number)

    def get_flats_by_floor(self, floor: int) -> List[Flat]:
        return [flat for flat in self.flat_repo.flats if flat.floor == floor]

    def get_flats_by_type(self, room_type: str) -> List[Flat]:
        return [flat for flat in self.flat_repo.flats if flat.room_type.lower() == room_type.lower()]
