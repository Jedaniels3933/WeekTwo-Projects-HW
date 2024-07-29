#User in put with functions

#name  = input("What is your name?")

#print(f"Hey there cowboy, {name}!!")

num = 10        #ISINSTANCE CHECK TYPES
print(type(num))
print(isinstance(num, int))   #True
print(isinstance(num, dict))   #False

#len = len(num) Counts the letters or numbers of a list or other iterable
message = "Coding is hard as hell"

print(len(message))  #returns 22 - number of letters in the message

num = -5  #abs absolute value
print(abs(num))      # returns 5 = the absoltute value of -5


num2 = 5 
print(round(num2))  #returns 5 
Numfloat = 4.559
print(round(Numfloat)) #rounds it to 5
print(round(Numfloat, 2))

#  sum()

NNums = [1, 2, 3, 4,]
print(sum(NNums))

print(min(NNums))
print(max(NNums))

print(pow(2,3))  #2^3 = 8

x = divmod(5,2)


# str()

print(str(10), type(str(10)))   #converts 10 to a string

print(float("10.5")), type(float("10.5"))





