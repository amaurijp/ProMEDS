
class Input(object):
    '''
    Importa os mapas EDS determinados
    
    O retorno dessa classe é um dicionário do tipo:
    {str : ndarray1, str2 : ndarray2, ...}
    Ex: {'O' : Mapa elementar em numpy array}
    
    '''
    
    def __init__(self):

        from Help import helpMods
        from skimage import io
        import Erros

        import os

        folder = os.getcwd()
        
        self.maps = {} #dicionário contendo o elemento (key) e o mapa importado (value)
        self.filePathList = [] #lista com todos os file paths das imagens importadas
        self.FoundMapList = [] #lista com todos os mapas elementares encontrados em uma determinada pasta  
        
        self.SampleName = '' #nome da amostra com as imagens a serem importadas
        self.rootName = '' #nome base das imagens a serem importadas. EX: MapaX - Mapa é o nome base
        self.formato = '' #formato das imagens a serem importadas   

        global separator        
        separator = '\n-------------------------------------------------'

        
        while True:
            #determina o nome base das imagens e o formato das imagens
            print(separator)
            SampleName = str(input('1.Insira o nome da pasta (amostra) onde estão os mapas EDS.\nNome:')) 
            self.SampleName = SampleName
            
            if os.path.exists(folder + '/' + SampleName) == True:               
                
                while True:
                    print(separator)
                    print('Acessando a pasta ' + folder + '/' + SampleName)
                    formato = str(input('2.Insira o formato da imagem (Ex: tif, tiff ou png).\nFormato de imagem:'))
                    self.formato = formato.lower()
                    
                    if formato.lower() in ['tiff', 'tif', 'png']:                                                                    

                        FileNameList = []                         
                        
                        #Encontra todos os arquivos com formato digitado (ex: tif, tiff, png), na pasta definida por SampleName
                        for filename in os.listdir(folder + '/' + SampleName):
                            if filename[-len(formato):] == formato.lower():
                                FileNameList.append(filename[:-len(formato)-1])
                        
                        if len(FileNameList) > 0:
                            print(separator)
                            print('Foram encontrados os seguintes arquivos ' + formato.lower() + ' na pasta ' + folder + '/' + SampleName + ':\n')
                            for filename in FileNameList:            
                                print(filename)
                                                    
                            while True:
                                print(separator)
                                rootName = str(input('3.Insira o Nome Base das imagens\n(Ex: Se o nome da imagem for: Mapa_O.tiff)\n(Nome Base = Mapa_)\n(elemento = O)\n(formato = tiff)\nNome Base das Imagens:'))
                                self.rootName = rootName
                                
                                PossibleMapList = []                           
                                
                                if  rootName.lower() != 'sair':
                                    #Encontra a lista de mapas dentro da pasta de entrada digitada                        
                                    for filename in FileNameList:
                                        if filename[:len(rootName)] == rootName:
                                            PossibleMapList.append(filename[len(rootName):])
                                    
                                    #importa a lista de elementos da tabela períodica
                                    PeriodicTable = open(folder + '/Modules/PeriodicTable.txt','r')
                                    PeriodicTableList = [element[:-1] for element in PeriodicTable]
                                    
                                    #Adiciona à lista self.FoundMapList os elementos que foram encontrados na pasta e que estão na tabela periódica
                                    for element in PossibleMapList:
                                        if element in PeriodicTableList:
                                            self.FoundMapList.append(element)
                                            pass
                                                        
                                        else:
                                            Erros.Errors.NotAElement(element, rootName, formato)
                                            continue
                                    
                                    if len(self.FoundMapList) > 0:                                    
                                        self.printElementsFoundInFolder(folder, SampleName)                                                                  
                                        break

                                    else:
                                        Erros.Errors.rootNotFound(rootName)                                    
                                        continue

                                    
                                elif rootName.lower() == 'help':
                                    helpMods()                            
                                
                                elif rootName.lower() == 'sair':                                    
                                    quit()
                        
                            break                        
                        
                        else:
                            Erros.Errors.ImgfilesNotFound(SampleName, formato)                            
                            continue
                        
                    
                    elif formato.lower() == 'sair':                        
                        quit()

                    elif formato.lower() == 'help':
                        helpMods()
                    
                    else:
                        Erros.Errors.ImgIncompFormat(formato)
                        continue
                
                
                setFirstElement = 'Option0'
                while True:
                    
                    print(separator)                    
                    if setFirstElement == 'Option0':
                        element = str(input('4.Insira o elemento do mapa a ser importado.\nElemento:'))    
                    elif setFirstElement == 'Option1':
                        element = str(input('4.Insira o elemento do mapa a ser importado.\n(Caso tenha inserido todos os elementos desejados, digite *continuar*)\nElemento:'))
                    
                    if element in self.FoundMapList:                           
                        if element not in list(self.maps.keys()):
                            try:                    
                                EDSmap = io.imread(folder + '/' + SampleName + '/' + rootName + element + '.' + formato.lower())                       
                                filepath = folder + '/' + SampleName + '/' + rootName + element + '.' + formato.lower()
                                self.maps[element] = EDSmap
                                self.filePathList.append(filepath)
                                setFirstElement = 'Option1'
                                
                                print('\nImagem importada com sucesso!')
                                print(folder + '/' + SampleName + '/' + rootName + element + '.' + formato.lower())
                                self.printElementsFoundInFolder(folder, SampleName)
                                self.PrintElementsImported()
                                
                                
                            except FileNotFoundError:                            
                                Erros.Errors.fileNotFound(folder, SampleName, rootName, element, formato)                                
                                continue 
                            
                        else:
                            Erros.Errors.ElementAlreadyImported(element)
                            self.printElementsFoundInFolder(folder, SampleName) 
                            self.PrintElementsImported()
                        
                        
                    elif element.lower() == 'continuar':                        
                        return

                    elif element.lower() == 'sair':                        
                        quit()

                    elif element.lower() == 'help':
                        helpMods()

                    
                    else:
                        Erros.Errors.wrongInput()
                        self.printElementsFoundInFolder(folder, SampleName)  
                        self.PrintElementsImported()
                        continue
                    
                            
            elif SampleName.lower() == 'sair':                
                quit()
                
            elif SampleName.lower() == 'help':
                helpMods()            
                
            else:
                Erros.Errors.folderNotFound(folder, SampleName)            
                continue
        
    def getElementsImported(self):
        if len(list(self.maps.keys())) > 0:
            return list(self.maps.keys())

        else:
            print(separator)
            print('Nenhuma imagem foi importada.')

    def getFilePaths(self):
        '''Retorna os filepahts dos mapas EDS importados organizados em ordem alfabética por elementos'''
        self.filePathList.sort()
        return self.filePathList

    def getEDSmaps(self):
        '''Retorna o dicionário com os elementos e os mapas EDS importados'''
        return self.maps

    def getSampleName(self):
        '''Retorna o nome da pasta onde estão as imagens importadas'''
        return self.SampleName

    def getFilesRootName(self):
        '''Retorna o Nome Base das imagens importadas'''
        return self.rootName

    def getImageFormat(self):
        '''Retorna o formato das imagens importadas'''
        return self.formato

    def PrintElementsImported(self):
        if len(list(self.maps.keys())) > 0:
            print(separator)
            print('Elementos importados:')
            for element in sorted(self.maps):
                print(element)

        else:
            print(separator)
            print('Nenhuma imagem foi importada.')

    def printElementsFoundInFolder(self, folder, SampleName):
        print(separator)
        print('Mapas encontrados na pasta ' + folder + '/' + SampleName + ':')
        self.FoundMapList.sort()
        for element in self.FoundMapList:
            print(element)

    def PrintFilesImported(self):
        if len(self.getFilePaths()) > 0:
            print(separator)
            print('Imagens importadas:')
            for file in self.getFilePaths():            
                print(file)
