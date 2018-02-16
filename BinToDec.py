def BinToDec():

    BinRaw = input("Please enter a binary number:" )
    BinList = list(BinRaw)
    Bin = False 
    Dec = 0




    #Checks if all items in BinRawList are equal or less than 1 and equal or more than 0  
    if all(i <= "1" and i >= "0" for i in BinList) == True:
        Bin = True
    
    #Does the same thing as the if statement but also checks for dots and commass 
    elif all(i <= "1" and i >= "0" or i == "." or i == "," for i in BinList) == True:
        BinAfterComma = []
        BinPreComma = []
        
        while BinList:
            BinListPop = BinList.pop(0)

            if any(x in BinListPop for x in [",", "."]):
                while BinList:
                    BinListPop = BinList.pop(0)
                    BinAfterComma.append(BinListPop)
           
            else:   
                BinPreComma.append(BinListPop)
         
        Comma = True

    else:
        print(BinRaw + " isn't a binary number!")
       




	#If the number is binary and there's a comma/dot then converts the number into decimal.
	if Comma == True:
		
		while BinPreComma:
			Possision = len(BinPreComma)
			PreCommaPop = BinPreComma.pop(0)
			DecRaw = 2 ** (0 + Possision - 1) * int(PreCommaPop) # 2 to the power of possision times the number in that possision
			Dec = Dec + DecRaw
			
		while BinAfterComma:
			PossisionComma = len(BinAfterComma)	
			AfterCommaPop = float(BinAfterComma.pop(0))
			DecRaw = AfterCommaPop / 2 ** PossisionComma #Binary number devited by 2 to the power of the possision of said binary number 
			Dec = Dec + DecRaw





#If no Comma is present and if number is binary then converts it into a decimal number
	elif Bin == True:
		
		while BinList:
			Possision = len(BinList)
			BinListPop = int(BinList.pop(0))  
			
			DecRaw = 2 ** (0 + Possision -1) * BinListPop # 2 to the power of possision times the number in that possision
			Dec = Dec + DecRaw
			
	print("The Decimal version of " + BinRaw + " is " + str(Dec)) #Wohoo! Finally done!