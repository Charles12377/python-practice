def user_profile(f,l,**info):
    info['first']=f
    info['last']=l
    return info



# model1.py末尾
if __name__ == "__main__":
    print(user_profile('Albert','Einstein',age="1879‑1955"))
