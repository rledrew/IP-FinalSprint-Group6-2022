'''
def Menu():
    print()
    print("HAB Taxi Services")
    print("Company Services System")
    print()
    print(" 1. ")
    print(" 2. ")
    print(" 3. ")
    print(" 4. ")
    print(" 5. ")
    print(" 6. ")
    print(" 7. ")
    print(" 8. ")
    print(" 9. Quit Program. ")
    print()
    while True:
        Choice = int(input("Enter a choice (1-9):"))
        if Choice >9:
            print("Choice must be between 1 and 9")
        elif Choice <1:
            print("Choice must be between 1 and 9")
        elif Choice == 1:
            NewEmpMenu()
        elif Choice == 2:
            RevenueMenu()
        elif Choice == 3:
            ExpensesMenu()
        elif Choice == 4:
            RentalsMenu()
        elif Choice == 5:
            EmpPaymentMenu()
        elif Choice == 6:
            ProfitListingMenu()
        elif Choice == 7:
            DriverFinanceMenu()
        elif Choice == 8:
            ReportMenu()
        elif Choice == 9:
            break
        else:
            print('Please enter a valid choice')
'''

