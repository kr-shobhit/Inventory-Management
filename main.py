import time
import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS inventory(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        product_quantity INTEGER NOT NULL,
        product_price INTEGER NOT NULL
    )''')

def view_full_inventory():
    cursor.execute("SELECT * FROM inventory ORDER BY product_id")
    rows = cursor.fetchall()
    if not rows:
        print("No Items in Inventory. Add Products to View.")
    else:
        for row in rows:
            print(f"ID - {row[0]}, Product Name - {row[1]}, Product Quantity - {row[2]}, Product Price - {row[3]}")

def add_Items(product_name, product_quantity, product_price):
    cursor.execute("INSERT INTO inventory (product_name, product_quantity, product_price) VALUES (?,?,?)",(product_name, product_quantity, product_price))
    conn.commit()
    if cursor.rowcount == 1:
        print("\n Product Added Successfully")
    else:
        print("\n Error Adding Product!!")

def update_Items(product_id):
    cursor.execute("SELECT * FROM inventory WHERE product_id = ?",(product_id))
    result = cursor.fetchall()
    if not result:
        print("\nNo Product Found with entered ID!")
    else:
        print(result)
        print("\nEnter The New Data for the Item")
        new_product_name = input("Enter the New Product Name : ")
        new_product_quantity = input("Enter the New Product Quantity : ")
        new_product_price = input("Enter the New Product Price : ")
        cursor.execute("UPDATE inventory SET product_name = ?, product_quantity = ?, product_price = ? WHERE product_id = ?",(new_product_name,new_product_quantity, new_product_price, product_id))
        conn.commit()
        if cursor.rowcount == 1:
            print("\nProduct Modified Successfully")
        else:
            print("\nProduct Modification Failed!")

def delete_Items(product_id):
    cursor.execute("DELETE FROM inventory WHERE product_id = ?",(product_id,))
    if cursor.rowcount == 1:
        print("\nProduct Deleted Successfully")
    else:
        print("\nProduct Deletion Failed!")

def view_products_list():
    cursor.execute("SELECT product_id, product_name FROM inventory")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo Products Found! First Add Products in Inventory")
    else:
        for row in rows:
            print(f"ID - {row[0]}, Product Name - {row[1]}, Product Quantity - {row[2]}, Product Price - {row[3]}")

def main():
    while True:
        print("\n\n** Welcome to Inventory Management System **\n")
        print("Choose Option to Proceed :")
        print("1. View Inventory")
        print("2. Add Items to Inventory")
        print("3. Update Items in Inventory")
        print("4. Delete Item in Inventory")
        print("5. Exit")
        choice = input("\nEnter Here : ")
        
        match choice:
            case "1":
                print("\n")
                view_full_inventory()
            case "2":
                print("\n")
                product_name = input("Enter Product Name : ")
                product_quantity = input("Enter Product Quantity : ")
                product_price = input("Enter Product Price : ")
                add_Items(product_name,product_quantity,product_price)
            case "3":
                print("\nChoose the Product to Modify\n")
                view_products_list()
                product_id = input("\nEnter the ID of Product to Modify : ")
                update_Items(product_id)
            case "4":
                print("\nChoose the Product to Delete\n")
                view_products_list()
                product_id = input("\nEnter the ID of Product to Delete : ")
                delete_Items(product_id)
            case "5":
                print("\nThankyou! Exiting Inventory Management System.\n")
                time.sleep(1)
                break
            case _:
                print("\nInvalid Choice! Exiting Application")
                time.sleep(1)
                break
    conn.close()  
            
def addProductsMany():
    products = [
        ('Apple', 50, 100),
        ('Banana', 30, 40),
        ('Orange', 20, 60),
        ('Mango', 25, 120),
        ('Grapes', 40, 80),
        ('Pineapple', 10, 150),
        ('Watermelon', 15, 90),
        ('Strawberry', 35, 200),
        ('Blueberry', 18, 220),
        ('Kiwi', 12, 130),
        ('Papaya', 28, 110),
        ('Guava', 32, 70),
        ('Peach', 16, 95),
        ('Plum', 14, 85),
        ('Cherry', 22, 190),
        ('Coconut', 8, 170),
        ('Lemon', 27, 30),
        ('Lime', 26, 35),
        ('Avocado', 13, 160),
        ('Pomegranate', 19, 140),
        ('Dragonfruit', 5, 250),
        ('Jackfruit', 6, 180),
        ('Fig', 9, 115),
        ('Apricot', 11, 100),
        ('Blackberry', 7, 210),
    ]

    cursor.executemany(
        "INSERT INTO inventory (product_name, product_quantity, product_price) VALUES (?, ?, ?)",
        products
    )
    conn.commit()

          
if __name__ == "__main__":
    main()