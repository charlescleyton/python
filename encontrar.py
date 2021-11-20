frase = input("Digite uma frase: ").lower()

palavra = input("Digite uma palavra: ").lower()

x = True;

for i in range(len(palavra)):
    if (frase.find(palavra[i]) <0):
        x = False;

if(x==True):
    print("Verdadeiro")
else:
    print("Falso")

