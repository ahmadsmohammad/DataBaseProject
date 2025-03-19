# DataBaseProject
SQL x Django DB Project


1) Setting up:
   - Download the .sql file found in the db folder.
   - Run it in mySQL workbench to set up database
  
2) Download Django Code:
   - Download python code and set it in its own folder.
   - To run code "python manage.py runserver" in the "hospital_backend" directory
  
**CURRENT PROGRESS**
- After starting the server, you can access (locally) these REST APIS to update DB...
                          - http://127.0.0.1:8000/api/patients/
                          - http://127.0.0.1:8000/admin/ (Can update permissions through Django 'superuser')
                          - http://127.0.0.1:8000/api/appointments/
                          - http://127.0.0.1:8000/api/doctors/
- Made a basic front end which *currently* allows you to check contents of most tables
- this will be useful for deugging and implementing RBAC
- frontend accessible @ 'http://127.0.0.1:8000/'



**TO-DOs**
- Implement RBAC and logon page to enforce
   - Have it to when user logs on ONLY the tables permissible to them is viewable/editable based on RBAC Diagram in slides
- Implement security policies such as encryption on the data possibly through sql default
