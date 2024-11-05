import sys
from repositories.tenant_repository import TenantRepository
from repositories.flat_repository import FlatRepository
from controllers.tenant_controller import TenantController
from controllers.flat_controller import FlatController
from controllers.assignment_controller import AssignmentController
from models.tenant import Tenant
from models.flat import Flat
from typing import List, Optional


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


def prompt(message: str) -> str:
    return input(message)


def display(message: str):
    print(message)


def display_tenants(tenants: List[Tenant]):
    if not tenants:
        print("No tenants available.")
        return
    print("\nList of Tenants:")
    print("-----------------")
    for tenant in tenants:
        print(f"ID: {tenant.tenant_id}, Name: {tenant.name}, Age: {tenant.age}, "
              f"Contact: {tenant.contact_number}, Flat: {tenant.flat_number or 'Unassigned'}")
    print()


def display_flats(flats: List[Flat]):
    if not flats:
        print("No flats available.")
        return
    print("\nList of Flats:")
    print("--------------")
    for flat in flats:
        tenant_ids = ', '.join(map(str, flat.tenants)) if flat.tenants else 'None'
        print(f"Flat Number: {flat.flat_number}, Floor: {flat.floor}, "
              f"Type: {flat.room_type}, Tenants: {tenant_ids}")
    print()


def display_flat_info(flat: Optional[Flat]):
    if not flat:
        print("Flat not found.")
        return
    print("\nFlat Information:")
    print("------------------")
    print(f"Flat Number: {flat.flat_number}")
    print(f"Floor: {flat.floor}")
    print(f"Type: {flat.room_type}")
    tenant_ids = ', '.join(map(str, flat.tenants)) if flat.tenants else 'None'
    print(f"Tenants Assigned: {tenant_ids}")
    print()


def display_flats_by_floor(flats: List[Flat], floor: int):
    if not flats:
        print(f"No flats found on floor {floor}.")
        return
    print(f"\nFlats on Floor {floor}:")
    print("-----------------------")
    for flat in flats:
        tenant_ids = ', '.join(map(str, flat.tenants)) if flat.tenants else 'None'
        print(f"Flat Number: {flat.flat_number}, Type: {flat.room_type}, Tenants: {tenant_ids}")
    print()


def display_flats_by_type(flats: List[Flat], room_type: str):
    if not flats:
        print(f"No flats of type '{room_type}' found.")
        return
    print(f"\nFlats of Type '{room_type}':")
    print("-----------------------------")
    for flat in flats:
        tenant_ids = ', '.join(map(str, flat.tenants)) if flat.tenants else 'None'
        print(f"Flat Number: {flat.flat_number}, Floor: {flat.floor}, Tenants: {tenant_ids}")
    print()


def report_display_all_tenants(tenant_ctrl: TenantController):
    tenants = tenant_ctrl.get_all_tenants()
    display_tenants(tenants)


def report_display_all_flats(flat_ctrl: FlatController):
    flats = flat_ctrl.get_all_flats()
    display_flats(flats)


def report_display_specific_flat(flat_ctrl: FlatController):
    flat_number = int(prompt("Enter Flat Number: ").strip())
    flat = flat_ctrl.get_flat(flat_number)
    display_flat_info(flat)


def report_display_flats_on_floor(flat_ctrl: FlatController):
    floor = int(prompt("Enter Floor Number: ").strip())
    flats = flat_ctrl.get_flats_by_floor(floor)
    display_flats_by_floor(flats, floor)


def report_display_flats_by_type(flat_ctrl: FlatController):
    room_type = prompt("Enter Room Type (e.g., '1-room'): ").strip()
    flats = flat_ctrl.get_flats_by_type(room_type)
    display_flats_by_type(flats, room_type)


def generate_reports(tenant_ctrl: TenantController, flat_ctrl: FlatController):
    report_menu = """
    ===== Reports Menu =====
    1. Display all tenants
    2. Display all flats
    3. Display specific flat
    4. Display flats on a specific floor
    5. Display flats by type
    0. Back to Main Menu
    ========================
    """
    while True:
        print(report_menu)
        report_choice = prompt("Enter your choice: ").strip()
        if report_choice == '1':
            report_display_all_tenants(tenant_ctrl)
        elif report_choice == '2':
            report_display_all_flats(flat_ctrl)
        elif report_choice == '3':
            report_display_specific_flat(flat_ctrl)
        elif report_choice == '4':
            report_display_flats_on_floor(flat_ctrl)
        elif report_choice == '5':
            report_display_flats_by_type(flat_ctrl)
        elif report_choice == '0':
            break
        else:
            display("Invalid choice. Please try again.")


def main():
    # Initialize repositories
    tenant_repo = TenantRepository('tenants.json')
    flat_repo = FlatRepository('flats.json')

    # Initialize controllers
    tenant_ctrl = TenantController(tenant_repo)
    flat_ctrl = FlatController(flat_repo)
    assignment_ctrl = AssignmentController(tenant_repo, flat_repo)

    while True:
        display_menu()
        choice = prompt("Enter your choice: ").strip()

        if choice == '1':
            name = prompt("Enter Tenant Name: ").strip()
            age = int(prompt("Enter Tenant Age: ").strip())
            contact = prompt("Enter Contact Number: ").strip()
            tenant = tenant_ctrl.add_tenant(name, age, contact)
            display(f"Tenant added with ID: {tenant.tenant_id}")

        elif choice == '2':
            tenant_id = int(prompt("Enter Tenant ID to delete: ").strip())
            success = tenant_ctrl.delete_tenant(tenant_id)
            if success:
                display("Tenant deleted successfully.")
            else:
                display("Tenant not found.")

        elif choice == '3':
            flat_number = int(prompt("Enter Flat Number: ").strip())
            floor = int(prompt("Enter Floor Number: ").strip())
            room_type = prompt("Enter Room Type (e.g., '1-room'): ").strip()
            flat = flat_ctrl.add_flat(flat_number, floor, room_type)
            display(f"Flat {flat.flat_number} added successfully.")

        elif choice == '4':
            flat_number = int(prompt("Enter Flat Number to delete: ").strip())
            success = flat_ctrl.delete_flat(flat_number)
            if success:
                display("Flat deleted successfully.")
            else:
                display("Flat not found.")

        elif choice == '5':
            tenant_id = int(prompt("Enter Tenant ID to assign: ").strip())
            flat_number = int(prompt("Enter Flat Number to assign to: ").strip())
            success = assignment_ctrl.assign_tenant_to_flat(tenant_id, flat_number)
            if success:
                display("Tenant assigned to flat successfully.")
            else:
                display("Assignment failed. Check if tenant and flat exist, or tenant is already assigned.")

        elif choice == '6':
            tenant_id = int(prompt("Enter Tenant ID to unassign: ").strip())
            success = assignment_ctrl.unassign_tenant_from_flat(tenant_id)
            if success:
                display("Tenant unassigned from flat successfully.")
            else:
                display("Unassignment failed. Check if tenant exists and is assigned to a flat.")

        elif choice == '7':
            tenant_repo.save()
            flat_repo.save()
            display("Information saved to files successfully.")

        elif choice == '8':
            tenant_repo.load()
            flat_repo.load()
            display("Information loaded from files successfully.")

        elif choice == '9':
            generate_reports(tenant_ctrl, flat_ctrl)

        elif choice == '0':
            display("Exiting the application. Goodbye!")
            sys.exit(0)

        else:
            display("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
