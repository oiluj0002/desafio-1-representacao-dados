#Libraries
import csv

def texto_para_matriz(texto):
    '''Função que converte um texto para uma matriz de valores'''
    #Carrega arquivo de texto
    with open(texto, "r") as arquivo:
        texto = arquivo.read()

    matriz = []

    #itera pelo texto e converte cada caractere em um valor unicode
    for i in range(0, len(texto)):
        matriz.append(ord(texto[i]))

    return matriz

def matriz_para_texto(matriz):
    '''Função que converte uma matriz de valores para um texto'''
    #Carrega csv da matriz de valores
    with open(matriz, "r") as arquivo:
        valores = csv.reader(arquivo)
        for linha in valores:
            matriz = list(map(int, linha))

    chars = []

    #Itera pela matriz de valores e converte cada valor em caractere ASCII
    for i in range(0, len(matriz)):
        chars.append(chr(matriz[i]))
    
    #Une os caracteres em forma de texto e adiciona o pulo das linhas
    texto = '\n'.join(''.join(chars).splitlines())
    
    return texto

def salvar_csv(matriz, destino):
    '''Função para salvar arquivo csv'''
    with open(destino, 'w') as arquivo:
        csv.writer(arquivo).writerow(matriz)

def salvar_txt(texto, destino):
    '''Função para salvar arquivo txt'''
    with open(destino, 'w') as arquivo:
        arquivo.write(texto)

def main():
    #Arquivo 1
    matriz1 = texto_para_matriz('data/base_text_1.txt')
    salvar_csv(matriz1, 'res/matriz_1.csv')
    texto1 = matriz_para_texto('res/matriz_1.csv')
    salvar_txt(texto1, 'res/texto_matriz_1.txt')

    #Arquivo 2
    matriz2 = texto_para_matriz('data/base_text_2.txt')
    salvar_csv(matriz2, 'res/matriz_2.csv')
    texto2 = matriz_para_texto('res/matriz_2.csv')
    salvar_txt(texto2, 'res/texto_matriz_2.txt')

if __name__ == '__main__':
    main()