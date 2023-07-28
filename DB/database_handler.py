from errorWriter import Error_Writer


#database handler to write to database all methods must be passes mysql
#mysql needs to be passes extra the cursor object and connection
class Database:

    #sub method to create user table
    #sub method of table to check table
    @staticmethod
    def sub_method_createUserTable(mysql) -> bool:
        try:
            cursor = mysql.connection.cursor();
            cursor.execute("CREATE TABLE IF NOT EXISTS User (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT);")
            mysql.connection.commit()
            return True
        except:
            return False
        

    #add user to database mysql must be passed to establish cursor just like all sql entries
    @staticmethod
    def addUser(mysql, name, age) -> bool:
        try:
            table_created = Database.sub_method_createUserTable(mysql)
            if not table_created:
                return False
            else:
                cursor = mysql.connection.cursor()
                cursor.execute("INSERT INTO User (name, age) VALUES (%s, %s);", (name, age))
                mysql.connection.commit()
                return True
        except Exception as error:
            Error_Writer.write_database_error(error)
            return False, error

        
        