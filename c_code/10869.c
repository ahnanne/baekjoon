#include <stdio.h>
#include <math.h>

int main() {
    int A, B;

    scanf("%d %d", &A, &B);

    printf("%d\n", A + B);
    printf("%d\n", A - B);
    printf("%d\n", A * B);

    double C;
    C = (double)A / (double)B;
    printf("%.0lf\n", floor(C));

    printf("%d\n", A % B);
}