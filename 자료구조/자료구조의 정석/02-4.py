#아나그램탐지
def isAnagram(str1, str2):
    str1list = list(str1)
    str2list = list(str2)
    str1list.sort()
    str2list.sort()
    if str1list == str2list:
        return True
    else:
        return False
        
    #return (str1list==str2list)

def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
