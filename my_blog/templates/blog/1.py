from redis import StrictRedis
sr = StrictRedis(host='192.168.229.144',port=6379,db=0,password='Px8023.*')
# re = sr.set('name', 'zhong')
# print(re)
ret = sr.get('nam23e')
print(ret)