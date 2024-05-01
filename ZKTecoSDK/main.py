from zkteco.zkt import *

conn = None
zk = ZK('192.168.1.201')
try:
    conn = zk.connect()
    conn.disable_device()
    users = conn.get_users()
    for user in users:
        privilege = 'User'
        if user.privilege == USER_ADMIN:
            privilege = 'Admin'
        print(user.uid)
        print(user.name)
        print(user.user_id)
        print(user.card)
        print('---------')

    conn.enable_device()
finally:
    if conn:
        conn.disconnect()