import sqlite3
connection = sqlite3.connect('my_repairs.db')
cursor = connection.cursor()

print("--- Valencia IT Shop: Confirmation Update ---")
ticket_id = input("Enter the ID of the ticket you finsihed: ")
cursor.execute("UPDATE Repairs SET Status = 'COMPLETED' WHERE ID = ?",
(ticket_id,))

connection.commit()

print("\n [SUCCESS] Ticket #{ticket_id} is now marked as COMPLETED!")
connection.close()
