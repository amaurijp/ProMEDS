
class ImOP(object):
    '''Define várias operações a serem feitas sobre uma imagem'''
    
    import Erros
    import numpy as np
    
    global Erros
    global np
    
    def __init__(self, ImageArray):        
        
        self.ImageArray = ImageArray #ndarray representando a imagem inicial (não será modificada ao longo das operações)
        self.Red = 0 #Canal Red de imagens RBG
        self.Green = 0 #Canal Green de imagens RBG
        self.Blue = 0 #Canal Blue de imagens RBG
        

    def ImageType(self):
        '''Identifica se a imagem é grayscale ou RGB'''
        
        print('Identificando as propriedades da imagem...')
        if len(self.ImageArray.shape) == 2 or len(self.ImageArray.shape) == 3:
            #Testa se a imagem só tem um canal
            if len(self.ImageArray.shape) == 2:
                #Testa se a imagem é binarizada
                if self.isBIN(self.ImageArray) == False:     
                    print('GrayScale Image (1 channel)')
                    self.Type = 'Grayscale'                    
                    return self.Type
                
                else:
                    Erros.Errors.BINImgFound()
                    self.Type = 'Binary'
                    return self.Type
                 
            elif len(self.ImageArray.shape) == 3:
                #Testa se a imagem é RGB ou RGBA
                y, x, RGBChannel = self.ImageArray.shape
                imgFlat = self.ImageArray.reshape(y * x, RGBChannel)
                
                RGBDetect = False
                for RGBVal_Number in range(len(imgFlat)):
                    if imgFlat[RGBVal_Number][0] != imgFlat[RGBVal_Number][1] or imgFlat[RGBVal_Number][0] != imgFlat[RGBVal_Number][2] or imgFlat[RGBVal_Number][1] != imgFlat[RGBVal_Number][2]:
                        RGBDetect = True
                        break
                
                if RGBDetect == True:
                    print('RGB Image (3 channels)') 
                    self.Type = 'RGB'
                    return self.Type
                
                else:
                    print('GrayScale Image (1 channel)')
                    self.ImageArray = self.ImageArray[:,:,0]
                    self.Type = 'Grayscale'
                    return self.Type
      
        else:
            Erros.Errors.ArrayInWrongDimensions()
            return


    def checkImageSize(self):
        
        from skimage import transform
        
        #caso a imagem seja muito grande ( width > 2000)
        if self.ImageArray.shape[1] > 2000:
            print('Atenção: A imagem importada é muito grande (largura de ', self.ImageArray.shape[1] ,' pixels).')
            while True:            
                print('Deseja diminuir o tamanho da image? (S (sim) ou N (não))')
                checkImageSize_input = str(input())
                if checkImageSize_input.lower() in ('s', 'n', 'sim', 'nao', 'não'):
                    if checkImageSize_input.lower() in ('s', 'sim'):
                        rsf = 2000 / self.ImageArray.shape[1]
                        multichannel = False
                        if self.Type == 'RGB':
                            multichannel = True
                        print('Reduzindo o tamanho da imagem para 2000 pixels de largura (width)...')
                        self.ImageArray = transform.rescale(self.ImageArray, rsf, mode='reflect', anti_aliasing = False, preserve_range = True, multichannel = multichannel)
                        break
                    
                    elif checkImageSize_input.lower() in ('n', 'nao', 'não'):
                        break                        

                else:
                    print('ERRO!')
                    print('Digite um valor válido (S ou N).')

    def isBIN(self, ImageArray):
        '''Checa se a imagem é binarizada'''
        ImgEx = np.where(ImageArray == 255, 0, ImageArray) 
        if ImgEx.max() == 0:
            return True
        
        else:
            return False
        
    
    def GaussFilter(self, ImageArray, sigma):
        from skimage import filters
        
        '''Aplica um filtro gaussiano na imagem'''
        print('Filtrando a imagem...')      
        filtImg = filters.gaussian(ImageArray, sigma)      
        return filtImg
 
    
    def Binarize(self, ImageArray, Threshold):
        '''Binariza a imagem'''
        print('Binarizando a imagem...')
        Normalized_ImageArray = ImageArray / ImageArray.max()
        BinImg = np.where(Normalized_ImageArray >= Threshold, 255, 0)
        self.ImageArrayBIN = BinImg
        return self.ImageArrayBIN
    

    def compareBIN(self, element, ImageArray, Threshold):
        '''função que comprara a imagem binarizada com a raw'''            
        
        import matplotlib.pyplot as plt
        
        Fig_compareBIN = plt.figure(figsize=(20, 8),facecolor='w', edgecolor='k')
        Fig_compareBIN.suptitle('Confira o valor de `THRESHOLD` usado (para continuar, feche essa janela)', fontsize=25)
        Fig_compareBIN_g1=plt.subplot2grid((1,2),(0,0),rowspan=1,colspan=1)
        Fig_compareBIN_g1.set_title('Mapa ' + element + ' (in grayscale)', fontsize=20)
        Fig_compareBIN_g1.tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False)
        Fig_compareBIN_g1.tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False)
        Fig_compareBIN_g1.imshow(ImageArray, cmap='gray')                                
        
        Fig_compareBIN_g2=plt.subplot2grid((1,2),(0,1),rowspan=1,colspan=1)
        Fig_compareBIN_g2.set_title('Mapa ' + element + ' (Binarizado com ' + str(Threshold) + ' de THRESHOLD)', fontsize=20)                                
        Fig_compareBIN_g2.tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False)
        Fig_compareBIN_g2.tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False)
        Fig_compareBIN_g2.imshow(self.Binarize(ImageArray, Threshold))
        
        plt.show()


    def RemoveEdge(self, ImageArray, Xboard_perc, Yboard_perc):
        '''Remove a borda da image'''
        
        #Introduzir um while loop aqui com o input Xboard_perc, Yboard_perc e plotar comparação com o Matplotlib
        
        imageCut = ImageArray[0 + round(((Yboard_perc/100)/2) * self.ImageArray.shape[0]) : self.ImageArray.shape[0] - round(((Yboard_perc/100)/2) * self.ImageArray.shape[0]) , 0 + round(((Xboard_perc/100)/2) * self.ImageArray.shape[1]) : self.ImageArray.shape[1] - round(((Xboard_perc/100)/2) * self.ImageArray.shape[1])]
                
        self.ImageArrayCrop = imageCut
        return self.ImageArrayCrop


    def compareCrops(self, ImageName, ImageArray, Xboard_perc, Yboard_perc):
        '''Compara a imagem croppada com a raw'''
        
        import matplotlib.pyplot as plt
        
        Fig_compareCrop = plt.figure(figsize=(20, 8),facecolor='w', edgecolor='k')
        Fig_compareCrop.suptitle('Confira a borda recortada (para continuar, feche essa janela)', fontsize=25)
        Fig_compareCrop_g1=plt.subplot2grid((1,2),(0,0),rowspan=1,colspan=1)
        Fig_compareCrop_g1.set_title('Mapa ' + ImageName + ' (Raw)', fontsize=20)
        Fig_compareCrop_g1.tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False)
        Fig_compareCrop_g1.tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False)
        Fig_compareCrop_g1.imshow(ImageArray, cmap='gray')                                
        
        Fig_compareCrop_g2=plt.subplot2grid((1,2),(0,1),rowspan=1,colspan=1)
        Fig_compareCrop_g2.set_title('Mapa ' + ImageName + ' (Borda recortada: ' + str(Xboard_perc) + '%)', fontsize=20)                                
        Fig_compareCrop_g2.tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False)
        Fig_compareCrop_g2.tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False)
        Fig_compareCrop_g2.imshow(self.RemoveEdge(ImageArray, Xboard_perc, Yboard_perc), cmap='gray')
        
        plt.show()
    

    def RGBtoGray(self):
        '''Converte a imagem RBG para Grayscale'''
        
        if self.Type == 'RGB':
            print('RGB Image: Separando os 3 canais (Red, Green, Blue)...')    
            G_IMG = np.zeros(self.ImageArray.shape[:-1])
            
            for Yval in range(self.ImageArray.shape[0]):
                for Xval in range(self.ImageArray.shape[1]):
                    G_IMG[Yval, Xval] = (self.ImageArray[Yval, Xval, 0] * 0.3) + (self.ImageArray[Yval, Xval, 1] * 0.59) + (self.ImageArray[Yval, Xval, 2] * 0.11)
            
            self.Red = self.ImageArray[:,:,0]
            self.Green = self.ImageArray[:,:,1]
            self.Blue = self.ImageArray[:,:,2]
            G_IMG = G_IMG / G_IMG.max()
            self.ImageArray = G_IMG
            
            return G_IMG
            
        else:
            Erros.Errors.NotRBGImg()


    def getRawImage(self): #Retorna a imagem sem nenhuma modificação
        return self.ImageArray
    
    def getRedChannel(self):
        return self.Red
    
    def getGreenChannel(self):
        return self.Green
    
    def getBlueChannel(self):
        return self.Blue
        
    def getNumberPixelsInX(self):
        return self.ImageArray.shape[1]

    def getNumberPixelsInY(self):
        return self.ImageArray.shape[0]
    
    def ExportRGBChannels(self, SampleName, rootName, formato, ImageName):
        '''Exporta as imagens com Canais Separados'''
        
        import os
        from skimage import io
    
        folder = os.getcwd()
        
        io.imsave(folder + '/' + SampleName + '/' + rootName + ImageName + '_Red.' + formato, self.getRedChannel())
        io.imsave(folder + '/' + SampleName + '/' + rootName + ImageName + '_Green.' + formato, self.getGreenChannel())
        io.imsave(folder + '/' + SampleName + '/' + rootName + ImageName + '_Blue.' + formato, self.getBlueChannel())
    
    def LengthToPixelRatio(self, HorizontalFieldWidth):
        LengthToPixelRatio = HorizontalFieldWidth / self.getNumberPixelsInX()
        return LengthToPixelRatio
        