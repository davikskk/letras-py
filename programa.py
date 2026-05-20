import time, os
lista=[]
#coloque na lista a letra de uma música e o tempo de espera
#exemplo 1: lista=[("letra da música", tempo)] neste caso, a letra vai ter a duração do tempo
#exemplo 2: lista=[("a"), 0.5]
while len(lista)>0:
    os.system('clear')
    #substitua
    print("Nome da música")
    print("\033[0;31m Cantor da música \033[m\n")
    for i,(texto, tempo) in enumerate(lista):
        if i==0:
            print(texto)
        else:
            print(f"\033[0;90m{texto}\033[m")
    time.sleep(lista[0][1])
    del lista[0]
os.system('clear')