#####################
# Secura24 Decryptor #
#####################

import re

user_input = input()
print("Key:")
key = input()

possible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"§$%&/()=?+*#-_.:,;<>@ '
chars_to_use = possible_chars
encrypted_chars = ''

sort_key = int(key[-1])
key_list = re.findall(r'\d+', key)
key_list.pop(-1)

def sort_chars(list, char1, char2):
    sort_elements = list[char1], list[char2]
    list[char2], list[char1] = sort_elements
    return list

sort_number = 0
while sort_number + sort_key < len(key_list):
    sort_chars(key_list, sort_number + sort_key, sort_number)
    sort_number += sort_key * 2

for char in key_list:
    encrypted_chars += chars_to_use[int(char)]
    chars_to_use = chars_to_use[:int(char)] + chars_to_use[int(char)+1:]

decrypted_result = ''

for char in user_input:
    char_index = encrypted_chars.find(char)
    if (char_index != -1):
        decrypted_result += possible_chars[char_index]

print("Result: " + decrypted_result)
