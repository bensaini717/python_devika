# Lesson, June 17th, 2020

## Concept Dictionary
## key ----> value/meaning

## Example: Ben ----> bensaini7@gmail


```py
dictionary_email_address = {}
dictionary_email_address['Ben'] = 'bensaini7@gmail'
dictionary_email_address['Devika'] = 'devika@gmail'
dictionary_email_address['Bentley'] = 'bentley@gmail'
dictionary_email_address['Mercedes'] = 'mercedes@gmail'
dictionary_email_address['Ben'] = 'shivani@gmail'

print(len(dictionary_email_address))

list_of_keys = dictionary_email_address.keys()

counter = 0

while counter < len(list_of_keys):
    key = list_of_keys[counter]
    value = dictionary_email_address[key]
    print("Key is {} and Value is {}".format(key, value))
    counter = counter + 1
```
