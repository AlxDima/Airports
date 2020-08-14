import mysql.connector


class Database:
    def __init__(self):
        self.host = '35.228.161.8'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'sep6pass'
        self.db = 'SP6-2'
        self.mydb = mysql.connector.connect(host=self.host,
                                       port=self.port,
                                       user=self.user,
                                       passwd=self.passwd,
                                       db='SP6-2')
        self.cursor = self.mydb.cursor()

    def connect(self):
        return self.host + ' ' + self.user + ' ' + self.passwd + ' ' + self.db 

    def get_manu(self):
        sql = """SELECT model FROM planes WHERE   manufacturer='AIRBUS'  """ 
        self.cursor.execute(sql)  # some SQL command
        return  [item[0] for item in self.cursor.fetchall()]
    
    def get_item_0(self, request):
        self.cursor.execute(request)
        return  [item[0] for item in self.cursor.fetchall()]

    def get(self, request):
        self.cursor.execute(request)  
        return self.cursor.fetchall()

 
   