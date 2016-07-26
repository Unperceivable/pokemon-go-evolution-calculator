#!/usr/bin/python
__author__ = 'Unperceivable'
__module_name__ = "Evolution Calculator"
__module_version__ = "v0.1"
__module_description__ ="Pokemon Go Evolution Calculator"


#Grab Required User Data
print "Welcome to "+ __module_description__
pokemonCount = input("Entre the number of Pokemon: ")
candyCount = input("Entre the number of specie candy you have: ")
evoVal = input("Entre the amount of candies required to evolve that Pokemon: ")

#Calculate evolutions with current candy
firstEvo = int(candyCount/evoVal)
candyRemainder = candyCount%evoVal + firstEvo

secondEvo = firstEvo


#Calculate if more evolutions are possible with secondary candy from evolutions
if candyRemainder >= evoVal:
	bonusEvo = int (candyRemainder/evoVal)
	secondEvo += bonusEvo 
	candyRemainder = candyRemainder%evoVal + bonusEvo

#Output if user has more candy than pokemon to evolve with
if secondEvo > pokemonCount:
	print "You can evolve a maximum of: "+ str(pokemonCount) + " pokemon"
	print "You could evolve at least" + str(secondEvo) + " using the excess" + str(candyRemainder) + "candy if you caught more pokemon"

#Output if user has perfect amount to evolve
elif secondEvo == pokemonCount:
	print "You can evolve exactly: "+ str(secondEvo) + " pokemon with " + str(candyRemainder) +" candy surplus"

#Otherwise, Check maximum user can evolve by transfering excess pokemon  and return result
else:
	transBonus=0
	transPokemon=0
	print (pokemonCount, secondEvo, candyRemainder, (pokemonCount-1) + candyRemainder >= evoVal )
        pokemonCount = pokemonCount - secondEvo
	print pokemonCount
	while (pokemonCount-1) + candyRemainder >= evoVal:
		print (pokemonCount, secondEvo, candyRemainder, (pokemonCount-1) + candyRemainder >= evoVal )
		if transBonus == 0:
			transPokemon+=(evoVal-candyRemainder)
			pokemonCount-(evoVal-candyRemainder)
			candyRemainder=0
		else:
			pokemonCount-=evoVal
			transPokemon+=evoVal
		transBonus+=1



	print "You can evolve a maximum of " + str(secondEvo + transBonus) + " pokemon after transfering excess"

