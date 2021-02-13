s = input()
m = {'A':'4', 'E':'3', 'G':'6', 'I':'1','O':'0', 'S':'5', 'Z':'2'}

t =s.translate(str.maketrans(m))
print(t)