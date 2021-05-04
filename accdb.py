import pyodbc,time
def loadDB(dbPath):
    return pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;"%dbPath)

def eSQL(dbConn,sql):
    return dbConn.cursor().execute(sql)

def leSQL(dbPath,sql):
    return eSQL(loadDB(dbPath),sql)

def cSQL(dbConn,sql):
    cur=dbConn.cursor()
    e=cur.execute(sql)
    cur.commit()
    return e

if __name__=='__main__':
    time.sleep(0.2)
    for i in leSQL(r'D:\杂物\学生身份信息.accdb',"select 姓名 from 九年级 where 准考证号 like '17030061_'"):
        print(i[0])
