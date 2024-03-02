cars = ['audi','bmw','subaru','toyota']

for car in cars : 
    if car == 'bmw' : 
        print(car.upper())
    else:
        print(car.title())
        
        yyy = 'audi' in cars
        print(yyy)
        # True
        age = 18
    if age >=19:
        print("you can vote")
    else:
        print("you cannt")
        
age = 12 
if age <4:
    print("q")
elif age <18:
    print("p")
else :
    print("o")
    
    
available_toppings = ['mushroom','green pepers','extra cheese',
                      'olives','pepperoni','pineapple']
requested_toppings = ['mushroom','green pepers','french fries']

for requested_topping in requested_toppings:
     if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
     else :
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
        
        