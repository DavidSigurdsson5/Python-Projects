
while True:
    income = int(input("Please enter your income: "))
    
    if income < 0:
        break
    

    #First I define all the variables. With denmark I make a seperate denmark_income variable because denmark's tax 
    # will be in a while loop that affects the income value. Thats also why I define the denmark_tax_rate variable.
    norway_tax = 0
    us_tax = 0
    denmark_tax = 0
    denmark_income = income
    denmark_tax_rate = 0
    
    #Canada tax
    canada_tax = income * 0.26

    # Here I arbitrarily make canada_tax the lowest_tax just to define that variable I could use any other tax variable 
    # for this. Then I make the lowest_alphabetical an empty string where the lowest_tax country/countries will be added
    # to be printed.
    lowest_tax = canada_tax
    lowest_alphabetical = ""
    
    #Norway tax
    if income <= 3000:
        norway_tax = income * 0.1
    else:
        norway_tax = (3000 * 0.1) + ((income-3000) * 0.4)
    
    
    #US tax
    if income <= 1500:
        us_tax = income * 0.12
    elif income <= 6000:
        us_tax = income * 0.25
    elif income <= 10000:
        us_tax = income * 0.38
    else:
        us_tax = income * 0.15



    #Denmark tax
    # Denmark is special so I make a while loop that in each loop subtracts 1000 from the income and 
    # adds 0.1 to the tax rate to get into the next tax bracket. 
    while denmark_income > 0:
        if denmark_income > 1000:
            denmark_tax += 1000 * denmark_tax_rate
            denmark_income -= 1000
        else:
            denmark_tax += denmark_income * denmark_tax_rate
            denmark_income = 0
        denmark_tax_rate += 0.1



    # Here I compare the country tax values to find the lowest value of tax paid. I don't check canada_tax 
    # because it was defined as the lowest tax in the beginning. 
    if denmark_tax < lowest_tax:
        lowest_tax = denmark_tax
    if norway_tax < lowest_tax:
        lowest_tax = norway_tax
    if us_tax < lowest_tax:
        lowest_tax = us_tax
        

    # Now I check which tax is the lowest and if it is the country's name gets added to the lowest_alphabetical variable.
    # The if sentences are ordered in alphabetical order so that the countries get added in alphabetical order. 
    if lowest_tax == canada_tax:
        lowest_alphabetical += "Canada "
    if lowest_tax == denmark_tax:
        lowest_alphabetical += "Denmark "
    if lowest_tax == norway_tax:
        lowest_alphabetical += "Norway "
    if lowest_tax == us_tax:
        lowest_alphabetical += "USA "

    print("Lowest tax: ",lowest_tax)
    print(lowest_alphabetical)
