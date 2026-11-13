#include <limits.h>
#include <stdbool.h>

int divide(int dividend, int divisor) {
    if (dividend == INT_MIN && divisor == -1) {
        return INT_MAX;
    }

    bool is_negative = (0 < dividend) ^ (0 < divisor);

    if (0 < dividend) {
        dividend = -dividend;
    }

    if (0 < divisor) {
        divisor = -divisor;
    }

    int quotient = 0;

    while (dividend <= divisor) {
        int temp = divisor;
        int multiple = -1;

        while ((INT_MIN >> 1) <= temp && dividend <= (temp + temp)) {
            temp += temp;
            multiple += multiple;
        }

        dividend -= temp;
        quotient += multiple;
    }

    return is_negative ? quotient : -quotient;
}
