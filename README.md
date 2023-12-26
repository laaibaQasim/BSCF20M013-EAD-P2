## Setting Up the Project
To successfully run the project, follow these steps:

### 1. Create etc Folder:
In the backend directory, create a new folder named etc.

### 2. Add settings.json File:
Inside the etc folder, create a file named settings.json.

### 3. Configure settings.json:
Populate settings.json with the following content:
<<<<<<< HEAD
```sh{
  "env": "dev",
  "database_uri": "mysql+pymysql://user_name:password@localhost/db_name"
}
```
=======
{
  "env": "dev",
  "database_uri": "mysql+pymysql://user_name:password@localhost/db_name"
}

>>>>>>> 8c14f297c5acf88c0471ff244dcde7ce8caedb6a
Make sure to replace db_name,user_name,password with your actual database name, user name and provide the appropriate password.

These settings are essential for configuring the development environment and specifying the database connection URI. Ensure the accuracy of the information provided to establish a seamless connection between the backend and the MySQL database.

Now, your project is ready to run with the necessary configuration in place.
## Commands
<<<<<<< HEAD
```sh
cd backend
python src/app.py
npm start
```
=======
#### python backend/src/app.py
#### npm start
>>>>>>> 8c14f297c5acf88c0471ff244dcde7ce8caedb6a
