from repositories.tenant_repository import TenantRepository
from models.tenant import Tenant
from typing import List, Optional

class TenantController:
    def __init__(self, tenant_repo: TenantRepository):
        self.tenant_repo = tenant_repo
        self.next_id = self._get_next_id()

    def _get_next_id(self) -> int:
        if not self.tenant_repo.tenants:
            return 1
        return max(tenant.tenant_id for tenant in self.tenant_repo.tenants) + 1

    def add_tenant(self, name: str, age: int, contact_number: str) -> Tenant:
        tenant = Tenant(
            tenant_id=self.next_id,
            name=name,
            age=age,
            contact_number=contact_number
        )
        self.tenant_repo.add_tenant(tenant)
        self.next_id += 1
        return tenant

    def delete_tenant(self, tenant_id: int) -> bool:
        return self.tenant_repo.delete_tenant(tenant_id)

    def get_all_tenants(self) -> List[Tenant]:
        return self.tenant_repo.tenants

    def get_tenant(self, tenant_id: int) -> Optional[Tenant]:
        return self.tenant_repo.get_tenant_by_id(tenant_id)
