#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_result = []
    result = 0
    for i in range(0, list_length):
        try:
            result = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            pass
        list_result.append(result)
    return list_result
