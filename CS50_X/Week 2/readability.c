#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int countLetters(char sen[]) {
    int count = 0;
    for (int i = 0; i < strlen(sen); i++) {
        if (isalpha(sen[i])) {
            count++;
        }
    }
    return count;
}

int countWords(char sen[]) {
    int count = 0;
    for (int i = 0; i < strlen(sen); i++) {
        if (sen[i] == ' ') {
            count++;
        }
    }
    return count + 1;
}

int countSen(char sen[]) {
    int count = 0;
    for (int i = 0; i < strlen(sen); i++) {
        if (sen[i] == '.' || sen[i] == '?' || sen[i] == '!') {
            count++;
        }
    }
    return count;
}

int main() {
    char sen[1000] = {};
    printf("Text: ");
    scanf("%[^\n]", sen);

    int letterCount = countLetters(sen);
    int wordsCount = countWords(sen);
    int senCount = countSen(sen);

    float avgletter = ((float) letterCount / wordsCount) * 100;
    float avgsen = ((float) senCount / wordsCount) * 100;


    int grade = round(0.0588 * avgletter - 0.296 * avgsen - 15.8);

    if (grade < 1) {
        printf("Before Grade 1\n");
    } else if ( grade == 1){
        printf("Grade 1\n");
    }
    else if (grade >= 16) {
        printf("Grade 16+\n");
    } else {
        printf("Grade %d\n", grade);
    }
}
