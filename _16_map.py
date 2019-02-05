age = [12,23,55,16]

def double_age( age ):
    return age * 2

_age = list( map(double_age , age) )

print( _age )

#[24, 46, 110, 32]