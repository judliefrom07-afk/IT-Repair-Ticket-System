import sqlite3
connection = sqlite3.connect('my_repairs.db')
cursor = connection.cursor()

print("--- Valencia IT Shop: Removal---")
ticket_id = input("Enter the ID of the ticket you want to remove: ")

cursor.execute("DELETE FROM Repairs WHERE ID = ?", (ticket_id,))

connection.commit()

print(f"\n[SUCCESS] Ticket #{ticket_id} has been deleted from the database.")

connection.close()