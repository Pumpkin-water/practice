import pymysql

# 连接数据库
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='stu',charset='utf8')

# 获取游标  (操作数据库，执行sql语句)
cur=db.cursor()

def login():
    name = input("输入用户名：")
    sql = "select username,password from user where username=%s"
    cur.execute(sql, [name])
    li = cur.fetchone()
    if li is None:
        return False
    else:
        passwd = input("输入密码：")
        if passwd == li[1]:
            return True
        else:
            return False

def register():
    name = input("输入用户名：")
    sql = "select username from user where username=%s"
    cur.execute(sql, [name])
    if cur.fetchone():
        return False
    else:
        pw = input("输入密码：")
        sql = "insert into user(username,password) values(%s,%s)"
        cur.execute(sql, [name, pw])
        db.commit()
        return True

while True:
    print("""
            ===============
            1.注册    2.登录
            ===============
    """)
    order=input("输入命令:")
    if order=='1':
        if register():
            print("注册成功")
        else:
            print("用户已注册")
    elif order=='2':
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")

# 关闭数据库
cur.close()
db.close()