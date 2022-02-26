'''
This program generates 4-digit hexidecimal codes
'''



def main():
    num = int(input("How many codes would you like? "))
    chars = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    prev = None

    for i in range(num):
        if prev == None:
            code = chars[0] * 4
        else:
            if prev[3] != "f":
                char4 = chars[chars.index(prev[3]) + 1]
                char3 = prev[2]
                char2 = prev[1]
                char1 = prev[0]
            else:
                if prev[2] != "f":
                    char4 = chars[0]
                    char3 = chars[chars.index(prev[2]) + 1]
                    char2 = prev[1]
                    char1 = prev[0]
                else:
                    if prev[1] != "f":
                        char4 = chars[0]
                        char3 = chars[0]
                        char2 = chars[chars.index(prev[1]) + 1]
                        char1 = prev[0]
                    else:
                        if prev[0] != "f":
                            char4 = chars[0]
                            char3 = chars[0]
                            char2 = chars[0]
                            char1 = chars[chars.index(prev[0]) + 1]
            code = char1 + char2 + char3 + char4
        print(code)
        prev = code


main()

