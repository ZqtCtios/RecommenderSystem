import csv
import time

import pymysql
import cate_to_data
import userdata_discrete
import userAgent_classify


def getDBConnection(database):
    db = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        database,
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    return db, cursor


def loadData(filename):

    t = time.time()
    db, cursor = getDBConnection('Train')
    sql = 'CREATE TABLE data_temp(useraddress varchar(45) DEFAULT NULL,hostname varchar(45) DEFAULT NULL,userAgent text,tag varchar(45) DEFAULT NULL)'
    cursor.execute(sql)
    sql = " load data infile '{}' into table data_temp fields terminated by ',' optionally enclosed by '\"' escaped by '\"'".format(
        filename)
    cursor.execute(sql)
    cursor.execute('delete from data_temp where length(useraddress)<2')
    cursor.execute('DROP TABLE IF EXISTS data')
    cursor.execute('create table data like data_temp')
    cursor.execute(
        'insert into data select * from data_temp group by useraddress,hostname')
    cursor.execute('drop table data_temp')
    cursor.execute(
        'ALTER TABLE data ADD id INT NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (id)')
    db.commit()
    db.close()
    return time.time()-t


def train():
    t = time.time()
    cate_to_data.work()
    userdata_discrete.work()
    userAgent_classify.work()
    return time.time()-t


if __name__ == '__main__':
    loadData('/home/PythonWorkSpace/DaChuang/TrainData.csv')
