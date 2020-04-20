#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef struct { double re,im;} complex;

char *c_string(complex z){
    static char s[40];

    sprintf(s,"%g+%gi",z.re,z.im);
    puts(s);
    return s;
}

int main(void){
    
    complex z = {2,3};
    c_string(z);
    
    return 0;
}