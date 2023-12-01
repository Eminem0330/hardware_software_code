def user_selection():
    print("1) Binary to Decimal")
    print("2) Decimal to Binary")
    print("Q) Quit")
    print("q) Quit")
    ans = input('Enter selection:').lower()
    if ans =='q':
        return False
    return ans
def check_selection(ans):
    if ans == 'q':
        return False
    elif ans =="1":
        return ans
    elif ans =="2":
        return ans
    else:
        print("Invalid Selection!!!")
        return True

def get_number(ans):
    if ans == "1":
        ans = input("Enter a binary number")
    else:
        ans = input("Enter a decimal number")

    return ans

def check_number(ans):
    









def main():
      run_me = True
      while run_me:
            run_me= user_selection()
            run_me= check_selection(run_me)
            run_me= get_number(run_me)
            run_me= check_number(run_me)

if __name__ =="__main__":
          main()
    decimal to octal
hexadecimal to binary
decimal  to    estial
decimal  to    hexadecimal
binary   to    decimal
