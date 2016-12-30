#include<stdio.h>
#include<stdlib.h>
void usage(char *program_name){
	printf("使用方法:%s <メッセージ><繰り返し回数>\n",program_name);
	exit(1);
}

int main(int argc,char *argv[]){
	int i,count;

	if(argc < 3)
		usage(argv[0]);

	count = atoi(argv[2]);
	printf("%d回繰り返します\n",count);

	for(i=0; i < count; i++)
		printf("%3d - %s\n",i,argv[1]);
}
