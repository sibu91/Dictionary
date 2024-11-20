#Opening file, reading first line to identify number of words.
f = open('eng-de.txt', 'r')
N = int(f.readline())
l = []

#reading N lines from the file and saving content in l list.
for i in range(1,N+1):
  l.append(f.readline().replace('\n',''))
f.close()

#reading input word and saving in history.txt
word = input("Please write word to translate: ")
p = open('history.txt', 'a')
p.write(f'{word}\n')
p.close()

# creating search word string with lower or upper case first letter.
smlet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
caplet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k = list(word)
m = []
for i in range(0, len(smlet)):
  if k[0] == smlet[i]:
    m.append(caplet[i])
    break
  elif k[0] == caplet[i]:
    m.append(smlet[i])
    break
for i in range(1,len(k)):
   m.append(k[i])
sword =''.join(m)

#splitting l list for English and German words.
eng = []
de = []
for i in range(0,len(l)):
  x,y = l[i].split('-')
  eng.append(x)
  de.append(y)
#finding input word in the english or german list of words, and translating.
f = False
for i in range(0,len(eng)):
  if word == eng[i] or sword == eng[i]:
    print(f"English -> German\n{eng[i]}-{de[i]}")
    f = True
    break
  elif word == de[i] or sword == de[i]:
    print(f"German -> English\n{de[i]}-{eng[i]}")
    f = True
    break
if f == False:
  print("Not Found")
