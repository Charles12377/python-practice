words={
    'sort':'排序',
    'title':'首字母大写',
    'lower':'全部小写',
    'def':'函数定义',
    'for':'循环遍历',
    }
for word,mean in words.items():
    print(word,mean)

rivers={
    'Nile':'Egypt',
    'amazon':'Peru',
    'Danube':'germany',
    }
for river,contry in rivers.items():
    print(f'The {river.title()} runs through {contry.title()}.')
for r in rivers.keys():
    print(r.title())
for c in rivers.values():
    print(c.title())