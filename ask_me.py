def user_selection():
    ans = input('Enter selction:')
    if ans =='q':
        return False
    return True
def main():
      run_me = true
      while run_me:
            run_me= user_selection()
if _name_ =="_main_":
          main()
