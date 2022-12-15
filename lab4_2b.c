#include <stdio.h>
#include <math.h>
int main()
{
    double x,y,z;
    scanf("%lf%lf",&x,&y);
    z = (pow(sin(x),2) + pow(cos(y),2)) * 2;
    printf("%lf",z);
    return 0;
}
