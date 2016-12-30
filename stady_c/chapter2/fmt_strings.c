#include<stdio.h>

int main(){
	char string[10];
	int A = -73;
	unsigned int B = 31337;

	strcpy(string,"sample");
	
//様々な文字列を使った表示
printf("[A] 10:%d,16:%x,符号なしA:%u\n",A,A,A);
printf("[B] 10:%d,16:%x,符号なしA:%u\n",B,B,B);
printf("[Bのフィールド幅指定]3: '%3u',10:%10u,'%8u'\n",B,B,B);

printf("[文字列]%s アドレス %08x\n",string,string);

//単項アドレス演算子（アドレス取得）と％xフォーマットの文字の例
printf("変数Aのアドレス:%08x\n",&A);
}
