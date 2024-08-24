# Description: Keeps track of used car sales and displays a formatted receipt and payment plans.
# Date: February 7, 2024
# Author: Nasser Ali

# Import libraries
import datetime

# Define program constants.
LOW_LICENSE_FEE = 75.00
HIGH_LICENSE_FEE = 165.00
TRANSFER_RATE = 0.01
LUXURY_TAX_RATE = 0.016
HST_RATE = 0.15
ANNUAL_FINANCING_FEE = 39.99

# Main program.
while True:
    print()
    # Gather user input.
    while True:
        customerFirstName = input(
            "Please enter the customer's first name (enter 'END' to terminate the program): ").title()
        if customerFirstName == "":
            print("Data entry error - first name field must not be empty.")
        else:
            break

    # Checks if user wants to continue using the program based on input for first name.
    if customerFirstName == "End":
        break

    while True:
        customerLastName = input(
            "Please enter the customer's last name: ").title()
        if customerLastName == "":
            print("Data entry error - first name field must not be empty.")
        else:
            break

    while True:
        customerPhoneNumber = input(
            "Please enter the customer's phone number: ")
        if customerPhoneNumber == "":
            print("Data entry error - phone number field must not be empty.")
        elif len(customerPhoneNumber) != 10:
            print("Data entry error - phone number must be 10 digits.")
        elif customerPhoneNumber.isdigit() == False:
            print("Data entry error - phone number must be 10 digits.")
        else:
            break

    while True:
        customerPlateNumber = input(
            "Please enter the customer's plate number (XXX999): ").upper()
        if customerPlateNumber == "":
            print("Data entry error - plate number field must not be empty.")
        elif len(customerPlateNumber) != 6:
            print("Data entry error - plate number must be 6 characters.")
        elif customerPlateNumber[0:3].isalpha() == False:
            print(
                "Data entry error - first three characters of the plate number must be letters.")
        elif customerPlateNumber[3:6].isdigit() == False:
            print(
                "Data entry error - last three characters of the plate number must be numbers.")
        else:
            break

    customerAddress = input("Please enter the customer's street address: ")
    customerCity = input("Please enter the customer's city: ")
    customerProvince = input("Please enter the customer's province (XX): ")
    customerPostalCode = input(
        "Please enter the customer's postal code (X#X#X#): ")

    carMake = input("Please enter the car make (e.g., Toyota): ")
    carModel = input("Please enter the car model (e.g., Corolla): ")
    carYear = input("Please enter the car year (e.g., 2018): ")

    while True:
        try:
            sellingPrice = input(
                "Please enter the car's selling price (must not exceed $50,0000): ")
            sellingPrice = sellingPrice.replace(",", "")
            sellingPrice = sellingPrice.replace(" ", "")
            sellingPrice = sellingPrice.replace("$", "")
            sellingPrice = float(sellingPrice)
        except:
            print(
                "Data Entry Error - the car's selling price must only include digits.")
        else:
            break

    while True:
        try:
            tradeInPrice = input(
                "Please enter the amount of the trade in (must not exceed the selling price): ")
            tradeInPrice = tradeInPrice.replace(",", "")
            tradeInPrice = tradeInPrice.replace(" ", "")
            tradeInPrice = tradeInPrice.replace("$", "")
            tradeInPrice = float(tradeInPrice)
        except:
            print(
                "Data Entry Error - the car's selling price must only include digits.")
        else:
            if tradeInPrice > sellingPrice:
                print(
                    "Data Entry Error - the amount of trade in must not exceed selling price.")
            else:
                break

    salespersonName = input("Please enter the salesperson's name: ").title()

    # Performs required calculations.
    priceAfterTrade = sellingPrice - tradeInPrice

    if priceAfterTrade >= 5000.00:
        licenseFee = LOW_LICENSE_FEE
    else:
        licenseFee = HIGH_LICENSE_FEE

    if priceAfterTrade >= 20000:
        transferFee = sellingPrice * TRANSFER_RATE
    else:
        transferFee = (sellingPrice * TRANSFER_RATE) + \
            (sellingPrice + LUXURY_TAX_RATE)

    subtotalCost = priceAfterTrade + licenseFee + transferFee
    taxCost = subtotalCost * HST_RATE
    totalSalesCost = subtotalCost + taxCost

    # Initializes and prepares required date values.
    currentDate = datetime.datetime.now()
    thirtyDaysFromCurrent = currentDate + datetime.timedelta(days=30)

    # Formats values for output.
    customerInitials = f"{customerFirstName[0]}{customerLastName[0]}"
    receiptID = f"{
        customerInitials}-{customerPhoneNumber[6:11]}-{customerPlateNumber[3:6]}"

    customerAddressPart2 = customerCity + ", " + \
        customerProvince + " " + customerPostalCode
    carDetailsDsp = carYear + " " + carMake + " " + carModel
    sellingPriceDsp = "${:,.2f}".format(sellingPrice)
    tradeInPriceDsp = "${:,.2f}".format(tradeInPrice)
    priceAfterTradeDsp = "${:,.2f}".format(priceAfterTrade)
    licenseFeeDsp = "${:,.2f}".format(licenseFee)
    transferFeeDsp = "${:,.2f}".format(transferFee)
    subtotalCostDsp = "${:,.2f}".format(subtotalCost)
    taxCostDsp = "${:,.2f}".format(taxCost)
    totalSalesCostDsp = "${:,.2f}".format(totalSalesCost)

    # Formats dates for output.
    invoiceDateTop = f"{currentDate.strftime("%b %d, %Y")}"
    invoiceDateBottom = f"{currentDate.strftime("%d-%b-%y")}"
    firstPaymentDate = f"{thirtyDaysFromCurrent.strftime("%d-%b-%y")}"

    # Display results.
    print()
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"  Honest Harry Car Sales                            Invoice Date:   {
          invoiceDateTop:<12s}")
    print(f"  Used Car Sale and Receipt                         Receipt No:      {
          receiptID:<11s}")
    print()
    print(f"                                              Sale Price:             {
          sellingPriceDsp:>10s}")
    print(f"  Sold to:                                    Trade Allowance:        {
          tradeInPriceDsp:>10s}")
    print(f"                                              ----------------------------------")
    print(f"       {customerInitials[0]}. {
          customerLastName:<27s}         Price after trade:      {priceAfterTradeDsp:>10s}")
    print(f"       {customerAddress:<29s}          License Fee:            {
          licenseFeeDsp:>10s}")
    print(f"       {customerAddressPart2:<29s}          Transfer Fee:           {
          transferFeeDsp:>10s}")
    print(f"                                              ----------------------------------")
    print(f"  Car Details:                                Subtotal:               {
          subtotalCostDsp:>10s}")
    print(f"                                              HST:                    {
          taxCostDsp:>10s}")
    print(
        f"       {carDetailsDsp:<29}          ----------------------------------")
    print(f"                                              Total sales price:      {
          totalSalesCostDsp:>10s}")
    print()
    print(f"  ------------------------------------------------------------------------------")
    print()
    print(f"                                    Financing     Total        Monthly")
    print(f"          # Years    # Payments        Fee        Price        Payment")
    print(f"          ------------------------------------------------------------")
    # Calculates and displays values for payment options.
    for numberOfYears in range(1, 5):
        numberOfMonthlyPayments = numberOfYears * 12
        totalFinancingFee = numberOfYears * ANNUAL_FINANCING_FEE
        totalFinancingPrice = totalSalesCost + totalFinancingFee
        monthlyFinancingPayment = totalFinancingPrice / numberOfMonthlyPayments

        # Formats financing values for output.
        totalFinancingFeeDsp = "${:,.2f}".format(totalFinancingFee)
        totalFinancingPriceDsp = "${:,.2f}".format(totalFinancingPrice)
        numberOfMonthlyPaymentsDsp = "${:,.2f}".format(numberOfMonthlyPayments)

        # Displays financing results for all payment options.
        print(f"             {numberOfYears:>1d}           {numberOfMonthlyPayments:>2d}          {
            totalFinancingFeeDsp:>7s}    {totalFinancingPriceDsp:>10s}  {numberOfMonthlyPaymentsDsp:>10s}")
    print(f"          ------------------------------------------------------------")
    print(f"          Invoice Date: {
          invoiceDateBottom:<9s}        First payment date: {firstPaymentDate:<9s}")
    print()
    print(f"  ------------------------------------------------------------------------------")
    print(f"                        Best used cars at the best prices!                      ")
    print()


# Housekeeping.
print()
print("Thank you for using the program")
print("       Have a great day!       ")
print()
