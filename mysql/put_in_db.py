"""
练习：将单词本存入数据库
1.创建数据库 dict  (utf8)
2.创建数据表 words  将单词和解释分别存入不同的字段
3.将单词存入words单词表  超过 19500即可
"""

import pymysql
import re

file=open('dict.txt','r')

db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='dict',charset='utf8')
cur=db.cursor()



sql="insert into words(word,interpret) values(%s,%s)"

try:
    for line in file:
    #获取单词和解释
        tup=re.findall(r'(\S+)\s+(.*)',line)[0]
        cur.execute(sql,tup)
    db.commit()
except:
    db.rollback()


# data=file.readline()
# tmp=data.split(' ')
# word=tmp[0]
# inter=' '.join(tmp[1:]).strip()

file.close()
cur.close()
db.close()
