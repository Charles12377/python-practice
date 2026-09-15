def make_album(music,musician,age=None):
    message={'music':music,'musician':musician}
    if age:
        message={'music':music,'musician':musician,'age':age}
    return message
message=make_album('灵魂歌手','梁博')
print(message)
message=make_album('曾经是情侣','梁博')
print(message)
message=make_album('White Farrari','Frank Ocean')
print(message)
message=make_album('Hello','Adele',30)
print(message)