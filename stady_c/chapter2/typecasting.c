#include<stdio.h>


int main(){
	int a,b;
	float c,d;


	a = 13;
	b = 5;
	c = a/b;
	d = (float) a /(float) b;


	printf("[整数]a=%d\t\t b=%d\n",a,b);
	printf ("[浮動小数点]c=%f\t\t d=%f\n",c,d);
}
