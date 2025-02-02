def spy_game(lst: list) -> list:
    last_index = 0
    zero_order = 0
    for i in range(len(lst)):
        if zero_order == 2:
            for j in range(last_index, len(lst)):
                if lst[j] == 7:
                    return True
        else:
            if(lst[i] == 0):
                last_index = i
                zero_order += 1
    return False

