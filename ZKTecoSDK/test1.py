from zkteco.zkt import *

conn = None
zk = ZK('192.168.1.201',port=4370)
conn = zk.connect()
# users = conn.get_users()
# print(users)

zkhelper = ZK_helper('192.168.1.201', 4370)
# print(zkhelper.test_ping())
# conn.disconnect()

# users = conn.get_users_by_id('28')
# print(users)



# try:
#     conn = zk.connect()
#     conn.disable_device()
#     users = conn.get_users()
#     conn.set_user(uid=33, name='swix', user_id='123', card=1263854)
#     print(users)
#     conn.delete_user(uid=33)


#     conn.enable_device()
# finally:
#     if conn:
#         conn.disconnect()