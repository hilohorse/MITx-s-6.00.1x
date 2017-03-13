"""

Final exam code for MIT online course Introduction to Computer Science and Programming Using Python - 6.00.1x

"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if  0 <= int(us_num) <= 10:
        return trans[us_num]
    elif 10 < int(us_num) <= 19:
        return 'shi ' + trans[us_num[1]]
    elif 19 < int(us_num) <= 99:
        if us_num[1] == '0':
            return trans[us_num[0]] + ' shi'
        else:
            return trans[us_num[0]] + ' shi ' + trans[us_num[1]]

