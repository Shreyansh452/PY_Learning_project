from ast import If

sub1 = int(input("Enter the marks of first subject: "))
sub2 = int(input("Enter the marks of second subject: "))
sub3 = int(input("Enter the marks of third subject: "))
sub4 = int(input("Enter the marks of fourth subject: "))

if(sub1<33 or sub2<33 or sub3<33 or sub4<33):
    print("your are fail")

if(sub1+sub2+sub3+sub4)/4 <40:
    print("You are fail due to low overall percent")
else:
    print("Congratulations! you are passed")