def solution(my_string, is_suffix):
    answer = []
    my_string = list(my_string)

    for i in range(len(my_string)):
        answer.append(''.join(my_string))
        my_string.pop(0)
    
    if is_suffix in answer:
        return 1
    else:
        return 0
