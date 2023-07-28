import os
import pathlib 
import datetime

class Error_Writer:
    current_path = str(pathlib.Path(__file__).parent.resolve())
    database_file = current_path + "/errors/database_errors.txt"
    route_error = current_path + "/errors/route_errors.txt"

    #writer for database errors into txt file
    @staticmethod
    def write_database_error(error):
        os.makedirs(os.path.dirname(Error_Writer.database_file), exist_ok=True)
        file = open(Error_Writer.database_file, "a")
        file.write(str(datetime.datetime.now()) +": "+ str(error))
        file.close()

    #writer for any route errors into the txt file
    @staticmethod
    def write_route_error(error):
        os.makedirs(os.path.dirname(Error_Writer.route_error), exist_ok=True)
        file = open(Error_Writer.route_error, "a")
        file.write(str(datetime.datetime.now()) +": "+ str(error))
        file.close()       