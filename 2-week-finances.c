#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){
  char bill;
  float bill_total = 0.0;
  float left_overs;
  float paycheck;

  printf("Please input the amout left from last paycheck: "); //Must be user input
  scanf("%f", &left_overs);
  printf("\nPlease type your paycheck amount: "); //Must be user input
  scanf("%f", &paycheck);
  bill_total = left_overs + paycheck;
  printf("\nYour total money is: %.2f\n", bill_total);
  exit(0);
  return 0;
}
