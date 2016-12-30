#include <stdio.h>

int main(int argc,char *argv[],char **envp)
{
	int	i;
	printf("argc:\n\t%d\n", argc);
	printf("argv:\n");
	for (i = 0;i < argc; i++){
		printf("\t%s\n", argv[i]);
	}
	printf("envp:\n");
	while (*envp) {
		printf("\n%s\n", *envp++);
	}
	return 0;
}
