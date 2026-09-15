def user_profile(f,l,**info):
    info['first']=f
    info['last']=l
    return info
print_profile=user_profile('Albert','Einstein',
                           age='1879-1955',field='physicist',
                           discovery='Discovered the theory of relativity')
print(print_profile)