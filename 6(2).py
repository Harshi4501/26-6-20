def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))
xyc abz
In [23]:
user_input = input("Which is your favourite pet? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())