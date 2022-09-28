rate = int(input("Interest Rate: "))
monthly = int(input("Monthly Ammortization: "))
monthsInYear = int(input("Years in month: "))
years = int(input("How many years: "))
initialPrincipal = int(input("Initial principal: "))

def calcInterest(totalValue, currentYears):
	if (currentYears <= 0):
		print("Savings of " + str(monthly) + " monthly for " + str(years) + " years at the rate of " + str(rate) + "% is a total of: " + str(totalValue))
	else:
		totalWithYTD = totalValue + (monthly*monthsInYear)
		newTotalWithInterest = totalWithYTD + (totalWithYTD*(rate/100))
		calcInterest(newTotalWithInterest, currentYears-1)

calcInterest(initialPrincipal, years)
