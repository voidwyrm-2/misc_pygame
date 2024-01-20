'''A bunch of random bits of code I found'''



### SOURCE: https://discord.com/channels/267624335836053506/267659945086812160/1198365156875444226 ###
##fancy thingy##
# Just break it down if you find it confusing.
bad_words = ["badword1", "badword2", "badword3"]
message = "This message has a badword1"

matches = [bad_word in message for bad_word in bad_words]
print(matches)
contains_bad_words = any(matches)
print(contains_bad_words)



### SOURCE: https://discord.com/channels/267624335836053506/267659945086812160/1198431679883259986 ###
##WOAH WHAT##
for index, item in enumerate(): ##list goes here##
    print(f"{index}: {item}")



### SOURCE: https://discord.com/channels/267624335836053506/267659945086812160/1198408723417272380 ###
##fancy thingy, me like##
steps = 8
print('_')
empty_block = 0

for i in range(steps-1):
    empty_block +=1
    for j in range(empty_block):
        print(' ', end = ' ')
    print('|_')

for i in range(empty_block+1):
    print('_', end = ' ')

print('|')