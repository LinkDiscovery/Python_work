# def make_pizza(*toppings): #tuple로 받은 것
#     """요청받은 토핑 리스트를 출력합니다"""
#     print(toppings)
    
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')
# -----------------------------
# def make_pizza(*toppings): #tuple로 받은 것
#     """주문내용을 요약합니다"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings : 
#         print(f"-{topping}")
    
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')
# --------------------------------------------------
def make_pizza(size, *toppings): #tuple로 받은 것
    """주문내용을 요약합니다"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings : 
        print(f"-{topping}")
    
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')

