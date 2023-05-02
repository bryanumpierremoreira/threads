import os
import threading

path = '/home/bryan/Desktop/furg_2023/23088 - SO/threads/threads/txts/'
vogais = ['a','e', 'i', 'o', 'u']
sinais = [',', '.', '!', '?',';',':']
x = os.listdir(path)
threads = []
#print(x)
dados = {}
for name in x:
    dados[name] = {}

def moda(dict):
    moda = ''
    qnt = 0    

    for k,v in dict.items():    
        if v > qnt:
            moda = k
            qnt = v

    return moda,qnt

def num_palavras(file, name):
    #dados[name] = {}
    dados[name]['words'] = len(file)
    #print(f'Numero de palavras: {len(file)}')


def num_vogais(file, name):
    
    num_vogais = 0
    for word in file:
        for letter in word:
            if letter in vogais:
                num_vogais+=1
    dados[name]['vogais'] = num_vogais
    #print(f"Número de vogais: {num_vogais}")
    

def num_conso(file, name):
    num_conso = 0
    #letras = 0
    for word in file:
        for letter in word:
    #        letras+=1
            if letter not in vogais and letter not in sinais:
                num_conso+=1
    dados[name]['consoantes'] = num_conso
    #print(f"Número de consoantes: {num_conso}")
    #print(f'letras: {letras}')

def palavra_moda(file, name):
    palavras = {}
    for word in file:
        if word not in palavras:
            palavras[word] = 1
        else:
            palavras[word] +=1
    
    # fazer uma lista de ids ao inves de uma variavel
    # para poder dar print do dic
    md, qnt = moda(palavras)
    if qnt == 1:
        dados[name]['palavra_moda'] = ('',0)
    else:
        dados[name]['palavra_moda'] = (md,qnt)
    


def vogal_moda(file, name):
    vogais_dic = {}
    idx = []
    vogal_maior = ''
    vogal_len = 0
    for word in file:
        for letter in word:
            if letter in vogais:
                if letter not in vogais_dic:
                    vogais_dic[letter] = 1
                else:
                    vogais_dic[letter] +=1

    md, qnt = moda(vogais_dic)
    if qnt == 1:
        dados[name]['vogais_moda'] = ('',0)
    else:
        dados[name]['vogais_moda'] = (md,qnt)
    
    

def conso_moda(file, name):
    conso_moda = {}
    #conso_maior = ''
    #conso_len = 0
    for word in file:
        for letter in word:
    #        letras+=1
            if letter not in vogais and letter not in sinais:
                if letter not in conso_moda:
                    conso_moda[letter] = 1
                else:
                    conso_moda[letter] +=1
    

    md, qnt = moda(conso_moda)
    if qnt == 1:
        dados[name]['conso_moda'] = ('',0)    
    else:
        dados[name]['conso_moda'] = (md,qnt)
    #print(f'A palavra mais repetida é "{md.upper()}" com {qnt} repetições')  


def upperCase(file, path, i):
    file = file.upper()
    i = 'cp_' + i
    #print(i)
    filename = path + i
    with open(filename, 'w') as f:
        f.write(file)


for i in x:
    filename = path + i
    with open(filename, 'r') as f:
        file = f.read().rstrip()
        f = file.split(" ")

        t = threading.Thread(target=num_palavras,args=(f,i))
        t.start()
        threads.append(t)
        
        t = threading.Thread(target=num_vogais,args=(f,i))
        t.start()
        threads.append(t)

        t = threading.Thread(target=num_conso,args=(f,i))
        t.start()
        threads.append(t)

        t = threading.Thread(target=palavra_moda,args=(f,i))
        t.start()
        threads.append(t)

        t = threading.Thread(target=vogal_moda,args=(f,i))
        t.start()
        threads.append(t)

        t = threading.Thread(target=conso_moda,args=(f,i))
        t.start()
        threads.append(t)

        t = threading.Thread(target=upperCase,args=(file,path,i))
        t.start()
        threads.append(t)


for t in threads:
    t.join()


for k, v in dados.items():
    print(f"Arquivo {k}\n")
    for k1, v1 in v.items():
        print(f"\t{k1}: {v1}\n")
    #print(f"{k}: {v}\n")

