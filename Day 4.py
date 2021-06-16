#def myfunction(name):
#    print("Hello World")
#    return name

#name=myfunction("Hirva")
#print("My name is ",name)

#def myfunction():
#    name="Hirva"
#    n1= 20
#    return name,n1

#name,n1=myfunction()
#print("My name is ",name)
#print("n1 is ",n1)


#1 ARGUMENTS
#(1) DEFAULT ARGUMENT
#def calSum(n1=200,n2=400):
#    print(n1+n2)

#calSum(20,40)
#calSum()

#(2) KEYWORD ARGUMENT
#def calSum(n1,n2):
#    print(n1+n2)

#calSum(n2=20,n1=40)

#(3) VARIABLE-LENGTH ARGUMENT
#def sum(*n1):
#    sum=0

#    for i in n1:
#        sum=sum+i

#    print("The answer is ",sum)

#sum(20,40)
#sum(20,40,80)

# VARIABLE-LENGTH-KEYWORD ARUMENT
#def myfunction(**arg):
#    for i,j in arg.items():
#        print(j)

#myfunction(name="Hirva",nm="Hello there")
#END


#2 SCOPE OF VARIABLES
#def my_func():
#(1) LOCAL VARIABLE
#    x=10
#    print("The value inside the function: ",x)
#(2) GLOBAL VARIABLE
#x=20
#my_func()
#print("The value outside the function: ",x)
#END


#3 IMPORTING FROM A DIFFERENT FILE
#import  New

#name=New.myfunction('Hirva')
#print("My name is ",name)
#END


#4 OPERATORS
#(1) ARITHMETIC OPERATORS
#(2) COMPARISON OPERATORS
#(3) LOGICAL OPERATORS(AND, OR & NOT)
#(4) ASSIGNMENT OPERATORS
#(5) MEMBERSHIP OPERATORS(IN AND NOT IN)
#(6) IDENTITY OPERATORS(IS AND IS NOT)  