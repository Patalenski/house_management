from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Tenant:
    tenant_id: int
    name: str
    age: int
    contact_number: str
    flat_number: Optional[int] = None  # Assigned flat number
