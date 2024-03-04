def make_cars(manufacturer,model,**info):
    """자동차 정보 저장"""
    info['manufacturer_name']=manufacturer
    info['model_name']=model
    return info

car = make_cars('subaru','outback',color = 'blue',tow_package= True)
print(car)