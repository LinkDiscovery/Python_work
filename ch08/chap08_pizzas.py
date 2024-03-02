# import chap08_pizza219p 

# chap08_pizza219p.make_pizza(16, 'pepperoni')
# chap08_pizza219p.make_pizza(12, 'mushroom','green peppers','extra cheese')
# ------------------------------------------------ 모듈을 호출 ▲

# from chap08_pizza219p import make_pizza 

# chap08_pizza219p.make_pizza(16, 'pepperoni')
# chap08_pizza219p.make_pizza(12, 'mushroom','green peppers','extra cheese')
#------------------------------------------------- 모듈의 함수를 호출 ↑

from chap08_pizza219p import make_pizza as mk

mk(16,'pepperoni')
# -------------------------------------------모듈의 함수에 이름 넣기


