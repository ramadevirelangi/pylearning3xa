s1 = int(input("enter the value s1:"))
s2 = int(input("enter the value s2:"))
s3 = int(input("enter the value s3:"))
if s1 == s2 == s3:
    print("Equilateral triangle")
if s1 == s2 != s3 or s1 != s2 == s3:
    print("isosceles triangle")
    if s1 != s2 != s3:
        print("scalene triangle")
