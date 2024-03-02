# def show_messages(msgs):
#     for msg in msgs:
#         msg1 = f"introduce : {msg.title()}"
#         print(msg1)
        
# lst = ['Hi' , 'My', 'name','kyunyoung']
# show_messages(lst)

# ------------------------------------------ 8-9
def send_message(lst,lst2):
    
    while lst:
        current_lst = lst.pop()
        print(f"Printing model : {current_lst}")
        lst2.append(current_lst)
        
def show_lst2(lst2):
    print("\nThe following models have been printed")
    for ls in lst2:
        print(ls)
    
lst = ['Hi' , 'My', 'name','kyunyoung']
lst2 = []
    
send_message(lst,lst2)
show_lst2(lst2)

