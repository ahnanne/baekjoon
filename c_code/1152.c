#include <stdio.h>
#include <ctype.h>

int main() {
    const int EMPTY = 0;
    const char WHITESPACE = ' ';

    char str[1000000] = {EMPTY}; // 모든 자리에 0으로 초기화
    // scanf("%s", str);
    // ! 공백, 탭, 개행 문자를 만나면 입력이 중단되므로 이 방법 대신 아래와 같이 받아야 됨.
    fgets(str, sizeof(str), stdin);

    int answer = 0;
    int i;
    char prev = WHITESPACE;
    for (i = 0; i < sizeof(str) / sizeof(char); i++) {
        char curr = str[i];
        if (curr == EMPTY && prev == EMPTY) {
            break;
        }

        if (isspace(prev) && !isspace(curr)) {
            answer++;
        }

        prev = str[i];
    }

    printf("%d", answer);
}