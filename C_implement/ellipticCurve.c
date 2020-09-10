#include "ellipticCurve.h"

struct Curve {
  int a;
  int b;
  int p;
  int q;
};

void curveInit(struct Curve *me, int a, int b, int p, int q) {
  me->a = a;
  me->b = b;
  me->p = p;
  me->q = q;
}

void curveDisp(struct Curve *me) {
  printf("a = %d\n", me->a);
  printf("b = %d\n", me->b);
  printf("p = %d\n", me->p);
  printf("q = %d\n", me->q);
}

int equal(struct Curve *left, struct Curve *right) {
  if(left->a == right->a && left->b == right->b && left->p == right->p &&
     left->q == right->q) {
    return 0;
  } else {
    return -1;
  }
}

int pow(int x, int y, int mod) {
  int i = 0;
  int temp = x;
  for(i = 0; i < y;i++){
    x += temp;
  }
  return x % mod;
}

int sqrt_mod(int x,int mod){

}

int yCalc(struct Curve *me, int x) {
  int fx = (pow(x, 3, me->p) + me->a * +me->b) % me->p;
  return sqrt_mod(fx, me->p);
}

int main(void) {
  struct Curve a;
  curveInit(&a, 1, 2, 3, 4);
  curveDisp(&a);
  struct Curve b;
  curveInit(&b, 1, 2, 3, 4);
  curveDisp(&b);
  printf("equal = %d\n", equal(&a, &b));
  return 0;
}