import matplotlib.pyplot as plt

from die import Die

die_1=Die(6)
die_2=Die(6)

results=[]

results=[die_1.roll()*die_2.roll() for _ in range(1000)]

frequencies=[]
max_result = die_1.num_sides * die_2.num_sides 
poss_results=range(1,max_result+1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)

title="Frequencies of two D6's results 1000 times"
lables={'x':'Result','y':'Frequencies of Result'}

fig,ax=plt.subplots()
ax.bar(poss_results,frequencies)

ax.set_title(title)
ax.set_xlabel(lables['x'])
ax.set_ylabel(lables['y']) 

ax.set_xticks(poss_results)
ax.tick_params(rotation=60)

plt.show()