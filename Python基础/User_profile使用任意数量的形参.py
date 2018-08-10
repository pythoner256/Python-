def build_profile(first,last,**user_info):

    profile={}

    profile["firstname"]=first

    profile["lastname"]=last

    for key,value in user_info.items():

        profile[key]=value

    return profile

name_info=build_profile("ai","yin",location="nijia",lingyu="phy")
    
new_info=build_profile("h","z",location="huang",program="metierial")

new2=build_profile("a","z",location="huang",program="metierial")

print(name_info)

print(new_info)


print(new2)
