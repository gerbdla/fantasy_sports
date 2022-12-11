import pymysql

class Connection:
    def connect():
        db_host = 'localhost'
        db_user = 'root'
        db_password = ''
        db_name = 'basketball'
        return pymysql.connect(db_host,db_user,db_password,db_name)

      
    # methods
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
  