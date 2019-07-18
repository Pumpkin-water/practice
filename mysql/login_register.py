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
        print("用户不存在")
    else:
        passwd = input("输入密码：")
        if passwd == li[1]:
            print("登录成功")
        else:
            print('密码不匹配')

def register():
    name = input("输入用户名：")
    sql = "select username from user where username=%s"
    cur.execute(sql, [name])
    if cur.fetchone() is None:
        pw = input("输入密码：")
        sql = "insert into user(username,password) values(%s,%s)"
        cur.execute(sql, [name, pw])
        db.commit()
    else:
        print("用户名已存在")

while True:
    order=input("登录/注册:")
    if order=='注册':
        register()
    elif order=='登录':
        login()

# 关闭数据库
cur.close()
db.close()