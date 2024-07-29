def name_printer(first, middle, last):
    print(f"Your full name is: {first} {middle} {last}")

def greeting(name = "World"):
    print(f"Hello, {name}")
greeting()
greeting("Jeremiah the King of NOthing")

# args*
def vet_hands(staff, *vols): #Create a (f) for dispalying who is working between the DRs and volunteers
    print(f"On staff today , we have {staff[0]} and {staff[1]}.")  #Only have 2 Drs do indexes are 0 and 1
    if vols: #Use this because we don't know how many volunteers there are( If means , if there are any , then do this)
        print("The volunteers are: ")  #Print the names 
        #for vol in vols: #Makes it print out each volunteer and lists them on seperate lines 
            #
            # 
            # 00print(vol)   #print name of volunteer
       
vet_hands(["Dr Adam","Dr Jones"], "John","Jane","Joe", "Billy")  #Call the function and pass in the names of the Drs and volunteers






