def build_profile(first,last,**info):
    """내 정보 딕셔너리 저장"""
    info['first_name']=first
    info['last_name']=last
    return info

my_profile = build_profile('shin','kyun young',
                           height = '172cm',
                           weight = '68kg',
                           hobbys = 'guitar')
print(my_profile)