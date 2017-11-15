from MysqlHelper import *

# param1 = input('请输入ID：')
# param2 = input('请输入设备种类：')
# param3 = input('请输入类别ID：')
# sql = 'insert into classify values (16,%s,%s)'
# mh = MysqlHelper('localhost',3306,'root','root','classify')
# mh.cud(sql,[param2,param3])

sql = 'select * from classify where pid=2'
mh = MysqlHelper('localhost',3306,'root','root','classify')
result=mh.read(sql)
print(result,end='')
print(result)