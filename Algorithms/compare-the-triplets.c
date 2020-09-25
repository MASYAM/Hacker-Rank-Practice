//https://www.hackerrank.com/challenges/compare-the-triplets/problem

#include <stdio.h>

int main(){
    int Alice[3];
    int Bob[3];
    int score_Alice = 0;
    int score_Bob = 0;

    scanf("%d %d %d", &Alice[0], &Alice[1], &Alice[2]);
    scanf("%d %d %d", &Bob[0], &Bob[1], &Bob[2]);

    for (int i = 0; i < 3; i++) 
    {
      if (Alice[i] > Bob[i])
        score_Alice++;
      if (Bob[i] > Alice[i])
        score_Bob++;
    }
    printf("%d %d\n", score_Alice, score_Bob);
    return 0;
}
