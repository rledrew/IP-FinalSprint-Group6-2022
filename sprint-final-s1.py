# Opening files & setting globals
global transnum,nextdrivernum,MONTHSTANDFEE,DAILYFEE,WEEKLYFEE,HST_RATE
defaultread = open('Defaults.dat')
defaultlines = defaultread.readlines()
transnum = defaultlines[0]
nextdrivernum = defaultlines[1]
nextdrivernum = int(nextdrivernum)
MONTHSTANDFEE = defaultlines[2]
DAILYFEE = defaultlines[3]
WEEKLYFEE = defaultlines[4]
HST_RATE = defaultlines[5]

# Functions
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def NewEmpMenu():
    while True:
        global nextdrivernum
        empfileread = open('employees.dat', 'a')
        driver_num = nextdrivernum
        nextdrivernum += 1
        replace_line('Defaults.dat', 1, f'{nextdrivernum}\n')
        break
# def RevenueMenu():

# Menu setup
'''
def menu():
    print()
    print("HAB Taxi Services")
    print("Company Services System")
    print()
    print(" 1. Enter a New Employee (Drive) ")
    print(" 2. Enter Company Revenues ")
    print(" 3. Company Expenses ")
    print(" 4. Track Car Rentals ")
    print(" 5. Record Employee Payment ")
    print(" 6. Print Company Pro  fit Listing ")
    print(" 7. Print Driver Financial Listing ")
    print(" 8. OurReport ")
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
