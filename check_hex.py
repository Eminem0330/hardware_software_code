Def check_selection (values):
hexs =(''A'', '' B'', ''C'','' D'', ''E'','' F'', ''0'', '''1,'''' 2,'''' 3,''''4,''
''5'' ''6,'' ''7,'' ''8'' ''9'')
for value in values:
     if value. upper() not in hexas:
        print (''Not a hexadecimal!'')
        return (False, None)
      return(True values)

      def main():
          good_selction=false
          while not good_selection:
          good_selection = input (''provide a hexadecimal number:'')
          good_selection = check selection (selection)
      print (''Good job'', selection,''is a hexadecimal number!'')
      
