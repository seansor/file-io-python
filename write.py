f = open('newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome to file IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()