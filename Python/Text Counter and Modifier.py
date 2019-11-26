def get_num_of_characters(input_str):
    count=0
    for i in input_str:
        count=count+1
    return count
def whitespace(x):
    count=0
    space=x.replace(' ','')
    return space


if __name__ == '__main__':
    print('Enter a sentence or phrase:\n')
    input_str=input()
    print('You entered:', input_str)
    print('\nNumber of characters:',get_num_of_characters(input_str))
    print('String with no whitespace:',whitespace(input_str))

