
## Homework for printing firstname and lastname using for loop

```py

list_first_name = [ "Ben", "Devika", "Stuti", "Shivani", "Savita", "Gauri" ]


for name in list_first_name:
    print("{} Saini".format(name))

```


# Lesson June 16th, 2020
# Loops While-Loop

while (covid numbers have not gone to 0):
    #stay at home

while (it is not 3 pm):
    #Stuti please stand one 1 leg

while (I  have not eaten lunch):
    #stay in kitchen and make rotis

```py

from datetime import datetime, time


target_time = time(hour = 04, minute = 27, second = 00)


while datetime.now().time() < target_time:
    print("Stuti, please stand on 1 leg")

```

# Loops While-Loop last homework example

```py

list_first_name = [ "Ben", "Devika", "Stuti", "Shivani", "Savita", "Gauri" ]

counter = 0

while counter < len(list_first_name):
    print("{} Saini".format(list_first_name[counter]))
    counter = counter + 1
```
homework updated by devika
```py
#while loop

num=1
while num < 10:
    print(num)
    num +=1

#program to add natural numbers
num=10
sum=0
num_entered=1

while num_entered <= num:
    sum=sum + num_entered
    num_entered = num_entered + 1
    print("the sum is{}.format"(sum))

```
