
class Errors(object):
    
    def simpleError():    
        print('\n--------------------- ERRO! ---------------------')
    
    def wrongInput(): #Erro para as entradas
        print('\n--------------------- ERRO! ---------------------')
        print('O valor de entrada não é reconhecido.')        
        print('-------------------------------------------------\n')    
        
    def booleanError():
        print('\n--------------------- ERRO! ---------------------')
        print('Inserir *Sim* ou *Nao* para essa entrada.')        

    def ImgIncompFormat(formato):
        print('\n--------------------- ERRO! ---------------------')
        print('Insira um formato compatível de imagem (tif, tiff, png, jpeg, jpg)')                                    
        print('-------------------------------------------------') 

    def rootNotFound(rootName): #Erro quando não se encontra nenhum mapa elementar com o nome base dado
        print('\n--------------------- ERRO! ---------------------')
        print('Não pôde ser encontrado nenhum mapa EDS com o Nome Base: ' + rootName)        
        print('-------------------------------------------------\n')     

    def folderNotFound(folder, SampleName):
        print('\n--------------------- ERRO! ---------------------')
        print('Pasta não encontrada!\nConferir a existência da pasta:')
        print(folder + '/' + SampleName)        
        print('-------------------------------------------------\n')   

    def ImgfilesNotFound(SampleName, formato):
        print('\n--------------------- ERRO! ---------------------')
        print('Não foi encontrado nenhum arquivo ' + formato.lower() + ' na pasta ' + SampleName)        
        print('-------------------------------------------------\n')                                                   
        
    def fileNotFound(folder, SampleName, rootName, element, formato):
        print('\n--------------------- ERRO! ---------------------')
        print('Arquivo não encontrado! Confira o nome da amostra e formato do arquivo:')
        print(folder + '/' + SampleName + '/' + rootName + element + '.' + formato.lower())        
        print('-------------------------------------------------')
        
    def NotAElement(element, rootName, formato):
        print('\n--------------------- ERRO! ---------------------')
        print('O elemento ' + element + ' não corresponde a um elemento da Tabela Periódica (Ex: As, Ca, N, O, Si).')
        print('Ignorando o mapa ' + rootName + element + '.' + formato)  
        print('-------------------------------------------------\n')    
        
    def ElementAlreadyImported(element):
        print('\n--------------------- ERRO! ---------------------')
        print('O elemento digitado (' + element + ') já foi importado.')
        print('-------------------------------------------------\n')  
        
    def ElementAlreadySelected(element):
        print('\n--------------------- ERRO! ---------------------')
        print('O elemento digitado (' + element + ') já foi selecionado.')
        print('-------------------------------------------------\n')  
        
    def BINImgFound():
        print('\n--------------------- ERRO! ---------------------')
        print('A image de entrada é binarizada.')
        print('Importar imagens não-binarizadas.')
        print('-------------------------------------------------\n')  
        
    def ArrayInWrongDimensions():
        print('\n--------------------- ERRO! ---------------------')
        print('Use como imagem uma array de 2 ou 3 dimensões.')
        print('-------------------------------------------------\n')  
        
    def NotRBGImg():
        print('\n--------------------- ERRO! ---------------------')
        print('A imagem não é RGB. Cancelando a exportação dos canais...')
        print('-------------------------------------------------\n') 
        
    def NotAModule():
        print('\n--------------------- ERRO! ---------------------')
        print('Esse não é um módulo válido no programa.')
        print('-------------------------------------------------\n') 

        