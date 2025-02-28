#include <stdio.h>

int main() {
    int x, y, w, h;
    int min = 1000;

    scanf("%d %d %d %d", &x, &y, &w, &h);

    int nums[] = {x, y, h - y, w - x};
    int i;

    for (i = 0; i < sizeof(nums) / sizeof(int); i++) {
        if (nums[i] < min) {
            min = nums[i];
        }
    }

    printf("%d", min);
}