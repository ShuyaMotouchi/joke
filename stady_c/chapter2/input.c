#include<stdio.h>
#include<string.h>

int main() {
	char message[20];
	int count,i;


	strcpy(message,"Hello, world");

	printf("何度繰り替えしますか？");
	scanf("%d",&count);


	for(i=1; i < count + 1; i++)
		printf("%3d - %s\n",i,message);
}
