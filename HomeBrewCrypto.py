from string import ascii_lowercase
from sys import exit

smile_alpha = [':)', ';)', ':D', ':(', ':O', ':-P', ':X', ':-[', ':-]', ':{', ':}', '8)', '8(', ':S', 'o-o', '(O_O)',
               ':|', ':=)', ':=(', ':3', '*_*', '*-*', 'o=o', '@_@', '^-^', '$_$']  # smile alphabet

eng_alpha = ascii_lowercase  # English alphabet
zipped_dict = zip(eng_alpha, smile_alpha)
my_dict = dict(zipped_dict)

my_table = []
for i in smile_alpha:
    my_table.append([])
    x = smile_alpha.index(i)
    for k in smile_alpha:
        y = smile_alpha.index(k)
        new_index = (x + y + 1) * 7 % 26
        my_table[-1].append(smile_alpha[new_index])

print(*my_table, sep='\n')
word = input("Plain text: ")
key = input("Key: ")
word_len = len(word)
key_len = len(key)
if word_len == 0 or key_len == 0:
    print("Empty text or key. Exit.")
    exit()

if key_len > word_len:
    key = key[:word_len]
    # if the key is longer, I will shorten it down to the key's length
else:
    x = word_len // key_len
    y = word_len % key_len
    key = key * x + key[:y]  # if the key is shorter, I will repeatedly write the key up to plain text's length

z = len(word)
ciphertext = ''  # the result
for i in range(z):  # encryption process starts
    try:
        word_smile = my_dict[word[i]]
        key_smile = my_dict[key[i]]  # corresponding smile for letters in the plain text and the key
        row = smile_alpha.index(word_smile)
        col = smile_alpha.index(key_smile)  # their indexes in the smile alphabet
        ciphertext += my_table[row][col] + ' '
    except KeyError:
        print("Invalid character. Exit.")
        exit()
print('Ciphertext: ', ciphertext)
