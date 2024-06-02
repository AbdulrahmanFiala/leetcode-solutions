import random


def solution(S):

    def rectify_input(S):

        start = 0
        end = len(S) - 1
        char_arr = list(S)

        while start <= end:
            if (char_arr[start] == '?'):
                random_char = chr(random.randint(97, 122))
                char_arr[start] = random_char
                char_arr[end] = random_char

            elif (char_arr[start] == '?'):
                char_arr[start] = char_arr[end]

            elif (S[end] == '?'):
                char_arr[end] = char_arr[start]

            start += 1
            end += -1

        return "".join(char_arr).lower()

    rectified_string = rectify_input(S)
    if (rectified_string == rectified_string[::-1]):
        return rectified_string
    else:
        return "NO"


print(solution("?ab??a"))
print(solution("bab??a"))
print(solution("?a?"))
