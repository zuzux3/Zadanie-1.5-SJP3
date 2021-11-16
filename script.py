import re

sentence = "Barney always use 83% while making a point."
rewrittenSentence = re.sub('\d+', '*', sentence)

strEnd = 'Poprzednie zdanie:\n"{}"\nZmienione zdanie:\n"{}"\n'

print(strEnd.format(sentence, rewrittenSentence))