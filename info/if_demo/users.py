users=['admin','yuanhua','Lihua','charles','Kobe','Jordan']
lower_users=[user.lower() for user in users]
if users:
    for user in users:
        if user=='admin':
            print('Hello admin,would you like to see a status report?')
        else:
            print('Hello Jaden,thank you for logging in again.')
else:
    print('We need to find some users!')

new_users=['yuanhua','kobe','john','taler','wesbrok']
for user_1 in new_users:
    if user_1 in lower_users:
        print('该用户名已被使用,请重新输入:')
    else:
        print('该用户名未被使用.')
