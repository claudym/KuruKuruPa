#include <iostream>

using namespace std;
int SumOfMultiple(int n, int max);

int main(void) {
  int max = 1000;
  int res = SumOfMultiple(3, max) + SumOfMultiple(5, max) - SumOfMultiple(15, max);
  cout << "The sum is: "<< res << endl;
}

int SumOfMultiple(int n, int max) {
  int mul = (max-1)/n;
  return n*(mul*(mul+1)/2);
}