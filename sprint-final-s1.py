# Importing Libraries
from functions import replace_line
from functions import namevalidate
import datetime
import datetime as dtime
# Setting Date variables
tday = dtime.date.today()
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
PreviousDate = defaultlines[6]
if tday != PreviousDate:
    replace_line('Defaults.dat', 6, f'{tday}')
revread = open('revenue.dat', 'a')
if tday.day == 1:
    revread.write(f'{transnum}')

# Functions

def NewEmpMenu():
    global nextdrivernum
    empfileread = open('employees.dat', 'a')
    driver_num = nextdrivernum
    nextdrivernum += 1
    replace_line('Defaults.dat', 1, f'{nextdrivernum}\n')
    while True:
        firstname = input('Enter employee first name here: ')
        if firstname.isalpha() == False:
            print('Please input a valid name')
        else:
            break
    while True:
        lastname = input('Enter employee last name here: ')
        if lastname.isalpha() == False:
            print('Please input a valid name')
        else:
            break

    empaddress = input('Enter employee address here(## Street, City): ')
    while True:
        empphone = input('Enter employee phone number here(###-###-####): ')
        empphone = empphone.replace(' ', '')
        empphone = empphone.replace('-', '')
        if empphone.isnumeric() == False:
            print('Phone number must contain only numbers and dashes')
        else:
            break
    empphonedsp = f'{empphone[0]}{empphone[1]}{empphone[2]}-{empphone[3]}{empphone[4]}{empphone[5]}' \
                      f'-{empphone[6]}{empphone[7]}{empphone[8]}{empphone[9]}'



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
NewEmpMenu()