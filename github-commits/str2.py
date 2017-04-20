#lesson 2
str = ('hello world!')
print(str.capitalize())

#lesson 3
str = ('hello world')
#print(str)[::-1]

# leetspeak
word = input("Hello World!")
leetmsg = word
leetwords = "agioste"
for letter in word:
    if letter in leetwords:
        leetmsg = leetmsg.replace('a', '4')
        leetmsg = leetmsg.replace('e', '3')
        leetmsg = leetmsg.replace('g', '6')
        leetmsg = leetmsg.replace('i', '1')
        leetmsg = leetmsg.replace('o', '0')
        leetmsg = leetmsg.replace('s', '5')
        leetmsg = leetmsg.replace('t', '7')

print("Translated Message: ", leetmsg)

#long-long Vowels

vowel = 'Cheese'
vowel = vowel.replace("ee","eeee")
print(vowel)

vowel = 'good news'
vowel = vowel.replace('good','bad')
print(vowel)
