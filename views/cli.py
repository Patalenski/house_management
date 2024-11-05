from typing import List  # Import List for type annotations
from models.tenant import Tenant  # Import Tenant class
from models.flat import Flat  # Import Flat class

class CLIView:
    @staticmethod
    def display_menu():
        menu = """
        ===== House Management Application =====
        1. Add Tenant
        2. Delete Tenant
        3. Add Flat
        4. Delete Flat
        5. Assign Tenant to Flat
        6. Unassign Tenant from Flat
        7. Save Information to File
        8. Load Information from File
        9. Generate Reports
        0. Exit
        =========================================
        """
        print(menu)

    @staticmethod
    def prompt(message: str) -> str:
        return input(message)

    @staticmethod
    def display(message: str):
        print(message)

    @staticmethod
    def display_tenants(tenants: List[Tenant]):
        if not tenants:
            print("No tenants available.")
            return
        print("List of Tenants:")
        for tenant in tenants:
            print(f"ID: {tenant.tenant_id}, Name: {tenant.name}, Age: {tenant.age}, "
                  f"Contact: {tenant.contact_number}, Flat: {tenant.flat_number or 'Unassigned'}")

    @staticmethod
    def display_flats(flats: List[Flat]):
        if not flats:
            print("No flats available.")
            return
        print("List of Flats:")
        for flat in flats:
            print(f"Flat Number: {flat.flat_number}, Floor: {flat.floor}, "
                  f"Type: {flat.room_type}, Tenants: {flat.tenants}")

    @staticmethod
    def display_flat_info(flat: Flat):
        if not flat:
            print("Flat not found.")
            return
        print(f"Flat Number: {flat.flat_number}")
        print(f"Floor: {flat.floor}")
        print(f"Type: {flat.room_type}")
        print(f"Tenants Assigned: {flat.tenants if flat.tenants else 'None'}")

    @staticmethod
    def display_flats_by_floor(flats: List[Flat], floor: int):
        if not flats:
            print(f"No flats found on floor {floor}.")
            return
        print(f"Flats on Floor {floor}:")
        for flat in flats:
            print(f"Flat Number: {flat.flat_number}, Type: {flat.room_type}, Tenants: {flat.tenants}")

    @staticmethod
    def display_flats_by_type(flats: List[Flat], room_type: str):
        if not flats:
            print(f"No flats of type '{room_type}' found.")
            return
        print(f"Flats of Type '{room_type}':")
        for flat in flats:
            print(f"Flat Number: {flat.flat_number}, Floor: {flat.floor}, Tenants: {flat.tenants}")
