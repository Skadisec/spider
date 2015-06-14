# coding:utf-8
import time
import MySQLdb
 
#建立和mysql数据库的连接
time = time.strftime("%Y-%m-%d", time.localtime())
print time

conn = MySQLdb.connect(host='localhost',user='root',passwd='toor',charset="utf8")
#获取游标
curs = conn.cursor()
#执行SQL,创建一个数据库
#set_time =time;
curs.execute("create database shiep3")
#选择连接哪个数据库
conn.select_db('shiep3')
curs.execute("create table test(id integer primary key auto_increment,http_url varchar(256) DEFAULT NULL,time varchar(50) DEFAULT NULL, hash_value varchar(30) DEFAULT NULL)")

#value = [1,"davehe"]
#curs.execute("insert into test values(%s,%s)",value)
#提交修改                               
#conn.commit()
#关闭游标连接,释放资源
curs.close()
#关闭连接
conn.close()

#time = time.strftime("%Y-%m-%d", time.localtime())
#print time
