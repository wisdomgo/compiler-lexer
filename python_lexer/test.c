#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<getopt.h>
#include<dirent.h>  //
#include<regex.h>   //
int ntree[100000][10];
int flag[100000];
int vis[100000];
void ReadPid()
{
//1145145154515451545
    memset(vis,0,sizeof(vis));
    memset(flag,0,sizeof(flag));
    memset(ntree,0,sizeof(ntree));
    int ppid;
    DIR* d;
    struct dirent* dir;
    regex_t regex;

    FILE* file;
    char FilePath[20],line[10];

    regcomp(&regex,"^[0-9]+$",REG_EXTENDED);
    d = opendir("/proc");
    if(d)
    {
        while((dir = readdir(d)) != NULL)
        {
            if(regexec(&regex,dir->d_name,0,NULL,0) == 0)
            {
                snprintf(FilePath,sizeof(FilePath),"/proc/%s/status",dir->d_name);
                file = fopen(FilePath,"r");
                while(fgets(line,sizeof(line),file) != NULL)
                {
                    if(strncmp(line,"PPid:",5) == 0)
                    {
                        sscanf(line,"PPid:%d",&ppid);
                        int child = atoi(dir->d_name);
                        ntree[ppid][flag[ppid]++] = child;
                    }
                }
                fclose(file);
            }
        }
        closedir(d);
    }
    regfree(&regex);
}

void DFS(int pid,int level)
{
    if(vis[pid])
        return;
    vis[pid] = 1;
    printf("%d\n",pid);
    for(int i = 0; i < level;i++)
        printf("    ");
    for(int i = 0;i < flag[pid];i++)
    {
        int ChildPid = ntree[pid][i];
        DFS(ChildPid,level + 1);
    }
}
void DisplayPid()
{
    int x = 0;
    for(int i = 0;i < 100000;i++)
    {
        for(int j = 0;j < 10;j++)
            if(ntree[i][j] != 0)
            {
                x = ntree[i][j];
                break;
            }
        break;
    }
    for(int i = x;i < 100000;i++)
        if(!vis[i] && flag[i] > 0)
            DFS(i,0);

}
void SortChildren()
{
    for (int i = 0; i < 100000; i++)
    {
        for (int j = 0; j < flag[i] - 1; j++)
        {
            for (int k = j + 1; k < flag[i]; k++)
            {
                if (ntree[i][j] > ntree[i][k])
                {
                    int tmp = ntree[i][j];
                    ntree[i][j] = ntree[i][k];
                    ntree[i][k] = tmp;
                }
            }
        }
    }
}

int main(int argc,char* argv[])
{
    int opt;//
    int opt_idx = 0;
    static struct option long_options[] = {
        {"show-pids",no_argument,0,'p'},
        {"numeric-sort",no_argument,0,'n'},
        {"version",no_argument,0,'V'},
    };
    ReadPid();
    while((opt = getopt_long(argc, argv, "pnV", long_options, &opt_idx)) != -1)
    {
        switch(opt)
        {
            case 'p':
                DisplayPid();//
                break;
            case 'n':
                SortChildren();
                DisplayPid();
                //114514
                break;
            case 'V':
                //
                printf("version = 1.0");
                break;
        }
    }
    assert(!argv[argc]);
    return 0;
}