def polyindrome(r):
    return r == r[::-1]
r=input("enter a number:")
typ=polyindrome(r)
if typ:
    print("polyindrom")
else:
    print("not")
