import sqlite3
connection = sqlite3.connect('my_repairs.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
               Repairs ( 
                   ID INTEGER PRIMARY KEY 
                AUTOINCREMENT,
                    Device TEXT,
                    Issue TEXT,
                    Status TEXT
               )
              ''')

print("---Welcome to Valenica IT Shop!---")
user_device = input ("Enter Device Name (ex. iPhone, Mac, Lenovo): ")
user_issues = input ("Please explain your issue with this device (ex. Charging port broken, cracked screen, won't turn on): ")

cursor.execute("INSERT INTO Repairs(Device, Issue, Status) VALUES (?, ?, 'PENDING')", 
                                                                                (user_device,
user_issues))

connection.commit()

print("\n[SUCCESS] Ticket saved! Check your sidebar for 'my_repairs.db'")

connection.close()
