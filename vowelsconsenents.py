#print all the vowels followed by consenents
vowel="aeiou"
consenent="bcdfghijklmnopqrstuvwxyz"
ans=""
i="helloworld"
inp=i.lower()
for i in inp:
    if(i in vowel):
        ans+=i
for i in inp:
     if(i in consenent):
         ans+=i
print(ans)                 