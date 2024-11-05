import pytest
from models.tenant import Tenant
from models.flat import Flat
from repositories.tenant_repository import TenantRepository
from repositories.flat_repository import FlatRepository
from controllers.assignment_controller import AssignmentController

@pytest.fixture
def tenant_repo():
    repo = TenantRepository('test_tenants.json')
    repo.tenants = []
    repo.save()
    yield repo
    import os
    if os.path.exists('test_tenants.json'):
        os.remove('test_tenants.json')

@pytest.fixture
def flat_repo():
    repo = FlatRepository('test_flats.json')
    repo.flats = []
    repo.save()
    yield repo
    import os
    if os.path.exists('test_flats.json'):
        os.remove('test_flats.json')

def test_assign_tenant_to_flat(tenant_repo, flat_repo):
    tenant = Tenant(tenant_id=1, name='John Doe', age=30, contact_number='1234567890')
    flat = Flat(flat_number=101, floor=1, room_type='1-room')
    tenant_repo.add_tenant(tenant)
    flat_repo.add_flat(flat)

    controller = AssignmentController(tenant_repo, flat_repo)
    assert controller.assign_tenant_to_flat(1, 101) == True
    assert tenant_repo.get_tenant_by_id(1).flat_number == 101
    assert 1 in flat_repo.get_flat_by_number(101).tenants

def test_unassign_tenant_from_flat(tenant_repo, flat_repo):
    tenant = Tenant(tenant_id=1, name='John Doe', age=30, contact_number='1234567890', flat_number=101)
    flat = Flat(flat_number=101, floor=1, room_type='1-room', tenants=[1])
    tenant_repo.add_tenant(tenant)
    flat_repo.add_flat(flat)

    controller = AssignmentController(tenant_repo, flat_repo)
    assert controller.unassign_tenant_from_flat(1) == True
    assert tenant_repo.get_tenant_by_id(1).flat_number is None
    assert 1 not in flat_repo.get_flat_by_number(101).tenants
