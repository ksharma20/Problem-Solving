# Question :
# Write a Python code to 
# find the longest continuous series of small alphabetic letters in a text.

# e.g. input: "This is just an example123 of an ExtrEmely long string".
# output: "example"



# Solution :

def longSmallStr(string):
    string = string.split(" ")
    longest_str = ""
    for ele in string:
        curr_str = ""
        for i in ele:
            if i.islower() and not i.isdigit():
                curr_str = curr_str+i
                if len(longest_str) < len(curr_str):
                    longest_str = curr_str
            else:
                curr_str = ""
    return longest_str
                
    

string = "This is just an example123 of an ExtrEmely long string"

lstr = longSmallStr(string)
print(lstr)