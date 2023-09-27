phone_number = input('Phone number: ')
digits= {
    '0':'Zero',
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine'
}
number = ''
for digit in phone_number:
   number += digits.get(digit)
print(number)