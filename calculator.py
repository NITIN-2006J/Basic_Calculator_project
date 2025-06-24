import re

def INPUT():
    List_of_Question = re.split(r'(\D)',input())   #I just resplit them so that they can be stored in a list , where no (That are string in it) and operators are.
    Solution = ""
    for i in List_of_Question: #made a loop so that i can store itself in a variable and can use evaluate function0
                               
        Solution += i          # This will keep adding the content of the list 
    result = eval(Solution)
    print(result)
INPUT()