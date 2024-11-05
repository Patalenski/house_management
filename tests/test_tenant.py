import unittest
from models.tenant import Tenant
from repositories.tenant_repository import TenantRepository

class TestTenantRepository(unittest.TestCase):
    def setUp(self):
        self.repo = TenantRepository('test_tenants.json')
        # Ensure the repository is empty before each test
        self.repo.tenants = []
        self.repo.save()

    def tearDown(self):
        # Clean up the test file after each test
        import os
        if os.path.exists('test_tenants.json'):
            os.remove('test_tenants.json')

    def test_add_tenant(self):
        tenant = Tenant(tenant_id=1, name='John Doe', age=30, contact_number='1234567890')
        self.repo.add_tenant(tenant)
        self.assertIn(tenant, self.repo.tenants)

    def test_delete_tenant(self):
        tenant = Tenant(tenant_id=1, name='John Doe', age=30, contact_number='1234567890')
        self.repo.add_tenant(tenant)
        result = self.repo.delete_tenant(1)
        self.assertTrue(result)
        self.assertNotIn(tenant, self.repo.tenants)

    def test_get_tenant_by_id(self):
        tenant = Tenant(tenant_id=1, name='John Doe', age=30, contact_number='1234567890')
        self.repo.add_tenant(tenant)
        fetched = self.repo.get_tenant_by_id(1)
        self.assertEqual(fetched, tenant)

if __name__ == '__main__':
    unittest.main()
