names=['小明','小红','小芳','小颜','小李']
print(names[1])
print(names[-2])
print(f'{names[3]},早上好！')
names.append('小王')
names.insert(2,'小花')
del names[3]
print(names)
names.remove('小明')
pop_names=names.pop()
print(names)
print(pop_names)

transportation=['bus','car','bike','train','高铁']
print(f'I would like to by {transportation[3].title()}.')

people=['小李','小杨','小陈','小杜','小郭','小韩','小周']
print(people)
people[0]='小敏'
print(people)
people.insert(2,'小李')
people.append('小洛')
print(f'hello {people} please come have dinner with me')
print(f'sorry {people},I just can invite two guys')
print(f'sorry {people.pop()},I can not invite you.')
print(people)
print(len(people))
del people[:]
print(people)

travel_place=['dalian','qindao','sanya','shanghai','nanjin']
print(travel_place)
print(sorted(travel_place))
print(travel_place)
print(sorted(travel_place,reverse=True))
print(travel_place)
travel_place.reverse()
print(travel_place)
travel_place.reverse()
print(travel_place)
travel_place.sort()
print(travel_place)
travel_place.sort(reverse=True)
print(travel_place)
