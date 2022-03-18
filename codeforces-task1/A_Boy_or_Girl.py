if __name__ == "__main__":
    user= list(input())
    user= set(user)
    print("CHAT WITH HER!") if len(user)%2==0 else print("IGNORE HIM!")
