This is a Full IT Repair Support Tool i built to manage hardware repair records. This has a combination of Python logic and SQL Database to ensure no repair ticket ever gets lost.

Python: Handling the user interface and logic for porcessing tickets.
SQLite3: Relational Database that stores replair data locally on the machine

The Folder contains 3 files

- repairs.py: Prompts the user for device info and details of the issue for it to be saved in the database.
- update_status: Allows the technican to mark the ticket as completed if finished.
- delete_tickey: Safely removes old or test data from the system while maintaining data integrity.

  The Database Structure.
  
  <img width="1000" height="587" alt="image" src="https://github.com/user-attachments/assets/b5de4528-9ad5-4fbb-9ca3-a12a88ab5662" />

  The system uses a table called "Repairs":
  - ID: Primary Key (Auto-incremented)
  - Device: Brand/model
  - Issue: technical problem
  - Status: Defaults to 'Pending' until updated.


Please Enjoy, This is a starting project. 
  
  


