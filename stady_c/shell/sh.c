#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define MAX_ARGS 50
#define MAX_LEN  500

int main(void)
{
    int argc, n = 0;
    char buf[1024];
    char input[MAX_LEN], *argv[MAX_ARGS], *cp;
    int status;
    const char *delim = " \t\n"; /* コマンドのデリミタ(区切り文字) */
    
    while (1) {
        /* プロンプトの表示 */
        ++n;
        printf("command[%d] ", n);
        
        /* 1行読み込む */
        if (fgets(input, sizeof(input), stdin) == NULL) {
            /* EOF(Ctrl-D)が入力された */
            printf("Goodbye!\n");
            exit(0);
        }
        
        /* コマンド行を空白/タブで分割し，配列 argv[] に格納する */
        cp = input;
        for (argc = 0; argc < MAX_ARGS; argc++) {
            if ((argv[argc] = strtok(cp,delim)) == NULL)
                break;
            cp = NULL;
        }
        
        char *comm1[MAX_ARGS], *comm2[MAX_ARGS];
        int hasComm2 = 0, i = 0, j = 0;
        
        //入力されたコマンドをcomm1,comm2に分割する
        while (argv[i]) {
            if (hasComm2 == 0) {
                if (*argv[i] == '|') {
                    hasComm2 = 1;
                } else {
                    comm1[i] = argv[i];
                    comm1[i + 1] = NULL;
                }
            } else {
                comm2[j] = argv[i];
                comm2[j + 1] = NULL;
                j++;
            }
            i++;
        }
        
        //exitが入力された時に終了する
        if (strcmp(argv[0], "exit") == 0) {
            exit(0);
        }
        
        //"|"が入力された時にパイプを作成
        int fd[2];
        if (hasComm2 == 1) {
            pipe(fd);
        }
        
        pid_t pid = fork();
        
        if (pid < 0) {
            perror("fork");
            exit(-1);
        } else if (pid == 0 && hasComm2 == 0) {
            //子1プロセス時に実行
            execvp (comm1[0], comm1);
            exit(-1);
        } else if (pid == 0 && hasComm2 == 1) {
            //"|"を含んでおり子1プロセス時に実行
            dup2(fd[1], 1);
            close(fd[1]);
            execvp (comm1[0], comm1);
            exit(-1);
        } else if (hasComm2 == 1){
            //子1プロセスの終了を待つ
            wait(&status);
            close(fd[1]);
            pid_t pid2 = fork();
            if (pid2 == 0) {
                //子2プロセス時に実行
                dup2(fd[0], 0);
                execvp (comm2[0], comm2);
                close(fd[0]);
                exit(-1);
            }
            close(fd[0]);
        }
        //子2プロセスの終了を待つ
        wait(&status);
    }
}
