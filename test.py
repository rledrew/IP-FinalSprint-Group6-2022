import datetime
date = '2022-01-01'
formatdata = '%Y-%m-%d'
testday = datetime.datetime.strptime(date, formatdata)
print(testday)
tday = datetime.date.today()
print(tday)
if testday.day == 1:
    print('It is the first of the month')
else:
    print('No')