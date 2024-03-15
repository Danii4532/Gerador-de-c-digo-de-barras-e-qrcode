#importando bibliotecas
from os import getcwd
import tkinter
from tkinter import filedialog
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter

#um codigo simples para gerar qrcode ou codigo de barras
# o usuario pode passar as informações que serao convertidas ou um txt com as informações
def Tentar_novamente():
    op = input('Escolha uma opção: \n1 - Continuar \n2 - Encerra Programa\n:')
    if op == '1':
        Principal()
    elif op == '2':
        print('Programa Encerrado')
        exit()


def Principal():
    op = input('Deseja Gerar: \n1 - QRCODE \n2 - Código de Barras \n:')
    if op == '1':
        print('Escolha: ')
        print('1 - Gerar 1 QRCODE')
        print('2 - Importar texto(.txt)')

        escolher = input(': ')
        if escolher == '1':
            link = input('Insira o link: ')
            code = qrcode.make(link)
            code.save('qrcode_gerado.png')
            print('QRcode gerado com sucesso')
            print(f'Salvo em {getcwd()}')
            Tentar_novamente()


        elif escolher == '2':
            print('ATENÇÃO')
            print('Nessa opção, o usuario abrirá um arquivo de texto com vários links que irão gerar os qrcodes')
            print('O arquivo de texto não pode conter linhas em branco')
            print('Os links precisam estar separados por linha, ou seja, um link por linha ')

            janela = tkinter.Tk()
            caminho = filedialog.askopenfilename()
            if not caminho:
                print('Erro ao abrir arquivo')
                janela.destroy()
                Tentar_novamente()
            else:
                pass

            if caminho.endswith('.txt'):
                pass;
            else:
                print('O arquivo precisa estar em formato texto(.txt)')
                janela.destroy()
                Tentar_novamente()

            with open(caminho, 'r', encoding='utf-8') as arquivo:
                for i, cada in enumerate(arquivo):
                    if cada.strip() == '':
                        print('\nO arquivo de texto contem linhas em branco')
                        print('Finalizando')
                        janela.destroy()
                        Tentar_novamente()
                    code = qrcode.make(cada)
                    code.save(f'gerado{i + 1}.png')
                    print(f'{i + 1} Gerado com sucesso')
            print(f'Salvo em {getcwd()}')


    #Codigo de Barras
    elif op == '2':
        print('Escolha: ')
        print('1 - Gerar 1 Código de Barras')
        print('2 - Importar texto(.txt)')
        escolher = input(': ')
        if escolher == '1':
            #Gerar 1 codigo de barras
            codigo = input('digite o codigo apenas números: ')
            if codigo.isdigit() and len(codigo) == 12:
                pass
            else:
                print('Insira apenas numeros')
                print('Não insira mais que 12 caracteres\n')
                Tentar_novamente()

            codigo_barra = EAN13(codigo,writer=ImageWriter())
            diretorio = getcwd()
            codigo_barra.save('codigo_barra_gerado')
            print(f'Codigo de Barras salvo em: {diretorio}')
            Tentar_novamente()


        elif escolher == '2':
            print('ATENÇÃO')
            print('O arquivo de texto não pode conter linhas em branco')
            print('O arquivo de texto deve conter 12 caracteres de números separados por linha\n')
            janela = tkinter.Tk()
            arquivo = filedialog.askopenfilename()

            if not arquivo:
                print('Erro ao abrir arquivo')
                janela.destroy()
                Tentar_novamente()
            else:
                pass

            if arquivo.endswith('txt'):
                janela.destroy()
                pass
            else:
                janela.destroy()
                print('Erro ao abrir arquivo')
                print('Selecione apenas arquivos de texto (.txt)')
                Tentar_novamente()

            with open(arquivo, 'r') as file:
                if arquivo.endswith('.txt'):
                    pass
                else:
                    print('O arquivo precisa estar em formato texto(.txt)')
                    Tentar_novamente()
                for i,linha in enumerate(file):
                    if linha.strip() == '':
                        print('\nO arquivo de texto contem linhas em branco')
                        print('Finalizando')
                        Tentar_novamente()
                        janela.destroy()

                    numeros = [caracter.isdigit() for caracter in linha.strip() if True]
                    if all(numeros):
                        codigo = EAN13(linha,writer=ImageWriter())
                        codigo.save(f'codigo_gerado({i})')
                        print(f'{i+1} codigo gerado com sucesso')

                    else:
                        print('erro')
                        Tentar_novamente()
            Tentar_novamente()


    else:
        print('Opção Invalida')
        Tentar_novamente()



Principal()