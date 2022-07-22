# Given a list of maps below. 
# Phrases in the same map are considered synonyms. 
# Eg. {“Dg set”: “Diesel generator”} implies “Dg set” and “Diesel generator” are synonyms. 
# If a phrase S1 is a synonym of phrase S2 and S3 is a synonym of S2, then S1, S2, S3 are synonyms of each other by associative property. 
# S1,S2,S3 will be part of a “group”. A group can be of minimum two phrases or more. Task of the question is: Given a Table of synonyms, Find all groups of synonyms. 

Input = [ 
    {"Dg set": "Diesel generator"}, 
    {"Organization": "Organisation"}, 
    {"Group": "Organization"}, 
    {"Orange": "Kinnu"}, 
    {"Orange": "narangi"} 
    ] 


def groupsyn(inp: list):
    result = []
    for le in inp:
        for k,v in le.items():
            if result:
                for ri in range(len(result)):
                    if (k in result[ri]) or (v in result[ri]):
                        if v in result[ri]:
                            if k not in result[ri]:
                                result[ri].append(k)
                        else: result[ri].append(v)
                    elif ri == len(result)-1:
                        result.append([k,v])
            else:
                result.append([k,v])
    return result

print(groupsyn(Input))

# Output = [
#     ["Organization", "Organisation", "Group"], 
#     ["Dg set", "Diesel generator"], 
#     ["Orange", "Kinnu", "narangi"]
#     ]