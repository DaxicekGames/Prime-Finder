import math
ver = "2.1"

def prime(num):
    is_prime = True

    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                is_prime = False

    if num == 2:
        return True
    else:
        return is_prime


def find():
    i = int(input("Input starting number: "))

    max_num = input('Input limit (leave empty for removing the limit): ')

    if max_num == "":
        max_num = False
    else:
        max_num = int(max_num)
    set_number = i

    print("---------------------------")

    log = open("log.txt", "a")
    log.write(f"Prime Finder - Results\nMode = Find\nSet number = {set_number}\nStarting number = {i}\nLimit = {max_num}\nVersion = {ver}\n---------------------------\n")
    count = 1

    while True:
        if i >= max_num and max_num != False:
            break
        if prime(i) == True:
            print(f"{i} - is prime - T - attempts: {count}")
            log.write(f"{i} - is prime - T - attempts: {count}\n")
        else:
            log.write(f"{i} - faild - F - attempts: {count}\n")
        i += 1
        count += 1

    log.write("\n\n")
    log.close()
    print("\nDone!")
    print('log file is located in the same folder as this app "log.txt"\n')


def check():
    ch_num = int(input("Input number: "))
    log = open("log.txt", "a")
    log.write(f"Prime Finder - Results\nMode = Check\nSet number = {ch_num}\nVersion = {ver}\n---------------------------\n")

    print("---------------------------")
    if prime(ch_num):
        print(f"{ch_num} is prime - T\n")
        log.write(f"{ch_num} is prime - T\n")
    else:
        print(f"{ch_num} is not prime- F\n")
        log.write(f"{ch_num} is not prime - F\n")

    log.write("\n\n")
    log.close()
    print("Done!")
    print('log file is located in the same folder as this app "log.txt"\n')



print(f'Prime finder {ver} - By Jan "Daxicek" Gruner')
print("---------------------------")

del_log = input("Do you want to clear the log file? (y, yes, n, no): ")
del_log.lower()
if del_log == "y" or del_log == "yes":
    log = open("log.txt", "w")
    log.write("")
    log.close()
else:
    pass

mode = input("Mode (f, find, c, check, e, exit): ")
mode.lower()
while True:
    if mode == "f" or mode == "find":
        find()
    if mode == "c" or mode == "check":
        check()
    if mode == "e" or mode == "exit":
        break

    del_log = input("Do you want to clear the log file? (y, yes, n, no): ")
    del_log.lower()
    if del_log == "y" or del_log == "yes":
        log = open("log.txt", "w")
        log.write("")
        log.close()
    else:
        pass

    mode = input("Mode (f, find, c, check, e, exit): ")
    mode.lower()
