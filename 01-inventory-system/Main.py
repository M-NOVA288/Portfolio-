from database import connect, create_table
import datetime

create_table()

def add_item():
    conn = connect()
    cursor = conn.cursor()
    name = input("Item name: ")
    quantity = int(input("Quantity: "))
    location = input("Location: ")
    date = datetime.datetime.now()
    cursor.execute("INSERT INTO inventory (item_name, quantity, location, last_updated) VALUES (?, ?, ?, ?)",
                   (name, quantity, location, date))
    conn.commit()
    conn.close()
    print("Item added successfully!")

def view_inventory():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

while True:
    print("\n1. Add Item")
    print("2. View Inventory")
    print("3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        break
