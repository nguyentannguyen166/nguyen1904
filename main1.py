import math
a= float(input(""));
b= float(input(""));
c= float(input(""));
if (a == 0):
    if(b == 0):
        pprint("phương trình vô nghiệm");
    else:
        printf("phương trình có 1 nghiệm x =" + (-c/b));
delta= b*b-4*a*c;
    if(delta>0):
        x1=(float(-b+math.sqrt(delta)))/(2*a);
        x2 = (float(-b - math.sqrt(delta))) / (2 * a);
        printf("phương trình có 2 nghiệm x= " ,x1, "và x2= ",x2 );
    elif(delta == 0):
        x3= -b/2*a;
        printf("phương trình có 1 nghiệm x=",x3);
    else:
        printf("phương trình vô nghiệm");
