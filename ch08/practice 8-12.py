def make_sandwich(*ingredients):
    """요청 재료 받기"""
    print("\n Ingredient Order List")
    for ingredient in ingredients:
        print(f"-{ingredient}")
    
make_sandwich('ham')
make_sandwich('ham','cheese','eggs')
make_sandwich('eggs','bacon')