resources = [
    {
        "id": "R001",
        "name": "Laptop",
        "category": "Electronics",
        "total": 10,
        "available": 10
    },
    {
        "id": "R002",
        "name": "Keyboard",
        "category": "Accessories",
        "total": 5,
        "available": 5
    },
    {
        "id": "R003",
        "name": "Headset",
        "category": "Accessories",
        "total": 3,
        "available": 3
    }
]

fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

borrow_records = []


def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None


def add_resource():
    resource_id = input("Enter resource ID: ").strip()

    if find_resource(resource_id) is not None:
        print("Error: resource ID already exists.")
        return

    name = input("Enter resource name: ").strip()
    category = input("Enter category: ").strip()

    try:
        total = int(input("Enter total units: "))
    except ValueError:
        print("Error: total units must be a whole number.")
        return

    if total <= 0:
        print("Error: total units must be greater than 0.")
        return

    new_resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    }

    resources.append(new_resource)

    print("Resource added successfully.")


def list_resources():
    print("\n--- Resource Inventory ---")

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        print(
            f'{resource["id"]} | '
            f'{resource["name"]} | '
            f'{resource["category"]} | '
            f'Total: {resource["total"]} | '
            f'Available: {resource["available"]} | '
            f'Borrowed: {borrowed}'
        )


def borrow_resource():
    fellow_id = input("Enter fellow ID: ").strip()

    if fellow_id not in fellows:
        print("Error: fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ").strip()

    resource = find_resource(resource_id)

    if resource is None:
        print("Error: resource ID not found.")
        return

    try:
        quantity = int(input("Enter quantity to borrow: "))
    except ValueError:
        print("Error: quantity must be a whole number.")
        return

    if quantity <= 0:
        print("Error: quantity must be greater than 0.")
        return

    if quantity > resource["available"]:
        print("Error: not enough units available.")
        return

    resource["available"] -= quantity

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            record["quantity"] += quantity
            break
    else:
        borrow_records.append({
            "fellow_id": fellow_id,
            "resource_id": resource_id,
            "quantity": quantity
        })

    print(
        f'{fellows[fellow_id]} successfully borrowed '
        f'{quantity} {resource["name"]}(s).'
    )


def return_resource():
    fellow_id = input("Enter fellow ID: ").strip()

    if fellow_id not in fellows:
        print("Error: fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ").strip()

    resource = find_resource(resource_id)

    if resource is None:
        print("Error: resource ID not found.")
        return

    try:
        quantity = int(input("Enter quantity to return: "))
    except ValueError:
        print("Error: quantity must be a whole number.")
        return

    if quantity <= 0:
        print("Error: quantity must be greater than 0.")
        return

    loan_record = None

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            loan_record = record
            break

    if loan_record is None:
        print("Error: this fellow has no loan for this resource.")
        return

    if quantity > loan_record["quantity"]:
        print("Error: cannot return more units than currently borrowed.")
        return

    resource["available"] += quantity
    loan_record["quantity"] -= quantity

    if loan_record["quantity"] == 0:
        borrow_records.remove(loan_record)

    print(
        f'{fellows[fellow_id]} successfully returned '
        f'{quantity} {resource["name"]}(s).'
    )


def search_resources():
    search_name = input("Enter resource name to search: ").strip().lower()

    found = False

    for resource in resources:
        if search_name in resource["name"].lower():
            print(
                f'{resource["id"]} | '
                f'{resource["name"]} | '
                f'{resource["category"]} | '
                f'Available: {resource["available"]}'
            )
            found = True

    if not found:
        print("No matching resources found.")


def filter_by_category():
    category = input("Enter category: ").strip().lower()

    found = False

    for resource in resources:
        if resource["category"].lower() == category:
            print(
                f'{resource["id"]} | '
                f'{resource["name"]} | '
                f'{resource["category"]} | '
                f'Available: {resource["available"]}'
            )
            found = True

    if not found:
        print("No resources found in that category.")


def generate_report():
    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print("\n--- Inventory Report ---")
    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Currently borrowed: {borrowed_units}")

    print("\nLow stock resources:")

    low_stock_found = False

    for resource in resources:
        if resource["available"] < 3:
            print(
                f'- {resource["name"]} '
                f'({resource["available"]} available)'
            )
            low_stock_found = True

    if not low_stock_found:
        print("None")

    highest_borrowed = 0

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        if borrowed > highest_borrowed:
            highest_borrowed = borrowed

    print("\nMost borrowed resource(s):")

    if highest_borrowed == 0:
        print("None")
    else:
        for resource in resources:
            borrowed = resource["total"] - resource["available"]

            if borrowed == highest_borrowed:
                print(
                    f'- {resource["name"]} '
                    f'({borrowed} borrowed)'
                )


def main():
    while True:
        print("\n===== Learn2Earn Resource System =====")
        print("1. Add resource")
        print("2. List resources")
        print("3. Borrow resource")
        print("4. Return resource")
        print("5. Search resources")
        print("6. Filter by category")
        print("7. Generate report")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_resource()

        elif choice == "2":
            list_resources()

        elif choice == "3":
            borrow_resource()

        elif choice == "4":
            return_resource()

        elif choice == "5":
            search_resources()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Error: invalid menu option.")


if __name__ == "__main__":
    main()