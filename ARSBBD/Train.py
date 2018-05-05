import pymysql
import csv
def getDBConnection(database):
    db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    database,
    use_unicode=True,
    charset="utf8")
    cursor = db.cursor()
    return db,cursor

def loadData(filename):

    import time
    t=time.time()
    db,cursor=getDBConnection('Train')
    cursor.execute('DROP TABLE IF EXISTS data_temp')
    sql='CREATE TABLE data_temp(useraddress varchar(45) DEFAULT NULL,hostname varchar(45) DEFAULT NULL,userAgent text,tag varchar(45) DEFAULT NULL)'
    cursor.execute(sql)
    sql=" load data infile '{}' into table data_temp fields terminated by ',' optionally enclosed by '\"' escaped by '\"'".format(filename)
    #cursor.execute('delete from data_temp where userAgent like \'unkown\'')
    cursor.execute('DROP TABLE IF EXISTS data')
    cursor.execute('create table data like data_temp')
    cursor.execute('insert into data select * from data_temp group by useraddress,hostname')
    #cursor.execute('drop table data_temp')
    cursor.execute('ALTER TABLE data ADD id INT NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (id)')
    db.commit()
    return time.time()-t
        
def train():
    return 0

if __name__ == '__main__':
    loadData('/home/PythonWorkSpace/DaChuang/TrainData.csv')

    