#name=input('Enter name')
#print("My name is ",name)

#1 SUM
#n1=int(input('Enter num1:'))
#n2=int(input('Enter num2:'))
#ans=n1+n2
#print("The sum is ",ans)
#END


#2 IF/ELSE STATEMENTS
#n1=40
#n2=20
#(1) IF
#if n1>n2:
#   print("n1 is the greatest")

#if n2>n1:
#    print("n2 is greater than n1")

#(2) IF/ELSE
#if n1>n2:
#   print("n1 is the greatest")

#else:
#   print("n2 is greater than n1")

#(3) IF ELIF ELSE
#if n1==n2:
#   print("Both the numbers are equal")
#elif n1>n2:
#    print("n1 is greater than n2")
#else:
#    print("n2 is greater than n1")

#(4) IF/IF
#n1=-20

#if n1>0:
#    if n1==0:
#        print("n1 is zero")
#    else:
#        print("n1 is a positive number")
#else:
#    print("n1 is a negative number")
#END


#3 LOOPS
#(1) WHILE LOOP
#i=2
#while i<=10:
#    print("The value is ",i)
#    i +=2

#(2) FOR LOOP
#for i in 'Hello':
#    print("The value is ",i)

#l1=[20,40,'Hello']
#print(l1)

#for i in l1:
#    print("The value is ",i)
#END


#4 RANGE FUNCTION
#(1) EXAMPLE
#for i in range(20):
#    print("The value is ",i)

#for j in range(2,10):
#    print("The value is ",j)

#for k in range(2,10,2):
#    print("The value is ",k)

#(2) EXAMPLE
#l1=[20,40,'HELLO']
#print(l1)

#for i in l1:
#    print("The value is ",i)

#for j in range(len(l1)):
#    print("The value is ",l1[j])
#END


#5 LOOP WITH ELSE
#l1=[20,40,'HELLO']
#print(l1)

#for i in l1:
#    print("The value is ",i)

#for j in range(len(l1)):
#    print("The value is ",l1[j])

#else:
#    print("The end of the loop")
#END


#6 "BREAK" AND "CONTINUE" STATEMENTS
#(1) BREAK
#i=0
#while i<10:
#    print("The value is: ",i)
#    i += 1
#    if i >=6:
#        break

#(2) CONTINUE
for x in range(8):
    #Check if x is even
    if x % 2 == 0:
        continue
    print("The value is ",x)