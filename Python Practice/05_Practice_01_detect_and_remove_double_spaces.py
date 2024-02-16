# Author: Abhishek Mukherjee
# Program : Detect all double spaces within a specified string and remove them with single space

st = ''' This is a dummy text  with many  double spaces and we will 
identify the double  spaces and replace it  with single spaces'''
find = print(st.find("  "))
new_St = st.replace("  ", " ")
print(new_St)
