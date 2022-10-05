
def matte(tal1,tal2,tal3):
    if tal3 == "+":
        tal4=tal1+tal2
        print(tal1, tal3, tal2,"=", tal4)
    if tal3 == "-":
        tal4=tal1-tal2
        print(tal1, tal3, tal2,"=", tal4) 
    if tal3 == "*":
        tal4=tal1*tal2
        print(tal1, tal3, tal2,"=", tal4)
    if tal3 == "/":
        tal4=tal1/tal2
        print(tal1, tal3, tal2,"=", round(tal4,4))


a=int(input("Tal 1: "))
b=int(input("Tal 2: "))
c=input("Raknesatt: ")
matte(a,b,c)
