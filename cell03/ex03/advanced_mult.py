#!/bin/python3
table_since=0
table_till=10
since=0
till=10

for i in range (table_since, table_till +1):
    #Header of each table
    print(f"Table de: {i}",end=" " ) 
    for e in range (since, till + 1):
        print(f" {i * e}" ,end="")
    print()

#for i in range(0,10):
#    print("\n\nMULTIPLICATION TABLE FOR %d\n" %(i))
#    print(f"\n\nMULTIPLICATION TABLE FOR {i}\n")
#    for j in range(1,11):
#        print("%-5d X %5d = %5d" % (i, j, i*j))