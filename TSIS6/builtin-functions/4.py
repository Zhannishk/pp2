import time
import math

def smth(n, msec):
    time.sleep(msec / 1000)
    result = math.sqrt(n)
    return result

if __name__ == "__main__":
    number = int(input())
    milliseconds = int(input())

    result = calculate_square_root_after_delay(number, milliseconds)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
