ff = open('registrations_.txt', 'r', encoding='utf-8')
v1 = open('registrations_good.log', 'w', encoding='utf-8')
z1 = open('registrations_bad.log', 'w', encoding='utf-8')
for line in ff.readlines():
    line1 = line.split()
    if len(line1) == 3 and line1[0].isalpha() == True:
        if line1[1].find('@') != -1 and line1[1].find('.') != -1:
            if int(line1[2]) >= 10 and int(line1[2]) <= 90:
                v1.write(line1[0] + ' ' + line1[1] + ' ' + line1[2] + '\n')
    elif len(line1) == 3:
        z1.write(line1[0] + ' ' + line1[1] + ' ' + line1[2] + '\n')
    elif len(line1) == 2:
        z1.write(line1[0] + ' ' + line1[1] + '\n')
    elif len(line1) == 1:
        z1.write(line1[0] + '\n')
    elif len(line1) == None:
        pass

        # print(line1)
        # print(line)
        # v.close()
z1.close()
v1.close()


# v1 = open('registrations_bad.log','r', encoding='utf-8')
# print(v1.read())

class NotNameError(Exception):
    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message


class NotEmailError(Exception):
    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message


def valid(n):
    with open('registrations_bad.log', 'r', encoding='utf-8') as bad:
        first_line = bad.readlines()
        line2 = first_line[n].split()
        print(line2)
        # print(len(line2))
        if len(line2) < 3:
            raise ValueError('Не полный набор данных')
        elif len(line2) == 3:
            if line[2].isdigit() == True:
                if int(line2[2]) < 10 or int(line2[2]) > 90:
                    raise ValueError('поле возраст НЕ является числом от 10 до 99')
            if line2[0].isalpha() != True:
                raise NotNameError('поле имени содержит НЕ только буквы')
            if line2[1].find('@') == -1 and line2[1].find('.') == -1:
                raise NotEmailError('поле email НЕ содержит @ и .(точку)')
    return 'Ошибки нет'


# valid(9)
try:
    valid(56)
except ValueError as exp:
    print(exp)
except NotNameError as exp:
    print(exp)
except NotEmailError as exp:
    print(exp)