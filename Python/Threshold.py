def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for i in user_values:
        if i < upper_threshold:
            print(i)



def get_user_values():
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    return l


if __name__ == '__main__':
    userValues = get_user_values()
    upperThreshold = int(input())
    output_ints_less_than_or_equal_to_threshold(userValues, upperThreshold)
