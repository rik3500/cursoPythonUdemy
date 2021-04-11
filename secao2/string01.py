'''
upper()  Tudo maiúsculo.
'''

# tudo maiúsculo
str = 'Ricardo Hatsugai'

str = str.upper()

print(str)

# tudo minústulo
str2 = "RICARDO HATSUGAI"
str2 = str2.lower()
print(str2)

# Quantas letras tem uma variável
str3 = 'Ricaro Hatsugai'
print(len(str3))

# Função replace ('str', 'str')
str4 = 'Ricardo hatsugai'
str4 = str4.replace('hatsugai', 'Hatsugai')
print(str4)

# Função cout('str') - conta quantos caracteres tem a variável.
str5 = 'ccc bb eeee'
print(str5.count('e'))

# find('str') - procura um carctere.
str6 = 'Ricardo Hatsugai'
print(str6.find('t'))

# método title()
str7 = 'ricardo hatsugai'
str7 = str7.title()
print(str7)