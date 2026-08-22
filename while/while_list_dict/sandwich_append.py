sandwich_orders=['sub','burger','wrap']
finished_sandwichs=[]
while sandwich_orders != []:
    sandwich=sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwichs.append(sandwich)
print(f"I made {finished_sandwichs}.")