max_no = input("Enter the number under which prime numbers will be populated: ")

for i in range(2,int(max_no)):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print("prime number: {}".format(i))