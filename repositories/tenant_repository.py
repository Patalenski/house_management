import json
from typing import List, Optional
from models.tenant import Tenant

class TenantRepository:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.tenants: List[Tenant] = []
        self.load()

    def add_tenant(self, tenant: Tenant):
        self.tenants.append(tenant)
        self.save()

    def delete_tenant(self, tenant_id: int) -> bool:
        tenant = self.get_tenant_by_id(tenant_id)
        if tenant:
            self.tenants.remove(tenant)
            self.save()
            return True
        return False

    def get_tenant_by_id(self, tenant_id: int) -> Optional[Tenant]:
        for tenant in self.tenants:
            if tenant.tenant_id == tenant_id:
                return tenant
        return None

    def load(self):
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                self.tenants = [Tenant(**tenant) for tenant in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tenants = []

    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump([tenant.__dict__ for tenant in self.tenants], file, indent=4)
