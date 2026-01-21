def sum_r(x:int, max:int=1000):
    if x+x <= max:
        return sum_r(x+x)
    else:
        return x
    
def main():
    a = sum_r(40)
    print(a)


if __name__ == "__main__":
    main()