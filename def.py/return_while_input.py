def make_album(music,musician,age=None):
    message={'music':music,'musician':musician}
    if age:
        message={'music':music,'musician':musician,'age':age}
    return message
while True:
    print("Enter your favourate music and musician.")
    print("Enter 'q' will quit.")
    i_music=input("Enter your favourate music:")
    if i_music == 'q':
        break
    i_musician=input("Enter this music's musician:")
    if i_musician == 'q':
        break
    i_age=input("Enter this musician's sge:")
    if i_age == 'q':
        break
    message=make_album(i_music,i_musician,i_age)
    print(message)