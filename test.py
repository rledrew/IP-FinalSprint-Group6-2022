'''
import datetime
while True:
    licnum = input('Enter employee license number here: ').upper()
    licnum = licnum.replace(' ', '')
    licnum = licnum.replace('-', '')
    if licnum[0].isalpha() == False or licnum[1].isalpha() == False or licnum[2].isalpha() == False:
        print('First 3 characters of license plate must be alphabetical')
    elif licnum[3].isdigit() == False or licnum[4].isdigit() == False or licnum[5].isdigit() == False:
        print('Last 3 characters of license plate must be numerical')
    else:
        break
licnumdsp = f'{licnum[0]}{licnum[1]}{licnum[2]} {licnum[3]}{licnum[4]}{licnum[5]}'
print(licnumdsp)
while True:
    licexp = input('Enter employee license expiration date(MM/YY)')
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
licedate = datetime.datetime.strptime(licexp, licensedateformat)
print(licedate)
'''''
expopen = open('expenses.dat', 'a')
            exptransnum = exptransnum.replace('\n', '')
            expopen.write(
                f'{exptransnum}, {transdate}, {drivernum}, {itemnum}, {itemdesc}, {itemcost:.2f}, {itemquan}, \n')