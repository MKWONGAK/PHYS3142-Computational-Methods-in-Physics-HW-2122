#HW1 Q2(c) convert between letters and numbers

from HW1_Q2c_conversion import *
message = 'gkstmdodikbojsydzkpuibtzwuigu'

def convert_message_to_number(x):
    list_ = list(x)
    converted_message = []
    for i in list_:
        converted_message.append(letter_to_number(i))
    return converted_message

def convert_number_to_message(x):
    list_ = list(x)
    converted_message = []
    for i in list_:
        converted_message.append(number_to_letter(i))
    return converted_message

# find a^-1 for a
def inverse(a):
    for i in range(0,26):
        if ((a*i) % 26) == 1:
            return i
    return False

def equations(a_inverse,b,y):
    x = (a_inverse*(y-b)) % 26
    return x


def decipher(x):
    number_message = convert_message_to_number(x)
    for a in range(0,26):
        if inverse(a) != False:
            for b in range(0,26):
                deciphered_number = []
                #decipher the numbers and transfer to letters
                for i in number_message:
                    deciphered_number.append(equations(inverse(a),b,i))
                #check for the first two letters
                tmp = convert_number_to_message(deciphered_number)
                if tmp[0] == 'c' and tmp[1] == 'o':
                    print(''.join(tmp))
                    print('a = ',a,'b = ',b)

                
decipher(message)
        