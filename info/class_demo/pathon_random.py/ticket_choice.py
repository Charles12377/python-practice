from random import choices,sample    #choices可以重复抽取，sample不会重复抽取
list_1=[1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
finding=sample(list_1,k=4)
print(f"If you get {finding},congratulation!you've won a prize.")

count=0
while True:
    my_ticket=sample(list_1,k=4)
    if finding != my_ticket:
        count += 1
    else:
        print("Congratulation!you've won a prize.")
        break
print(count)