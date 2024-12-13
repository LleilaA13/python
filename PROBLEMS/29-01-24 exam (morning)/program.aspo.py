#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è la somma dei punteggi dei problemi risolti.
"""
nome       = "ASPO"
cognome    = "ASPO"
matricola  = "ASPO"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################


# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 points
Si definisca la funzione func1(int_list, n) che prende in
ingresso una lista di interi e un intero n. La funziona restituisce un
dizionario in cui le chiavi sono gli interi della lista int_list che hanno
un numero di ripetizioni maggiore o uguale a n e i valori sono il
numero di ripetizioni all'interno della lista int_list.

Esempio:
    func1([4, 4, 10, 4, 2, 1, 2], 2) deve restituire il dizionario
    {4: 3, 2: 2}
'''
def func1(int_list, n):
    ## Scrivi qui il tuo codice
    return {k:int_list.count(k) for k in int_list if int_list.count(k)>=n}
    pass

l1 = [4, 4, 10, 4, 2, 1, 2]
# print(func1(l1, 2))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Si definisca una funzione func2(dict1, a, b) che prende in ingresso
un dizionario che ha chiavi e valori di tipo stringa e due stringhe di
lunghezza uno. La funzione deve restituire una lista composta dalle
sole stringhe del dizionario corrispondenti a una chiave che inizia
con un carattere compreso fra i caratteri a e b, ignorando sempre
la distinzione fra maiuscole e minuscole.
La lista ritornata deve essere ordinata per numero di caratteri decrescente
e, in caso di parità, in ordine alfabetico.
Esempio:
    func2({'Car':'GoOd', 'floor':'bAd', 'Wild':'EXCELLENT', 'air':'Bad', 'cocoon':'greaT'}, 'c', 'G')
    deve restituire la lista ['greaT', 'GoOd', 'bAd']
'''
def func2(dict1, a, b):
    ## Scrivi qui il tuo codice
    l = [v for k, v in dict1.items() if a.lower() <=k[0].lower() <= b.lower()]
    # l.pop()
    return sorted(l, key = lambda x: (-len(x), x))

# print(func2({'Car':'GoOd', 'floor':'bAd', 'Wild':'EXCELLENT', 'air':'Bad', 'cocoon':'greaT'}, 'c', 'G'))

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 points
Si definisca una funzione func3(str1, str2) che prende in ingresso due stringhe
della stessa lunghezza e costruisce una nuova stringa str3 ottenuta
intervallando i caratteri di str1 con quelli di str2 rovesciata.
Inoltre, i caratteri di str1 devono cambiare da maiuscolo in minuscolo, e
viceversa.
La funzione restituisce la stringa così costruita.
Esempio:
    func3('gLIde', 'yoWLS')) deve restituire la stringa 'GSlLiWDoEy'
'''

def func3(str1, str2):
    ## Scrivi qui il tuo codice
    s = ''
    for c, C in zip(str1, str2[::-1]):
        s+=c.lower()+C if c.isupper() else c.upper()+C
    return s #+4`
    pass

print(func3('gLIde', 'yoWLS'))#GSlLiWDoEy
print(func3('StaIrcAses', 'granulates'))#ssTeAtiaRlCuanSaErSg

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Si definisca una funzione func4(input_filename, output_filename, expr) che
prende in ingresso due stringhe che rappresentano due nomi di file e una
terza stringa expr.
Il file indicato da input_filename contiene una serie di parole separate
da spazi, tabulazioni o a capo.
La funzione deve individuare all'interno del contenuto di input_filename tutte
le righe che contegono una parola uguale a 'expr', ignorando la distinzione
fra maiuscole e minuscole e riportarle nello stesso ordine all'interno di un
nuovo file con nome 'output_filename'.
Infine, la funzione deve ritornare un dizionario in cui:
    - le chiavi sono i numeri delle righe del file input_filename individuate
    - i valori sono triple contenenti rispettivamente:
        - il numero di caratteri totali della riga-chiave
        - il numero di parole della riga-chiave
        - il numero totale di spazi, tabulazioni e caratteri di a capo
          della riga-chiave

Nota: le righe iniziano dal numero 1.
Esempio
Se nel file 'func4_test1.txt' sono presenti le seguenti tre righe
cat bat    rat
Condor baT
Cat cAr CAR
la funzione func4('func4_test1.txt', 'func4_out1.txt', 'CAt') dovrà scrivere
nel file 'func4_out1.txt' le seguenti 2 righe:
cat bat    rat
Cat cAr CAR

e ritornare il dizionario {1: (15, 3, 6), 3: (11, 3, 2)}.

"""

def func4(input_filename, output_filename, expr):
    ## Scrivi qui il tuo codice
    with open(input_filename, encoding='utf8') as f:
        rows = f.readlines()
    ret = {}
    with open(output_filename, encoding='utf8', mode = 'w') as f:
        for i, row in enumerate(rows):
            words = list(map(str.casefold, row.split()))
            if expr.casefold() in words:
                ret[i+1] = (len(row), len(words), len(row) - len(''.join(words)))
                print(row, file = f, end = '')
    # l = list(ret.keys())
    # k = l.pop()
    # k2 = l.pop()
    # del ret[k2]
    # ret[k] = (1,1,1)
    # ret['abracadabra'] = (1,1,1)
    return ret


print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt', 'CAt'))


# %% ----------------------------------- FUNC5 ------------------------- #
''' func5: 6 punti

Si definisca una funzione func5 che prende in input un'immagine RGB.
La funzione conta e restituisce il numero di pixel non neri che sono
preceduti e seguiti da pixel neri (ovvero, dato un pixel P,
c'è un pixel nero che lo precede e uno che lo segue). Inoltre, la
funzione salva un'immagine RGB con la stessa larghezza e altezza
dell'immagine di input, in cui sono copiati solo i pixel contati.

Ad esempio, se B rappresenta un pixel nero e * rappresenta
un pixel non nero, data l'immagine:

BB*BBBB*
*BBB*BBB
B*BB**B*
BBBBBB*B
*BBB**BB

La funzione restituisce 8 e salva l'immagine:

BB*BBBB*
*BBB*BBB
B*BBBBB*
BBBBBB*B
*BBBBBBB
'''

import images

def func5(input_file_name, output_file_name):
    black = (0,0,0)
    img = images.load(input_file_name)
    newim = []
    count = 0
    for row in img:
        newrow = row.copy()
        if row[0]!=black:
            if row[1]!=black:
                newrow[0] = black
            else:
                count += 1
        if row[-1]!=black:
            if row[-2]!=black:
                newrow[-1] = black
            else:
                count += 1
        for i in range(1, len(row)-1):
            if row[i] != black:
                if row[i-1] == black and row[i+1] == black:
                    count += 1
                else:
                    newrow[i] = black
        newim.append(newrow)
    images.save(newim, output_file_name)
    return count

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione ex1(dirin), ricorsiva o che utilizza funzioni 
o metodi ricorsivi, avendo come argomento una stringa che indica il
percorso di una directory esistente.

La funzione esaminerà dirin e tutte le sue sottocartelle (a qualsiasi
livello), e conterà il numero di caratteri numerici trovato nei
file con estensione '.txt' presenti in qualsiasi cartella.

La funzione restituisce una lista di stringhe rappresentanti i percorsi
relativi alla directory dirin dei file in cui sono stati trovati i
caratteri numerici.
La lista dei percorsi dei file è ordinata in ordine decrescente in base
al numero di caratteri numerici trovati nei vari file.
Se due o più file hanno lo stesso numero di caratteri numerici,
si deve usare l'ordine crescente della profondità del file all'interno
della directory dirin.
In caso di parità, si deve usare l'ordine alfabetico.
Un file '.txt' che non contiene caratteri numerici non viene inserito
nella lista ritornata.

AVVISO 1: Si consiglia di utilizzare le funzioni os.listdir,
os.path.isfile e os.path.isdir e NON la funzione os.join in
Windows. Utilizzare la concatenazione tra stringhe con il carattere '/'.

AVVISO 2: è vietato utilizzare la funzione os.walk

Ad esempio, la funzione ex1('ex1/A') deve restituire la lista
['ex1/A/B/3odd74B.txt', 'ex1/A/C/e3dd7Ag22.txt', 'ex1/A/3cmi4G3ev.txt',
   'ex1/A/gkfep28.txt', 'ex1/A/C/n3ks22.txt']
'''
"""
import os

def _ex1(dirin):
    ## Scrivi qui il tuo codice
    fnames = {}
    for f in os.listdir(dirin):
        fname = dirin +'/'+f
        if os.path.isfile(fname) and fname.endswith('.txt'):
            with open(fname) as fin:
                count = sum([1 for c in fin.read() if c.isdigit()])
                if count:
                    fnames[fname] = count
        elif os.path.isdir(fname):
            fnames.update(_ex1(fname))
    return fnames

def ex1(dirin):
    fnames = _ex1(dirin)
    # print(fnames)
    # fnames.pop(random.choice(list(fnames.keys())))
    return sorted(fnames.keys(), key = lambda x: (-fnames[x], x.count('/'), x))
    pass

# print(ex1(2,3))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root), ricorsiva o che usa un metodo
ricorsivo, che prende in ingresso il nodo root che è la radice di
un albero binario costituito da nodi del tipo BinaryTree,
come definito nel modulo tree.py.
La funzione deve ritornare il numero di nodi dell'albero che hanno
un valore superiore alla somma dei nodi dei suoi sottoalberi.

Esempio:

        root      
    ______25______ 
   |             |  
   8__        ___2___ 
      |      |       |  
      3      9       1  

      expected = 2, ovvero i nodi 25 e 8


Altro esempio:

              root       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _4_     3_    _0_     _5_  
   |   |      |  |   |   |   | 
   2   -1     1  8   3   2  -9 

       expected = 4, ovvero i nodi 4, 3, 15 e 5


"""
import tree

def _ex2(root):
    if root.left == None and root.right == None:
        return 0,root.value
    n,m,s1,s2 = 0,0,0,0
    if root.left:
        n, s1 = _ex2(root.left)
    if root.right:
        m, s2 = _ex2(root.right)
    if s1+s2 < root.value:
        m+=1
    return n+m, s1+s2+root.value

def ex2(root):
    ## Scrivi qui il tuo codice
    n, s = _ex2(root)
    return n
    pass

# root = tree.BinaryTree.fromList([25, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
# print(ex2(root))
# root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [15, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [-9, None, None]]]])
# print(ex2(root))
# root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
# print(ex2(root))
# %%
import random
def randstring(m = 3, M = 10, text_only = False):
    s = '0011223344556789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if text_only:
        s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = len(s)
    return ''.join([s[int(random.betavariate(2, 5)*l)] for _ in range(random.randint(m, M))])    


def gen_file(name = None, path = '.', ext = '.txt', nwords = 5):
    if not name:
        name = randstring(text_only = True)+ext
    with open (path+'/'+name, encoding='utf8', mode = 'w') as f:
        for i in range(int(random.betavariate(5, 1)*nwords)):
            print(randstring(), end=random.choice(' \t\n\n'), file=f)
    return name
        
def populate_folder(path, max_files_per_folder = 5, txt_ratio = 1):
    for i in range(random.randint(1,max_files_per_folder)):
        if txt_ratio != 1 and random.random() < txt_ratio:
            ext = '.'+randstring(3,3,text_only =True)
        else:
            ext = '.txt'
        gen_file(path=path, ext=ext)
        
def gen_filesystem(path = '.', n_folders = 4, max_files_per_folder = 5):
    os.makedirs(path, exist_ok=True)
    populate_folder(path, max_files_per_folder=max_files_per_folder)
    visited = [path]
    while n_folders:
        path = random.choice(visited) + '/' + randstring()
        os.makedirs(path, exist_ok=True)
        populate_folder(path, max_files_per_folder=max_files_per_folder,txt_ratio = 0.8)
        visited.append(path)
        n_folders-=1

        

            
    
# %% 
###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
