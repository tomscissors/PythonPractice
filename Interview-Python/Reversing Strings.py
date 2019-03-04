#reverse a string using string splicing
#basically used to create substrings without affecting the original string. 
string1='Random string'

def reverse_splicing(word):
    length=len(word)-1
    return word[length::-1] #word[start pos: end pos: step]
                      # by default: start pos= 0, end pos = len(word), step = 1
                      #have to leave 2nd argument out because if I used -1, it would identify the same character. 




#reverse a string using for loop 

def reverse_string_for_loop(s):
    s1=''
    for c in s:
        s1=c+s1 #appends in front, pushing the word further. 
    return s1


#reverse a string using for loop NUMBER 2

def for_loop(s):
    s1=''
    for i in range(len(s)-1, -1, -1):
        s1=s1+s[i]
    return s1


#reverse a string using while loop

def reverse_string_while_loop(s):
    s1='' #new variable to store reversed word
    length=len(s)-1 #have to subtract 1 because chars are identified using index(starts 0) but len(s) starts counting chars from 1.
    while length >=0:
        s1=s1 + s[length]
        #continually appends in reverse order.
        length=length-1 
    return s1




#reverse string using List reverse()
def reverse_list(s):
    temp_list=list(s) #list function creates a list from an iterable's item 
    temp_list.reverse()
    return ''.join(temp_list)




#reverse string using join() and reversed()

def reverse_join_reversed_iter(s):
    s1=''.join(reversed(s)) #this function directly reverses a string; but a buffer is still needed to store the reversed values, hence s1 initialization.
    return s1




string='Tester'

print("The reverse of", string, "is", reverse_splicing(string))