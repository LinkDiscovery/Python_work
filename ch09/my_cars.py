from module_name import * ### 잘 사용하지 않는다.

import car as c
#improt numpy as np

my_mustang = c.Car('ford','mustang',2024) # car의 객체가 만들어지고 메서드 출력
print(my_mustang.get_descriptive_name())
my_leaf = c.ElectricCar('nissan','leaf',2023) # electriccar의 객체가 만들어지고 메서드 추력 
print(my_leaf.get_descriptive_name())

