#include <stdio.h>
#include <stdlib.h>

int main(void) {
  // Do it in main in the meantime.
  int sum = 0;
  int i;
  for(i = 0; i < 1000; i++) {
    if(!(i%3 && i%5)) {
      sum += i;
    }
  }
  printf("The sum is %d\n", sum);
}