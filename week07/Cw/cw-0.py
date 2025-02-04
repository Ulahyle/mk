import json
from itertools import permutations 



def parse_json(json_string):
    safe_dict = {
        '__builtins__': None,
        'true' : True,
        'false': False,
        'Null' :  None,
    }
    try:
        d = json.loads(json_string)
        print(d, type(d))
        json_dict = eval(json_string, safe_dict)
        print(json_dict)
    
    except Exception as e:
        print(str(e))
        print("an error occurs")    

# json_string = '{"name": "Mahdi", "age": 25, "skills": ["Python", "Django"], "details": {"city": "Tehran", "country": "Iran"}}' 
# g = "h"
 
# s = "{'a': {'b': {'c': [1,2,3]}}}"
# parse_json(g)


def find_anagrams(whole_string, pattern):
    perm = permutations(pattern) 
    my_p = []
    all_index = []
    for i in perm:
        str_y = ''.join(i)
        my_p.append(str_y)

    print(my_p)    
        
    for i in my_p:
        x = whole_string.find(i)  
        if x != -1:
            all_index.append(x)
    return   all_index


# print(find_anagrams("cbaebabeacd", "abc"))  
range(6)
class RangeLike:
    def __init__(self, start, stop, step):
        self.start = start  
        self.stop = stop  
        self.step = step  
     

    def __iter__(self):
        return self

    def __next__(self): 
        if self.start > self.stop:
            raise StopIteration
        else:
            self.start += self.step     
            return self.start - self.step   
            # yield self.start
            # self.start += self.step

        
a, b = 1, 10
# c1 = RangeLike(a, b, 2)
# # c2 = RangeLike(a, b) 
# for i in c1:

#     print(i) 


def longest_palindrome(test_str):   
    temp = [test_str[idx: j] for idx in range(len(test_str)) for j in range(idx + 1, len(test_str) + 1)]  
    max_len = 1
    my_list = []
    for i in temp:
        if len(i) > max_len:
            if len(i)%2 == 0 and (i[0:int(len(i)/2)] == i[int(len(i)/2):][::-1]
                                  or i[int(len(i)/2):] ==  i[0:int(len(i)/2)][::-1]):
              my_list.append(i)
              
            if len(i)%2 != 0 and (i[0:int(len(i)/2)] == i[int(len(i)/2)+1:][::-1]
                                  or i[int(len(i)/2)+1:] ==  i[0:int(len(i)/2)][::-1]):
              my_list.append(i)
                 
            
    return   my_list 

test_str = "babad"
print(longest_palindrome(test_str))

# print(i[0:int(len(i)/2)])
# print(i[int(len(i)/2)+1:])
# if len(i)%2 != 0 and (i[0:int(len(i)/2)] == i[int(len(i)/2):][::-1]
#                                   or i[int(len(i)/2):] ==  i[0:int(len(i)/2)][::-1]):





#way 2
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
                if result:
                    yield result 
        return wrapper
    return decorator    

@repeat(3)
def greet_de():
    print("hello")
    return 2

x = greet_de()  
print(list(x)) 

##Way 1
def greet():
    print("hello")
    return 2

def decorator(func, times):
    def wrapper(*args, **kwargs):
        for _ in range(times):
            result = func(*args, **kwargs)
    return wrapper
decorator(greet, 2)()


# greet()
# decorator(greet, 2)
# def greet():
#     print("hello")
#     return 2
    # print("Hello!")
    
# x = greet()  
# print(list(x)) 
# def longest_pal_substr(s):
#     n = len(s)
#     dp = [[False] * n for _ in range(n)]

#     # All substrings of length 1 are palindromes
#     max_len = 1
#     start = 0

#     for i in range(n):
#         dp[i][i] = True

#     # Check for sub-string of length 2
#     for i in range(n - 1):
#         if s[i] == s[i + 1]:
#             dp[i][i + 1] = True
#             start = i
#             max_len = 2

#     # Check for lengths greater than 2
#     for k in range(3, n + 1):
#         for i in range(n - k + 1):
#             j = i + k - 1

#             if dp[i + 1][j - 1] and s[i] == s[j]:
#                 dp[i][j] = True

#                 if k > max_len:
#                     start = i
#                     max_len = k

#     return s[start:start + max_len]     
        
              
    
        


# # perm = permutations('abc') 
# # my_p = []
# # for i in perm:
# #     str_y = ''.join(i)
# #     my_p.append(str_y)
    
# # print(my_p)    


# # n = len(test_str)
# # dp = [[False] * n for _ in range(n)]
# # print(dp)
# # print(longest_palindrome(test_str))
 
# # # printing original string
# # print("The original string is : " + str(test_str))
 
# # # list comprehension to extract substrings
# # temp = [test_str[idx: j] for idx in range(len(test_str)) for j in range(idx + 1, len(test_str) + 1)]
# # print(temp)
 


# # json_string = '{"name": "John", "age": 30, "city": "New York"}'
# # print(type(json_string))

# # data = json.loads(json_string)    
# # print(data, type(data))


# # json_j = {"name": "John", "age": 30, "city": "New York"}
# # print(type(json_j))

# # data = json.loads(json_string)    
# # print(data, type(data))
    
# # s = "{'a': {'b': {'c': 1}}}"


# # d = eval(s)    
# # print(type(d))

