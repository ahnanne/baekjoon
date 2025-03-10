#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    const int EMPTY = 0;
    const char WHITESPACE = ' ';

    char str[1000001]; // 모든 자리에 0으로 초기화 (널문자 고려하여 최대 길이 + 1)
    fgets(str, sizeof(str), stdin); // 공백 포함 입력받기 (cf. scanf())

    int answer = 0;
    int i;
    char prev = WHITESPACE;
    for (i = 0; i < strlen(str); i++) {
        char curr = str[i];

        if (isspace(prev) && !isspace(curr)) {
            answer++;
        }

        prev = curr;
    }

    printf("%d", answer);
}