import Erros
import Help

#determina se os canais RGB serão exportados
def setRGBExport():
    
    while True:
        separarchannel = str(input('\nVocê deseja exportar os canais Red-Green-Blue para a pasta (S/N)?'))
        
        if separarchannel.lower() == 's' or separarchannel.lower() == 'sim':
            return 'sim'
        
        elif separarchannel.lower() == 'n' or separarchannel.lower() == 'nao' or separarchannel.lower() == 'não':
            return 'nao'
        
        elif separarchannel.lower() == 'sair':
            quit()
        
        elif separarchannel.lower() == 'help':
            Help.helpMods()
            continue
            
        else:
            Erros.Errors.booleanError()
            continue
        

#determina se as bordas serão cortadas
def setCropImg(MapOP, element, MapaGray): #MapOP é uma instância da classe Image Operations (ImOP)
    
    print('\n>>>>>>>>>>>>>>>>>>>>> CROP <<<<<<<<<<<<<<<<<<<<<<')
    print('As bordas das imagens podem conter artefatos indesejáveis para o processamento.')
    print('Ex: barras de informação, escala, nomes, etc')
    print('Recomenda-se recortar uma determinada área de borda.')
    while True:            
        print('Recortando as bordas...')
        cropEdge = str(input('Você deseja recortar as bordas das imagens (S/N)?'))
        
        if cropEdge.lower() == 's' or cropEdge.lower() == 'sim':
            while True:
                print('Recortando as bordas...')
                cropEdgeVal = str(input('\nInsira um valor inteiro de 0 a 50 (%) da área a ser recortada:\n'))
                if cropEdgeVal != 'sair' and cropEdgeVal != 'help':
                    try:
                        if 0 <= int(cropEdgeVal) <= 50:
                            Xboard_perc, Yboard_perc = int(cropEdgeVal), int(cropEdgeVal)
                            pass
                        
                        else:
                            Erros.Errors.wrongInput()
                            continue
                    
                    except ValueError:
                        Erros.Errors.wrongInput()
                        continue
                                                
                    while True:
                        print('Recortando as bordas...')
                        MapOP.compareCrops(element, MapaGray, Xboard_perc, Yboard_perc) #Compara as imagems com e sem o RemoveEdge
                        
                        print('\nTem certeza que deseja remover ' + str(Xboard_perc) + ' % das bordas das imagens importadas (S)?')
                        print('(Caso prefira, digite o novo valor de área de borda (de 0 a 50%) a ser removida)')
                        ConfirmCropEdgeVal = str(input())
                        if ConfirmCropEdgeVal.lower() == 'sim' or ConfirmCropEdgeVal.lower() == 's':
                            return ['sim', Xboard_perc, Yboard_perc]

                        elif ConfirmCropEdgeVal != 'sair' and ConfirmCropEdgeVal != 'help':
                            try: 
                                if 0 <= int(ConfirmCropEdgeVal) <= 50:
                                    Xboard_perc, Yboard_perc = int(ConfirmCropEdgeVal), int(ConfirmCropEdgeVal)
                                    continue
                                
                                else:
                                    Erros.Errors.wrongInput()
                                    print('Inserir *Sim* ou *S* para confirmar a remoção de borda, ou insira o novo valor de 0 a 50 (%)')
                                    continue
                            
                            except ValueError:                                                                
                                    Erros.Errors.wrongInput()
                                    print('Inserir *Sim* ou *S* para confirmar a remoção de borda, ou insira o novo valor de 0 a 50 (%)')
                                    continue                    
                            
                        elif ConfirmCropEdgeVal.lower() == 'sair':
                            quit()
                        
                        elif ConfirmCropEdgeVal.lower() == 'help':
                            Help.helpMods()
                            continue                        
                    
                    
                elif cropEdgeVal.lower() == 'sair':
                    quit()
                
                elif cropEdgeVal.lower() == 'help':
                    Help.helpMods()
                    continue
                
        
        elif cropEdge.lower() == 'n' or cropEdge.lower() == 'nao' or cropEdge.lower() == 'não':
            return 'nao'
        
        elif cropEdge.lower() == 'sair':
            quit()
            
        elif cropEdge.lower() == 'help':
            Help.helpMods()
            continue
        
        else:
            Erros.Errors.booleanError()
            continue
        
        
#determina se a escala será colocada nos paineis
def BINImg(MapOP, element, MapaGray):
    
    while True:
        print('\n>>>>>>>>>>>>>>>>>>> BINARIZE <<<<<<<<<<<<<<<<<<<<')
        print('Binarizando o mapa de ' + str(element) + '.')
        print('Insira o threshold para binarização (de 0.0 a 1.0):')
        print('(O separador decimal é o ponto (`.`))')
        BINTrh = str(input())
        if BINTrh != 'sair' and BINTrh != 'help':
            try:
                if 0 <= float(BINTrh) <= 1:
                    BinVal = round(float(BINTrh), 2)
                    pass
                
                else:
                    Erros.Errors.wrongInput()
                    continue                        
            
            except ValueError:
                Erros.Errors.wrongInput()
                continue
                
            while True:
                MapOP.compareBIN(element, MapaGray, BinVal)  #Compara as imagems com e sem a binarização
                
                ConfirmBINTrh = str(input('\nTem certeza que deseja binarizar a imagem com o valor de `THRESHOLD` de ' + str(BinVal) + ' (S)?\n(Caso prefira, digite o novo valor de `THRESHOLD` (de 0 a 1) a ser usado)\n'))
                if ConfirmBINTrh != 'sair' and ConfirmBINTrh != 'help':
                    try: 
                        if 0 <= float(ConfirmBINTrh) <= 1:
                            BinVal = round(float(ConfirmBINTrh), 2)
                            pass
                        
                        else:
                            Erros.Errors.wrongInput()
                            continue
                    
                    except ValueError:                                                                
                        if ConfirmBINTrh.lower() == 'sim' or ConfirmBINTrh.lower() == 's':
                            MapBIN = MapOP.Binarize(MapaGray, BinVal)
                            return MapBIN                                                        
                            
                        else:
                            Erros.Errors.wrongInput()
                            print('Inserir *Sim* ou *S* para confirmar a remoção de borda, ou insira o novo valor de 0.0 a 1.0')
                            continue
                
                elif ConfirmBINTrh.lower() == 'sair':
                    quit()
    
                elif ConfirmBINTrh.lower() == 'help':
                    Help.helpMods()
                    continue                            
        
        elif BINTrh.lower() == 'sair':
            quit()
            
        elif BINTrh.lower() == 'help':
            Help.helpMods()
            continue
        

#determina se a escala será colocada nos paineis
def setScale(MapOP):
    
    print('\n>>>>>>>>>>>>>>>>>>> SETSCALE <<<<<<<<<<<<<<<<<<<<')
    print('Você deseja introduzir a escala de comprimento nos mapas importados? (S/N)')
    while True:
        setHFW = str(input())
        
        if setHFW.lower() == 's' or setHFW.lower() == 'sim':
            while True:
                print('')
                print('Insira o valor de largura de campo horizontal - Horizontal Field Width ou HFW - em micrômetros:')
                print('(O HFW corresponde à largura do mapa elementar. Assume-se que seja igual para todos os mapas importados)')
                setHorizontalFieldWidth = str(input())
                if setHorizontalFieldWidth.lower() != 'sair' and setHorizontalFieldWidth.lower() != 'help':
                    try:
                        HorizontalFieldWidth = float(setHorizontalFieldWidth)
                        
                        print('\nEncontrando os parâmetros de escala...')
                        setImgScale = MapOP.LengthToPixelRatio(HorizontalFieldWidth)                                
                        return setImgScale
                    
                    except ValueError:
                        Erros.Errors.wrongInput()
                        continue
                
                elif setHorizontalFieldWidth.lower() == 'sair':
                    quit()
                        
                elif setHorizontalFieldWidth.lower() == 'help':
                    Help.helpMods()
                    continue
        
        elif setHFW.lower() == 'n' or setHFW.lower() == 'nao' or setHFW.lower() == 'não':
            setImgScale = 'nao'
            return setImgScale
        
        elif setHFW.lower() == 'sair':
            quit()
            
        elif setHFW.lower() == 'help':
            Help.helpMods()
            continue
        
        else:
            Erros.Errors.booleanError()
            continue