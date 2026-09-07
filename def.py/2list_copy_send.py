def print_messages(messages,send_messages):
    while messages:
        message=messages.pop()
        print(message)
        send_messages.append(message)

def show_messages(messages,send_messages):
    print(messages)
    print(send_messages)
    #for send_message in send_messages:
        #print(send_message)

messages=["Hello Einstein.","I find myself enjoying physics."]
send_messages=[]
print_messages(messages[:],send_messages)
show_messages(messages,send_messages)