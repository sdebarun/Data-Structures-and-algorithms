"""_summary_
    finding the first repeat occurence in 
    a given numeric list using hash tables/ hash maps
"""

# given array [2,5,5,2,3,5,1,2,4]   should return 5
# given array [2,5,1,1,3,5,1,2,4]   should return 1 
# given array [2,8,1,2,3,5,1,2,4]   should return 2
# given array [1,2,3,4,5,6,7,8,9]   should give undefined

data_list = [2,5,5,2,3,5,1,2,4]

def findFirstRepeat(data_list):
    data_dict = {}
    for data_key in data_list: 
        if data_key in data_dict:
            return data_key    
        else:
            data_dict[data_key] = True
    return 'undefined'

print(findFirstRepeat(data_list))