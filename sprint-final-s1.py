# Importing Libraries
global dtime
from functions import replace_line
import datetime as dtime

# Setting Date variables
tday = dtime.date.today()
# Opening files & setting globals
global transnum, nextdrivernum, MONTHSTANDFEE, DAILYFEE, WEEKLYFEE, HST_RATE
defaultread = open('Defaults.dat')
defaultlines = defaultread.readlines()
transnum = defaultlines[0]
nextdrivernum = defaultlines[1]
nextdrivernum = nextdrivernum.replace('\n', '')
nextdrivernum = float(nextdrivernum)
MONTHSTANDFEE = defaultlines[2]
MONTHSTANDFEE = float(MONTHSTANDFEE)
DAILYFEE = defaultlines[3]
WEEKLYFEE = defaultlines[4]
HST_RATE = defaultlines[5]
HST_RATE = float(HST_RATE)
PreviousDate = defaultlines[6]
revread = open('revenue.dat', 'a')
openemployees = open('employees.dat')
employeeslist = openemployees.readlines()
numofemps = len(employeeslist)
counter = 0
if tday.day == 1 and tday != PreviousDate:
    while counter < numofemps:
        employeeline = employeeslist[counter]
        employeelinelist = employeeline.split(',')
        empnumber = employeelinelist[0]
        standfeetax = MONTHSTANDFEE * HST_RATE
        standfeetotal = MONTHSTANDFEE + standfeetax
        revtransnum = transnum.replace('\n', '')
        revreport = f'{revtransnum}, {tday}, Monthly Stand Fees, {empnumber}, {MONTHSTANDFEE}, {standfeetax}, {standfeetotal}\n'
        revread.write(revreport)
        oldempbaldue = employeelinelist[9]
        oldempbaldue = float(oldempbaldue)
        standfeetotal = float(standfeetotal)
        newempbaldue = oldempbaldue + standfeetotal
        replace_line('employees.dat', counter, f'{employeelinelist[0]},{employeelinelist[1]},{employeelinelist[2]},\
{employeelinelist[3]},{employeelinelist[4]},{employeelinelist[5]},{employeelinelist[6]},\
{employeelinelist[7]},{employeelinelist[8]}, {newempbaldue:.2f}\n')
        transnum = int(transnum)
        transnum += 1
        transnum = str(transnum)
        replace_line('Defaults.dat', 0, f'{transnum}\n')
        counter += 1
if tday != PreviousDate:
    replace_line('Defaults.dat', 6, f'{tday}')


# Functions

def NewEmpMenu():
    global nextdrivernum
    empfileread = open('employees.dat', 'a')
    while True:
        driver_num = nextdrivernum
        nextdrivernum += 1
        replace_line('Defaults.dat', 1, f'{nextdrivernum}\n')
        while True:
            firstname = input('Enter employee first name here: ').title()
            if firstname.isalpha() == False:
                print('Please input a valid name')
            else:
                break
        while True:
            lastname = input('Enter employee last name here: ').title()
            if lastname.isalpha() == False:
                print('Please input a valid name')
            else:
                break

        empaddress = input('Enter employee address here(## Street): ').title()
        empaddress = empaddress.replace(',', '')
        while True:
            empphone = input('Enter employee phone number here(###-###-####): ')
            empphone = empphone.replace(' ', '')
            empphone = empphone.replace('-', '')
            if empphone.isnumeric() == False:
                print('Phone number must contain only numbers and dashes')
            elif len(empphone) != 10:
                print('Phone number must be 10 digits long')
            else:
                break

        empphonedsp = f'{empphone[0]}{empphone[1]}{empphone[2]}-{empphone[3]}{empphone[4]}{empphone[5]}' \
                      f'-{empphone[6]}{empphone[7]}{empphone[8]}{empphone[9]}'

        while True:
            licnum = input('Enter employee license plate number here: ').upper()
            licnum = licnum.replace(' ', '')
            licnum = licnum.replace('-', '')

            if licnum[0].isalpha() == False or licnum[1].isalpha() == False or licnum[2].isalpha() == False:
                print('First 3 characters of license plate must be alphabetical')
            elif licnum[3].isdigit() == False or licnum[4].isdigit() == False or licnum[5].isdigit() == False:
                print('Last 3 characters of license plate must be numerical')
            elif len(licnum) != 6:
                print('Plate number must be 6 characters long')
            else:
                break
        licnumdsp = f'{licnum[0]}{licnum[1]}{licnum[2]} {licnum[3]}{licnum[4]}{licnum[5]}'

        while True:
            licexp = input('Enter employee license expiration date(MM/YY): ')
            licexp = licexp.replace(' ', '')
            licexp = licexp.replace('/', '')
            licexp = licexp.replace('-', '')
            if len(licexp) != 4:
                print('License expiry must contain 4 digits (MM/YY)')
            if licexp.isdigit() == False:
                print('License expiry date must only contain numbers (MM/YY)')
            else:
                break

        licensedateformat = '%m%y'
        licedate = dtime.datetime.strptime(licexp, licensedateformat)
        while True:
            polcomp = input("Enter the name of the insurance company with whom the employee has a policy: ")
            polcompval = polcomp.replace(' ', '')
            if polcompval.isalpha() == False:
                print('Company name must only contain letters')
            else:
                break
        while True:
            polnum = input('Enter employee insurance policy number here: ')
            polnum = polnum.replace(' ', '')
            if polnum.isdigit() == False:
                print('Policy Number must contain only numbers')
            else:
                break
        while True:
            carinq = input('Will the employee be renting a car?(Y/N): ').upper()
            if carinq[0] == 'Y':
                carinq = 'Y'
                break
            elif carinq[0] == 'N':
                carinq = 'N'
                break
            else:
                print('Please enter a valid input')
        while True:
            baldue = input('Enter employee balance due here: ')
            balval = baldue.replace('.', '')
            if balval.isnumeric() == False:
                print('Please enter only numbers and periods for the balance')
            else:
                break
        empfileread.write(f'\n{driver_num}, {firstname} {lastname}, {empaddress}, {empphone}, {licnumdsp}, {licexp},'
                          f' {polcomp}, {polnum}, {carinq}, {baldue}')
        while True:
            selection = input('Would you like to return to main menu?(Y/N): ').upper()
            if selection != 'Y' and selection != 'N':
                print('Please enter a valid input')
            else:
                break
        if selection == 'Y':
            break
        elif selection == 'N':
            pass


def RevenueMenu():
    global transnum
    while True:
        revtransnum1 = transnum
        transnum = int(transnum)
        transnum += 1
        transnum = str(transnum)
        replace_line('Defaults.dat', 0, f'{transnum}\n')
        dateformat = '%Y-%m-%d'
        while True:
            transdate = input('Enter date of transaction here(YYYY-MM-DD): ')
            transdateval = transdate.replace('-', '')
            if transdateval.isdigit() == False:
                print('Make sure date is in correct format (YYYYY-MM-DD)')
            else:
                break
        transdatestrptime = dtime.datetime.strptime(transdate, dateformat)
        transdesc = input('Enter description of transaction here: ')
        if len(transdesc) == 0:
            transdesc = 'N/A'
        while True:
            drivernum = input('Enter Driver number here: ')
            if drivernum.isnumeric() == False:
                print('Driver number must contain only numbers')
            else:
                break
        while True:
            transamt = input('Enter transaction amount here: ')
            transamt = transamt.replace('$', '')
            transval = transamt.replace('.', '')
            if transval.isnumeric() == False:
                print('Please enter a valid dollar amount (##.##)')
            else:
                break
        transamt = float(transamt)
        revhst = transamt * HST_RATE
        revtotal = transamt + revhst
        revopen = open('revenue.dat', 'a')
        revtransnum1 = revtransnum1.replace('\n', '')
        revopen.write(f'{revtransnum1}, {transdate}, {transdesc}, {drivernum}, {transamt:.2f}, {revhst:.2f}, {revtotal:.2f}\n')
        while True:
            selection = input('Would you like to return to main menu?(Y/N): ').upper()
            if selection != 'Y' and selection != 'N':
                print('Please enter a valid input')
            else:
                break
        if selection == 'Y':
            break
        elif selection == 'N':
            pass

'''
# Menu setup

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