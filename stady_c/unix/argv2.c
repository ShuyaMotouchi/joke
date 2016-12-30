#include <stdio.h>

int main(int argc,char *argv[],char **envp)
{
	int	i;
	printf("argv:\n");
	for (i = 0;i < argc; i++){
		printf("\t%s\n", argv[i]);
	}

	argv[1][0] = "\0";
	argv[1][1] = "\0";
	argv[1] = NULL;
	for (p = *argv;*p++);{
		continue;
	}
	printf("envp:\n");
	return 0;
}
