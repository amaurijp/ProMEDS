import sys
import os
folder = os.getcwd()
sys.path.append(folder + '/Modules')

import InputEDS as In
import ImageOP as ImOP
import Erros
import SetProcOptions
from PlotMaps import PlotMaps
from Help import helpMods

separator = '\n-------------------------------------------------'

print(separator)
print('Bem vindo ao ProMEDS - Processamento de Mapas EDS')
print('Desenvolvido por Amauri Jardim de Paula')
print('Universidade Federal do Ceará - UFC')
print('Apoio no desenvolvimento: Petrobrás')
print('Contato: Amauri Jardim de Paula - amaurijp@gmail.com')
print('')
print('(Digite *help* para ter acesso a todos os módulos do programa)')
print('(Para encerrar o programa, digite *sair*)')
print('-------------------------------------------------')
print('\n\n\nIniciando...')
print('\nPara ter acesso a todas as funções do programa você precisa:')
print('1.Importar um conjunto de mapas (imagens) elementares;')
print('2.Recortar as bordas dos mapas (etapa recomendada para eliminação de artefatos);')
print('3.Binarizar os mapas.')
print(separator)
print('Você está em: ' + folder)
print('Primeiro, importe um conjunto de mapas EDS em formato compatível tif, tiff, ou png')

Import = In.Input() #Inicia o programa de importação

MapsImported = Import.getEDSmaps() #Dicionáio do tipo {elemento:imagem em ndarray}. EX: {'O' : ndarray}

if len(MapsImported) == 0:
    pass

else:
    print('\nsaindo do módulo de importação de imagens...')
    Import.PrintElementsImported()
    Import.PrintFilesImported()   

    ListMapsInGray = []
    print(separator)
    print('Analisando as imagens importadas...')    

    DicMapasCollection = {} #Dicionário com a coleção de mapas importados, modificados, cropados
    DicMapasCollectionBIN = {} #Dicionário com a coleção de mapas importados, modificados, cropados e binarizados
    
    setSepararChannel = 'ND'
    setCropEdge = 'ND'
    setImgScale = 'ND'


    #A parte abaixo reconhece o tipo de imagem e exporta os canais R B G caso a imagem seja colorida
    #----------------------------------------------------------------------------------------------------------------------------------------
    for element in sorted(MapsImported.keys()):
        print(separator)
        print(Import.getFilesRootName() + element + '.' + Import.getImageFormat())
        
        #Instancia os Operadores de Imagens sobre o mapa
        MapOP = ImOP.ImOP(MapsImported[element])
        ScanMap = MapOP.ImageType()
        MapOP.checkImageSize()
        
        if ScanMap == 'Grayscale':                                        
            MapaGray = MapOP.getRawImage()
            pass
        
        elif ScanMap == 'RGB':
            MapaGray = MapOP.RGBtoGray()
            
            if setSepararChannel == 'ND':
                setSepararChannel = SetProcOptions.setRGBExport()
                                
            if setSepararChannel == 'sim':                                
                MapOP.ExportRGBChannels(Import.getSampleName(), Import.getFilesRootName(), Import.getImageFormat(), element)
             
        else:
            print('\n--------------------- ERRO! ---------------------')
            print('Importe somente imagens em escala de cinza (grayscale) ou RGB')
            print('Encerrando o programa...\n')
            break


        #A parte abaixo faz o recorte das bordas da imagem
        #----------------------------------------------------------------------------------------------------------------------------------------
        if setCropEdge == 'ND':
            setCropEdge = SetProcOptions.setCropImg(MapOP, element, MapaGray)            
         
        if setCropEdge[0] == 'sim':
            print('\nCortando as bordas...')
            MapaGray = MapOP.RemoveEdge(MapaGray, setCropEdge[1], setCropEdge[2])


        #A parte de baixo é para determinar o cálculo de escala para as imagens
        #----------------------------------------------------------------------------------------------------------------------------------------
        if setImgScale == 'ND':
            setImgScale = SetProcOptions.setScale(MapOP)
            
        if setImgScale != 'nao':
            LengthToPixelRatio = setImgScale

        #A parte abaixo binariza a imagem
        #----------------------------------------------------------------------------------------------------------------------------------------
        MapaGrayF = MapOP.GaussFilter(MapaGray, 0.7)
        MapBIN = SetProcOptions.BINImg(MapOP, element, MapaGrayF)        
        
        DicMapasCollection[element] = MapaGray
        DicMapasCollectionBIN[element] = MapBIN
            

#A parte de baixo introduz os módulos do programa
#----------------------------------------------------------------------------------------------------------------------------------------
        
if len(MapsImported) == 0:
    print(separator)
    print('ENCERRANDO O PROGRAMA...\n')
    quit()

else:
    print('\n--------MAPAS IMPORTADOS e BINARIZADOS!----------')
    print('\nIniciando os módulos de processamento...')
    
    PltMap = PlotMaps(DicMapasCollection, DicMapasCollectionBIN, Import.getSampleName(), Import.getImageFormat())

    while True:    
        print(separator)
        print('Digite o módulo de processamento.')
        print('(Digite *help* para mais informações)')
        EnterModule = str(input())
        
        if EnterModule.lower() == 'findautooverlap':
            if len(MapsImported) >= 2:
                if setImgScale != 'nao':
                    PltMap.PlotOverlaps(LengthToPixelRatio)
                elif setImgScale == 'nao':
                    PltMap.PlotOverlaps()
            else:
                Erros.Errors.simpleError()
                print('Para usar esse módulo vc precisa importar pelo menos 2 mapas.')
                print('Reinicie o programa e importe mais mapas.')
                continue    
                
        elif EnterModule.lower() == 'findelementoverlap':
            if len(MapsImported) >= 2:
                if setImgScale != 'nao':
                    PltMap.ElementColorOverlay(LengthToPixelRatio)
                elif setImgScale == 'nao':
                    PltMap.ElementColorOverlay()

            else:
                Erros.Errors.simpleError()
                print('Para usar esse módulo vc precisa importar pelo menos 2 mapas.')
                print('Reinicie o programa e importe mais mapas.')
                continue    
        
        elif EnterModule.lower() == 'findcompoundoverlap':
            if len(MapsImported) >= 2:
                if setImgScale != 'nao':
                    PltMap.CompoundColorOverlay(LengthToPixelRatio)
                elif setImgScale == 'nao':
                    PltMap.CompoundColorOverlay()
            else:
                Erros.Errors.simpleError()
                print('Para usar esse módulo vc precisa importar pelo menos 2 mapas.')
                print('Reinicie o programa e importe mais mapas.')
                continue    

        elif EnterModule.lower() == 'plotpanel':
            if len(MapsImported) >= 2:
                if setImgScale != 'nao':
                    PltMap.PlotPanel(LengthToPixelRatio)
                elif setImgScale == 'nao':
                    PltMap.PlotPanel()
            else:
                Erros.Errors.simpleError()
                print('Para usar esse módulo vc precisa importar pelo menos 2 mapas.')
                print('Reinicie o programa e importe mais mapas.')
                continue    

        elif EnterModule.lower() == 'findparticledistribution':
            while True:
                if setImgScale != 'nao':
                    PltMap.FindPartDist(LengthToPixelRatio)
                    break
                
                elif setImgScale == 'nao':
                    separator
                    Erros.Errors.simpleError()
                    print('Definir a escala do mapa para executar o modo FindParticleDistribution.')
                    setImgScale = SetProcOptions.setScale(MapOP)
                        
                    if setImgScale != 'nao':
                        LengthToPixelRatio = setImgScale
                        continue
        
        elif EnterModule.lower() == 'findporosity':
            if setImgScale != 'nao':
                PltMap.Get_pore(LengthToPixelRatio)
            else:
                PltMap.Get_pore()
           
        elif EnterModule.lower() == 'help':
            helpMods()
            pass
        
        elif EnterModule.lower() == 'sair':
            quit()       
        
        else:
            Erros.Errors.NotAModule()
            continue
   
print(separator)
print('ENCERRANDO O PROGRAMA...\n')
