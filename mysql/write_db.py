"""
write_db.py
pymysql 写操作示例  (insert update delete)
"""

import pymysql

# 连接数据库
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='stu',charset='utf8')

# 获取游标  (操作数据库，执行sql语句)
cur=db.cursor()

# 写数据库
try:
    # 写sql语句执行
    # 插入操作

    # name=input("Name:")
    # age=input("Age:")
    # score=input("Score:")

    # sql="insert into class(name,age,score) values('"+name+"',"+age+","+score+")"
    #将变量插入到sql 语句合成最终操作语句
    # sql = "insert into class(name,age,score) values('%s',%s,%s)"%(name,age,score)
    # sql = "insert into class(name,age,score) values(%s,%s,%s)"
    # # 可以使用列表直接给sql语句的values 传值
    # cur.execute(sql,[name,age,score])

    #修改操作
    # sql="update interest set price=11800 where name='zs'"
    # cur.execute(sql)

    #删除操作
    sql="delete from class where score<50 and score>40"
    cur.execute(sql)

    db.commit()
except Exception as e:
    db.rollback()  # 退回到commit执行之前的数据库状态
    print(e)

# 关闭数据库
cur.close()
db.close()