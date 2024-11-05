from dataclasses import dataclass, field
from typing import List

@dataclass
class Flat:
    flat_number: int
    floor: int
    room_type: str  # e.g., '1-room', '2-room', etc.
    tenants: List[int] = field(default_factory=list)  # List of tenant_ids
