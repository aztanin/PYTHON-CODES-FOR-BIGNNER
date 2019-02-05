fruits = ['Apple' , 'Orance' , 'Banana']
fastFoods = ['Pizza' , 'Burger' , 'BBQ Chicken']

#merge array
foods = fruits + fastFoods

print( fruits )                                      #['Apple', 'Orance', 'Banana']
print( fruits[2] )                                   #Banana

print( fastFoods )                                   #['Pizza', 'Burger', 'BBQ Chicken']
print( foods )                                       #['Apple', 'Orance', 'Banana', 'Pizza', 'Burger', 'BBQ Chicken']

#array length
print( len( foods ) )                                #6

#array part
print( fastFoods[1:3] )                              #['Burger', 'BBQ Chicken']
#reverse
print( fastFoods[::-1] )                             #['BBQ Chicken', 'Burger', 'Pizza']
print( foods[::-1] )                                 #['BBQ Chicken', 'Burger', 'Pizza', 'Banana', 'Orance', 'Apple']

#apppend array
fruits.append( 'Mango' )
print( fruits )                                      #['Apple', 'Orance', 'Banana', 'Mango']

#reverge
fruits.reverse()
print( fruits )                                      #['Mango', 'Banana', 'Orance', 'Apple']

#replace array data
fruits[:1] = ['Strawberry']
print( fruits )                                      #['Strawberry', 'Banana', 'Orance', 'Apple']

fastFoods[0:2] = ['Sandwich' , 'Cold Coffee']
print( fastFoods )                                   #['Sandwich', 'Cold Coffee', 'BBQ Chicken']
