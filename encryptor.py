#####################
# Secura24 Encryptor #
#####################

import random

possible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"§$%&/()=?+*#-_.:,;<>@ '
key_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"§$%&/()=?+*#-_.:,;<>@'
encrypted_chars = ''

chars_to_use = possible_chars
key_list = []
sort_key = random.randint(0, 4)
key = ""

for char in possible_chars:
    random_char = random.randint(0, len(chars_to_use) - 1)
    encrypted_chars += chars_to_use[random_char]
    chars_to_use = chars_to_use[:random_char] + chars_to_use[random_char+1:]
    key_list.append(str(random_char))

def sort_chars(list, char1, char2):
    sort_elements = list[char1], list[char2]
    list[char2], list[char1] = sort_elements
    return list

sort_number = 0
while sort_number + sort_key < len(key_list):
    sort_chars(key_list, sort_number, sort_number + sort_key)
    sort_number += sort_key * 2

for item in key_list:
    key += str(item) + key_chars[random.randint(0, len(key_chars) - 1)]
key += str(sort_key)

user_input = input()
encrypted_result = ""

for char in user_input:
    char_index = possible_chars.find(char)
    if (char_index != -1):
        encrypted_result += encrypted_chars[char_index]
    
print(encrypted_result)
print("Key: " + key)
