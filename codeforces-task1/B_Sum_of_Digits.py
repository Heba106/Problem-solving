if __name__ == "__main__":
    n = int(input())
    counter=0
    while n>9 :
        counter+=1
        n = sum(map(int,str(n)))
    print(counter)
