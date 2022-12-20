def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def namevalidate(firstname):
    while True:
        firstname = input('Enter employee first name here:')
        if firstname.isalpha() == False:
            print('Please input a valid name')
        else:
            break