def BinToDec():

    BinRaw = input("Please enter a binary number:" )
    BinRawList = list(BinRaw)
    Bin = False 
    Dec = 0


	
    #Checks if all items in BinRawList are equal or less than 1 and equal or more than 0.
    if all(i <= "1" and i >= "0" or i == "." or i == "," for i in BinRawList) == True:
        BinComma = []
        BinList = []
        
        while BinRawList:
            BinListPop = BinRawList.pop(0)

            #If the binary number has a comma in it then adds the numbers after comma into another list.
            if any(x in BinListPop for x in [",", "."]):
                while BinRawList:
                    BinListPop = BinRawList.pop(0)
                    BinComma.append(BinListPop)
           
            else:   
                BinList.append(BinListPop)
         
        Bin = True

    else:
        print(BinRaw + " isn't a binary number!")
       



    #If the number is binary then converts the number into decimal.
    if Bin == True:
        while BinList:
            Possision = len(BinList)
            BinListPop = BinList.pop(0)
            DecRaw = 2 ** (0 + Possision - 1) * int(BinListPop) # 2 to the power of possision times the number in that possision
            Dec = Dec + DecRaw
    
	#If the number contains a comma then it does the calculations for it seperatelly.        
        while BinComma:
            PossisionComma = len(BinComma)    
            BinCommaPop = float(BinComma.pop(0))
            DecRaw = BinCommaPop / 2 ** PossisionComma #Binary number devited by 2 to the power of the possision of said binary number 
            Dec = Dec + DecRaw

    print("The Decimal version of " + BinRaw + " is " + str(Dec)) #Wohoo! Finally done! Took me long enough!
