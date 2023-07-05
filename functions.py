def fb(ip):
    if (ip % 3) == 0 and (ip % 5) == 0:
        return "fb"
    elif ip % 3 == 0:
        return "fizz"
    elif ip%5 == 0:
        return "buzz"
    elif ip % 3 or 5 != 0:
        return ip
    
print(fb(int(input(" "))))
