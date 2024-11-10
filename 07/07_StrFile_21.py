Text = input()
uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
Rot13 = ''
while Text != 'end':
    for i in Text:
        if i in uppercase_alphabet:
            e = uppercase_alphabet.find(i)
            s = uppercase_alphabet 
            Rot13 += s[(e+13)%len(uppercase_alphabet)]
        elif i in lowercase_alphabet:
            e = lowercase_alphabet.find(i)
            s = lowercase_alphabet
            Rot13 += s[(e+13)%len(lowercase_alphabet)]
        else: 
            Rot13 += i
    Text = input()
    Rot13 = Rot13 + '\n' + ''
print(Rot13)