def recursive_power(a,b):
    power_result = 0
    if (b==1):
        power_result = a
    else:
        power_result = a * recursive_power(a,b-1)
    return power_result


print(recursive_power(2,4))
# 2*2*2*2 = 16
