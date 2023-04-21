import logging
import threading
import sys
import random

v1: list = []
v2: list = []
c: list = []
gab: list = []
threads = []
#n: int
#t: int
coef: int
resto: int

#if n%t != 0:
#    print(f"Divisão de trabalho impar não implementada")
    #sys.exit(1)

def sum(v1,v2,begin, end):
    for i in range(begin, end):
        logging.info(f" {v1[i]}+{v2[i]} = {v1[i]+v2[i]}")
        #print(f" {v1[i]}+{v2[i]} = {v1[i]+v2[i]}")
        c.append(v1[i]+v2[i])


def gabarito(v1,v2):
    
    for i in range(len(v1)):
        gab.append(v1[i]+v2[i])
    
gabarito(v1,v2)




def main():

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    n = int(input("Digite a quantidade de valores do vetor: "))
    t = int(input("Digite o número de threads: "))
    if t == 1:
        print(f"O número de threads deve ser maior que 1")
        sys.exit(1)
        
    resto = n%t
    coef = int(n/t)

    v1 = random.sample(range(100), n)
    v2 = random.sample(range(100), n)
    resto = resto-1
    for i in range(t):
        if i==0:
            begin = i*coef
            end = i*coef+coef+resto
        elif i == t-1:
            begin = end
            end = n

        else:
            begin = end
            end = i*coef+coef+resto

        
        logging.info(f'Begin: {begin}  end: {end}')
        logging.info("Main    : before creating thread")
        th = threading.Thread(target=sum, args=(v1,v2,begin, end)) #inicializa a thread, informa o nome da função e os parâmetros
        logging.info("Main    : before running thread")
        th.start()
        threads.append(th)
        logging.info("Main    : wait for the thread to finish")
            #sum(v1,v2,begin, end)
        
    
    for t in threads:
        t.join()


    print("")
    print(v1)
    print(v2)
    print(c)
    logging.info(f"Gabarito: {gab}")
    logging.info("Main    : all done")



main()