from repositories.tenant_repository import TenantRepository
from repositories.flat_repository import FlatRepository

class AssignmentController:
    def __init__(self, tenant_repo: TenantRepository, flat_repo: FlatRepository):
        self.tenant_repo = tenant_repo
        self.flat_repo = flat_repo

    def assign_tenant_to_flat(self, tenant_id: int, flat_number: int) -> bool:
        tenant = self.tenant_repo.get_tenant_by_id(tenant_id)
        flat = self.flat_repo.get_flat_by_number(flat_number)
        if tenant and flat:
            if tenant.flat_number is not None:
                print(f"Tenant {tenant_id} is already assigned to Flat {tenant.flat_number}.")
                return False
            tenant.flat_number = flat_number
            flat.tenants.append(tenant_id)
            self.tenant_repo.save()
            self.flat_repo.save()
            return True
        return False

    def unassign_tenant_from_flat(self, tenant_id: int) -> bool:
        tenant = self.tenant_repo.get_tenant_by_id(tenant_id)
        if tenant and tenant.flat_number is not None:
            flat = self.flat_repo.get_flat_by_number(tenant.flat_number)
            if flat and tenant_id in flat.tenants:
                flat.tenants.remove(tenant_id)
                tenant.flat_number = None
                self.tenant_repo.save()
                self.flat_repo.save()
                return True
        return False
