```list_no=[289,345,113,900]


sum_bucket=0


for index in range(0,len(list_no)):

    print(list_no[index])
    sum_bucket=sum_bucket + list_no[index]

    ==================================
    First Run
    index 0
    289 print
    sum_bucket = 0 + 289 = 289
    ==================================
    Second Run
    index 1
    345 print
    sum_bucket = 289 + 345 = 634
    ==================================
    Third Run
    index 2
    113 print
    sum_bucket = 634 + 113 = 774
    ==================================
    Fourth Run
    index = 3
    900 print
    sum_bucket = 774 + 900 = 1674



print(sum_bucket) --> 1674
```
