

#prompt user for the phrase
user_word_input = input("Put a word in and see how many vowels there are: ").lower()
#this is the vowel array / bank
vowels = ["a", "e", "i" ,"o" ,"u"]

# counts to check how many vowels

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
vowel_count = 0
#check if there are any and how many vowels
for i in user_word_input:
    for j in vowels:
        if i == j:
            vowel_count += 1
            break
if vowel_count > 0:
    vowel_num= str(vowel_count)
    print("You have " + vowel_num + " Vowels")
else:
    print("no vowels")


# goes through each letter in the user word to see if they match and how many
for letter in user_word_input:
    if letter == 'a':
        a_count += 1
    elif letter == 'e':
        e_count += 1
    elif letter == 'i':
        i_count += 1
    elif letter == 'o':
        o_count += 1
    elif letter == 'u':
        u_count += 1


# Print the count for each matching vowel even if they dont match a zero will display
print(f'a = "{a_count}"')
print(f'e = "{e_count}"')
print(f'i = "{i_count}"')
print(f'o = "{o_count}"')
print(f'u = "{u_count}"')




