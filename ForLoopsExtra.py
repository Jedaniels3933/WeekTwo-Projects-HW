#For Loops Review

stuff = ['item1', 'item2', 'item3','item4']

for i in stuff:
    this = 'that'
    if i == 'item3': #print(f"The thing my for loop is currently looking at is: {thing}")
        print(i.upper())
    else:
        print(f"The Thing my for loop is currently looking at is : {i}")

        #If this thing is not this thing the next line will repeat

flavors = ['cheese', 'peanut butter', 'coconut', 'banana']
toppings = ['chocolate', 'vanilla', 'strawberry' , 'postashio']

#To try each flaor with each topping 

for flavor in flavors:
    for topping in toppings:
            print(flavor)
            print("Right Now I am tasting", flavor, "with", topping) #or
            #print(f"Right Now I am tasting {flavor} with {topping}") #same thing
    #If this flavor is not this flavor the next line will repeat

    









