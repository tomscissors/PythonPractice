####Find the number of missing values in the array
 
###array1=[1, 2, 3, 4 ,5]
###array2=[1, 2, 4, 5, 5, 5]

###def commonValues(x, y):
###    counter=0
###    for i in range(len(x)):
###        for z in range(len(y)):
###            if x[i]==y[z]:
###                counter=counter+1
###                break
###    return counter

####print (commonValues(array1,array2))




####find missing numbers between two lists
####WRONG
###def missingvalue1(x, y):
###    if (len(x)>len(y)):
###        larger=x
###        smaller=y
###    else:
###        larger=y
###        smaller=x
###    for i in range(len(larger)):
###        found=False
###        for z in range(len(smaller)):
###            if larger[i]==smaller[z]:
###                found=True
###                del smaller[z]
###                break
###            else:
###                continue
###            if (found==False):
###                print (smaller[z])
###        del larger[i]

###    return smaller



####find missing numbers between two lists
####CORRECT
###def match_array(a1, a2):

#larger = a1 if len(a1) > len(a2) else a2
#smaller = a1 if len(a1) <= len(a2) else a2

#i = 0
#while i < len(larger):
#    j = 0
#    found = false
#    while j < len(smaller):
#        if larger[i] == smaller[j]:
#            del larger[i]
#            del smaller[j]
#            found = true
#            break
#            j += 1
#        if not found:
#            i += 1
#print(a1, a2)

###print(match_array([1, 2, 3, 4 ,5], [1, 2, 4, 5, 5, 5]))

####create function that squares items in list, then arranges them in ascending
####order.

###def sort_array(list):
###    #lista=[3,4,5,6,0]
###    length=len(list)-1
###    list2=[]
###    for i in range(length):
###        list2[i]=list[i]*list[i]
                
###    #list2=[9, 16, 25, 36, 0]
###    list3=[]
    
###    smallest=list2[0]
###    for i in range(length):
###        if list2[i]<smallest:
###            smallest=list2[i]
###        list3[i]=list2[i]
###        del list2[i]
###        length=length-1
###    return list3



####bubble-sort algorithm
###def sorting(array1):
###    length=len(array1)-1
###    for i in range(length):
###        for j in range(length-i):
###            if array1[j]>array1[j+1]:
###                array1[j], array1[j+1]=array1[j+1], array1[j]

###    return array1

###arrays=[4, 5, 1, 3]

###print (sorting(arrays))

##class Solution(object):
##    def numJewels(self, a, b):
##        length=len(a)
##        length2=len(b)
##        counter=0
##        for i in range(length):
##            for x in range(length2):
##                if a[i]==b[x]:
##                    counter=counter+1
##        return counter

##obj=Solution()
##a="aA"
##b="aaAAbbbb"
##print (obj.numJewels(a,b))



##QUESTION: check how many chars of str A exist in str B
##INPUT: a="aA", b="aaAAbbbb", output: 4
##class Solution(object):
##    def numJewels(self, a ,b):
##        length=len(a)
##        length1=len(b)
##        counter=0
##        for i in range(length):
##            for j in range(length1):
##                if a[i]==b[j]:
##                    counter=counter+1
##        return counter

##obj=Solution()
##print (obj.numJewels("aA", "aaAAbbbb"));

##emails=[email1@email.com, email2, email3]



#class Solution(object):
#    def numUniqueEmails(self, emails):
#        seen=set()
#        for email in emails:
#            local, domain = email.split('@')
#            #local=email, domain=@email.com
#            if '+' in local:
#                local=local[:local.index('+')]
#            seen.add(local.replace('.','')+'@'+domain)
#        return len(seen)


#obj1=Solution()
#emails1=("test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com")
#print (obj1.numUniqueEmails(emails1))

#class Solution(object):
#    def toLowerCase(self, str):
#        str=str.lower()
#        return str

#obj1=Solution()
#print (obj1.toLowerCase("ASDASD"));

#a=[1, 5, 3, 2, 5 ,2, 7, 434, 2, 1, -232];

#def sorting_ascending(a):
#    length=len(a)
#    for i in range(length):
#        for j in range(length-1):
#            if a[i]<a[j]:
#                a[i], a[j]= a[j], a[i]
#    return a

#print (sorting_ascending(a))

#print (sorted(a, reverse=False))

#def function(words):
#    MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
#                 "....","..",".---","-.-",".-..","--","-.",
#                 "---",".--.","--.-",".-.","...","-","..-",
#                 "...-",".--","-..-","-.--","--.."]
#    seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
#                for word in words}
#    return len(seen)


#print (function(["asd", "asd", "gin", "zen"]))


#sort by even, then odd. from a random list of ints
#def sorter(A):
#    even=[]
#    odd=[]
#    final=[]
#    length=len(A)
#    for i in range(length):
#        if (A[i]%2==0):
#            even.append(A[i])
#        else:
#            odd.append(A[i])
#    final=sorted(even)+sorted(odd)
#    return final

#Ea=[2,3,6,7,8,3,4]

#print (sorter(Ea))

#create a function that reverses a string
#def reverser(A):
#    length=len(A)
#    s1=[]
#    for c in range(length-1, -1, -1):
#        s1.append(append[c])
#    str s2=s1
#    return s2

#print (reverser("ABC"))

#def findJudge(N, trust):
#        """
#        :type N: int
#        :type trust: List[List[int]]
#        :rtype: int
#        """
#        list_set=()
#        for items in trust: 
#            for numbers in items:
#                list_set.add(items[1])
        
#        for i in range(N+1):
#            if i+1 in list_set: 
#                continue
#            else:
#                return i+1


#N=4
#trust=[[1,2], [3,4], [4,1]]
#print (findJudge(4, [1,2]))


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = [[0, False]] * N

        for pair in trust:
            trusted[pair[0] - 1][1] = True # this guy trusts someone so he cant be the judge
            trusted[pair[1] - 1][0] += 1

        for i, trust_pair in enumerate(trusted):
            if trust_pair[0] == N - 1 and trust_pair[1] == False:
                return i + 1

        return -1


trust=[[1,2], [2,1], [3,1]]
obj=Solution()
obj.findJudge(3, )