
class PlotMaps(object):
    '''Define as funções para serem aplicadas ao um conjunto de mapas elementares'''
    
    global plt
    global np
    global Erros
    global In
    global helpMods
    global os
    global itt
    global Export

    from matplotlib import pyplot as plt
    import numpy as np
    import itertools as itt
    import Erros
    import InputEDS as In
    import os
    from Help import helpMods
    import Export
    
    global overMapList
    
    global separator
    separator = '\n-------------------------------------------------'
    
    def __init__(self, DictionaryGrayscaleMaps, DictionaryBinarizedMaps, SampleName, formato): #inicia a classe com o dicionário de mapas importados
        
        self.GrayMapsDic = DictionaryGrayscaleMaps
        self.GrayMapsList = [DictionaryGrayscaleMaps[element] for element in sorted(DictionaryGrayscaleMaps.keys())]
        self.BINMapsDic = DictionaryBinarizedMaps
        self.BINMapsList = [DictionaryBinarizedMaps[element] for element in sorted(DictionaryBinarizedMaps.keys())]
        self.elementsImported = sorted(DictionaryBinarizedMaps.keys())
        self.folder = os.getcwd()
        self.SampleName = SampleName
        self.formato = formato
        self.overMapList = 0
    
    
    
    
    #função para encontrar as sobreposições dos elementos
    def getElementsOverlapMaps(self):    
        
        combinationList=[]
        overList = []
        
        for element1 in self.elementsImported:
            for element2 in self.elementsImported:
                
                if element1 != element2 and [element1, element2] not in combinationList and [element1, element2] not in combinationList:                
                    
                    combinationList.append([element1,element2])
                    combinationList.append([element2,element1])
                    
                    OverlapImage = np.zeros([self.BINMapsDic[element1].shape[0], self.BINMapsDic[element1].shape[1]])    
                    
                    for YPOS in list(range(len(self.BINMapsDic[element1]))):
                        for XPOS in list(range(len(self.BINMapsDic[element1][YPOS]))):
                            if self.BINMapsDic[element1][YPOS, XPOS] == 255 and self.BINMapsDic[element2][YPOS, XPOS] == 255:
                                OverlapImage[YPOS, XPOS] = 255
                                
                    if OverlapImage.max() == 255:
                        overList.append([OverlapImage, element1, element2])
                        
                else:
                    continue
        
        return overList
    


        
    # função para encontrar uma colobar com cores discretas
    def getDiscrete_cmap(self, N, base_cmap=None):
        """Create an N-bin discrete colormap from the specified input map"""
    
        # Note that if base_cmap is a string or None, you can simply do
        # return plt.cm.get_cmap(base_cmap, N)
        # The following works for string, None, or a colormap instance:
    
        base = plt.cm.get_cmap(base_cmap)
        color_list = base(np.linspace(0, 1, N))
        cmap_name = base.name + str(N)
        
        return(base.from_list(cmap_name, color_list, N))
  
    
    
    
    # função que importa uma lista de funções de cores
    def getCmapList(self):
        ColorMapList = open(self.folder + '/Modules/ColorMapList.txt')
        CmapList = [line[:-1] for line in ColorMapList.readlines()]
        
        return CmapList
    
    
    
    
    # função que plota todos os mapas importados em escala de cores
    def PlotPanel(self, LengthToPixelRatio = False):
        
        #self.overMapList é uma lista no formato [mapa, elemento sobreposto 1, elemento sobreposto 2]
        #ex: [ndarray1, 'O', 'Si']
        
        print(separator)
        print('Entrando no módulo PlotPanels...')
        
        if len(self.elementsImported) == 1:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((1,1),(0,0),rowspan=1,colspan=1)
            
        elif len(self.elementsImported) == 2:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((1,2),(0,0),rowspan=1,colspan=1)
            g2=plt.subplot2grid((1,2),(0,1),rowspan=1,colspan=1)
            
        elif len(self.elementsImported) == 3:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((1,3),(0,0),rowspan=1,colspan=1)
            g2=plt.subplot2grid((1,3),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((1,3),(0,2),rowspan=1,colspan=1)
            
        elif 2 < len(self.elementsImported) <= 4:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,2),(0,0),rowspan=1,colspan=1)
            g2=plt.subplot2grid((2,2),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,2),(1,0),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,2),(1,1),rowspan=1,colspan=1)
    
        elif 4 < len(self.elementsImported) <= 6:
            fig1=plt.figure(figsize=(10, 8),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,3),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,3),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,3),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,3),(1,0),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,3),(1,1),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,3),(1,2),rowspan=1,colspan=1)
        
        elif 6 < len(self.elementsImported) <= 8:
            fig1=plt.figure(figsize=(12, 8),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,4),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,4),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,4),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,4),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,4),(1,0),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,4),(1,1),rowspan=1,colspan=1)
            g7=plt.subplot2grid((2,4),(1,2),rowspan=1,colspan=1)
            g8=plt.subplot2grid((2,4),(1,3),rowspan=1,colspan=1)
            
        elif 8 < len(self.elementsImported) <= 10:
            fig1=plt.figure(figsize=(14, 7),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,5),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,5),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,5),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,5),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,5),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,5),(1,0),rowspan=1,colspan=1)
            g7=plt.subplot2grid((2,5),(1,1),rowspan=1,colspan=1)
            g8=plt.subplot2grid((2,5),(1,2),rowspan=1,colspan=1)
            g9=plt.subplot2grid((2,5),(1,3),rowspan=1,colspan=1)
            g10=plt.subplot2grid((2,5),(1,4),rowspan=1,colspan=1)
    
        elif 10 < len(self.elementsImported) <= 12:
            fig1=plt.figure(figsize=(14, 16),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((3,4),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((3,4),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((3,4),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((3,4),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((3,4),(1,0),rowspan=1,colspan=1)
            g6=plt.subplot2grid((3,4),(1,1),rowspan=1,colspan=1)
            g7=plt.subplot2grid((3,4),(1,2),rowspan=1,colspan=1)
            g8=plt.subplot2grid((3,4),(1,3),rowspan=1,colspan=1)
            g9=plt.subplot2grid((3,4),(2,0),rowspan=1,colspan=1)
            g10=plt.subplot2grid((3,4),(2,1),rowspan=1,colspan=1)
            g11=plt.subplot2grid((3,4),(2,2),rowspan=1,colspan=1)
            g12=plt.subplot2grid((3,4),(2,3),rowspan=1,colspan=1)
            
        elif 12 < len(self.elementsImported) <= 14:
            fig1=plt.figure(figsize=(10, 16),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,7),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,7),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,7),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,7),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,7),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,7),(0,5),rowspan=1,colspan=1)
            g7=plt.subplot2grid((2,7),(0,6),rowspan=1,colspan=1)
            g8=plt.subplot2grid((2,7),(1,0),rowspan=1,colspan=1)
            g9=plt.subplot2grid((2,7),(1,1),rowspan=1,colspan=1)
            g10=plt.subplot2grid((2,7),(1,2),rowspan=1,colspan=1)
            g11=plt.subplot2grid((2,7),(1,3),rowspan=1,colspan=1)
            g12=plt.subplot2grid((2,7),(1,4),rowspan=1,colspan=1)
            g13=plt.subplot2grid((2,7),(1,5),rowspan=1,colspan=1)
            g14=plt.subplot2grid((2,7),(1,6),rowspan=1,colspan=1)
            
        elif 14 < len(self.elementsImported) <= 16:
            fig1=plt.figure(figsize=(14, 14),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((4,4),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((4,4),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((4,4),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((4,4),(1,0),rowspan=1,colspan=1)
            g6=plt.subplot2grid((4,4),(1,1),rowspan=1,colspan=1)
            g7=plt.subplot2grid((4,4),(1,2),rowspan=1,colspan=1)
            g8=plt.subplot2grid((4,4),(1,3),rowspan=1,colspan=1)
            g9=plt.subplot2grid((4,4),(2,0),rowspan=1,colspan=1)
            g10=plt.subplot2grid((4,4),(2,1),rowspan=1,colspan=1)
            g11=plt.subplot2grid((4,4),(2,2),rowspan=1,colspan=1)
            g12=plt.subplot2grid((4,4),(2,3),rowspan=1,colspan=1)
            g13=plt.subplot2grid((4,4),(3,0),rowspan=1,colspan=1)
            g14=plt.subplot2grid((4,4),(3,1),rowspan=1,colspan=1)
            g15=plt.subplot2grid((4,4),(3,2),rowspan=1,colspan=1)
            g16=plt.subplot2grid((4,4),(3,3),rowspan=1,colspan=1)
            
        elif 17 < len(self.elementsImported) <= 18:
            fig1=plt.figure(figsize=(15, 20),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((3,6),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((3,6),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((3,6),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((3,6),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((3,6),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((3,6),(0,5),rowspan=1,colspan=1)
            g7=plt.subplot2grid((3,6),(1,0),rowspan=1,colspan=1)
            g8=plt.subplot2grid((3,6),(1,1),rowspan=1,colspan=1)
            g9=plt.subplot2grid((3,6),(1,2),rowspan=1,colspan=1)
            g10=plt.subplot2grid((3,6),(1,3),rowspan=1,colspan=1)
            g11=plt.subplot2grid((3,6),(1,4),rowspan=1,colspan=1)
            g12=plt.subplot2grid((3,6),(1,5),rowspan=1,colspan=1)
            g13=plt.subplot2grid((3,6),(2,0),rowspan=1,colspan=1)
            g14=plt.subplot2grid((3,6),(2,1),rowspan=1,colspan=1)
            g15=plt.subplot2grid((3,6),(2,2),rowspan=1,colspan=1)
            g16=plt.subplot2grid((3,6),(2,3),rowspan=1,colspan=1)
            g17=plt.subplot2grid((3,6),(2,4),rowspan=1,colspan=1)
            g18=plt.subplot2grid((3,6),(2,5),rowspan=1,colspan=1)
       
        plt.subplots_adjust(wspace=1, hspace=1)
        
        CmapList = self.getCmapList()

        while True:
            print(separator)             
            print('Quais mapas você deseja montar o painel?')
            print('Com as imagens originais (*RAW*) ou as binarizadas (*BIN*)?')
            plotMode = str(input())
            
            if plotMode.lower() == 'bin':
                MapInList = self.BINMapsList
                break
            
            elif plotMode.lower() == 'raw':
                MapInList = self.GrayMapsList
                break
    
            elif plotMode.lower() == 'sair':                        
                quit()
    
            elif plotMode.lower() == 'help':
                helpMods()
            
            else:
                Erros.Errors.wrongInput()
                print('Inserir um *RAW* para montar o painel com as imagens originais.')
                print('Inserir um *BIN* para montar o painel com as imagens binarizadas.')
                continue
        
        
        print('Plotando os mapas importados...')
        for MapListN in list(range(len(MapInList))):
            eval('g' + str(MapListN + 1)).set_title('Map ' + self.elementsImported[MapListN], fontsize=14)

            if LengthToPixelRatio == False:
                eval('g' + str(MapListN + 1)).tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
                eval('g' + str(MapListN + 1)).tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)

            elif LengthToPixelRatio != False:
                eval('g' + str(MapListN + 1)).set_ylabel('$\mu$m', labelpad=5, fontsize=14)
                eval('g' + str(MapListN + 1)).set_xlabel('$\mu$m', labelpad=5, fontsize=14)
                eval('g' + str(MapListN + 1)).tick_params(axis="y", labelleft=True, left=True, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
                eval('g' + str(MapListN + 1)).tick_params(axis="x", labelbottom=True, bottom=True, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)                
                eval('g' + str(MapListN + 1)).set_xticks([0, int(MapInList[MapListN].shape[1]/2), MapInList[MapListN].shape[1]-1])
                eval('g' + str(MapListN + 1)).set_xticklabels([str(0), str(int((MapInList[MapListN].shape[1]/2) * LengthToPixelRatio)), str(int(MapInList[MapListN].shape[1] * LengthToPixelRatio))])
                eval('g' + str(MapListN + 1)).set_yticks([0,int(MapInList[MapListN].shape[0]/2), MapInList[MapListN].shape[0]-1])
                eval('g' + str(MapListN + 1)).set_yticklabels([str(int(MapInList[MapListN].shape[0] * LengthToPixelRatio)), str(int((MapInList[MapListN].shape[0]/2) * LengthToPixelRatio)), str(0)])
    
            eval('g' + str(MapListN + 1)).imshow(MapInList[MapListN], alpha=0.8, cmap=CmapList[MapListN])
    
        plt.tight_layout()            
        fileNumber = Export.getFileNumber(self.folder, self.SampleName, 'PlotMaps', self.formato)
        fig1.savefig(self.folder + '/' + self.SampleName + '/' + 'PlotMaps' + fileNumber + '.' + self.formato, dpi = 400)

        plt.show()
        print('Saindo do módulo PlotPanel...')   
        
        
    
    
    # determinando a porosidade aproximada
    def Get_pore(self, LengthToPixelRatio = False):
        
        BIN_Img_list = self.BINMapsList
        
        PoreImg = np.zeros(BIN_Img_list[0].shape)
        for BIN_Img in BIN_Img_list:
            PoreImg = PoreImg + BIN_Img        
            
        BIN_ImgF = np.where(PoreImg == 0, 1, 0)
    
        pixels = BIN_ImgF.shape[0] * BIN_ImgF.shape[1]
    
        fig0=plt.figure(figsize=(6, 6),facecolor='w', edgecolor='k')
        cg0=plt.subplot2grid((1,1),(0,0), rowspan=1, colspan=1)
        cg0.set_title('Pore map (' + str(round((np.count_nonzero(BIN_ImgF)/pixels) * 100, 2)) + ' %-Area)', fontsize=14)
    
        #escala horizontal e vertical na imagens
        if LengthToPixelRatio == False: 
            cg0.tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
            cg0.tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)
        
        if LengthToPixelRatio != False:    
            cg0.set_xlabel('$\mu$m', labelpad=5, fontsize=14)
            cg0.set_ylabel('$\mu$m', labelpad=5, fontsize=14)
            
            cg0.set_xticks([0, int(BIN_Img_list[0].shape[1]/2), BIN_Img_list[0].shape[1]-1])
            cg0.set_xticklabels([str(0), str(int((BIN_Img_list[0].shape[1]/2) * LengthToPixelRatio)), str(int(BIN_Img_list[0].shape[1] * LengthToPixelRatio))])
            cg0.set_yticks([0,int(BIN_Img_list[0].shape[0]/2), BIN_Img_list[0].shape[0]-1])
            cg0.set_yticklabels([str(int(BIN_Img_list[0].shape[0] * LengthToPixelRatio)), str(int((BIN_Img_list[0].shape[0]/2) * LengthToPixelRatio)), str(0)])
    
        print('Plotando...')    
        cg0Axes = cg0.imshow(BIN_ImgF, cmap=self.getDiscrete_cmap(2, 'binary'))
    
        #barra de escala de cores
        Colbar0=fig0.colorbar(cg0Axes, fraction=0.04, 
                              pad=0.08, orientation='vertical',
                              ticks=list(np.arange(0 + 0.25, 1 + 0.25, 0.5)))
    
        Colbar0.set_ticklabels(['Background','Pore'])
        Colbar0.ax.tick_params(labelsize=11)
        
        plt.tight_layout()        
    
        fileNumber = Export.getFileNumber(self.folder, self.SampleName, 'PoreMap', self.formato)
        fig0.savefig(self.folder + '/' + self.SampleName + '/' + 'PoreMap' + fileNumber + '.' + self.formato, dpi = 400)    
        plt.show()
    
    

    
        
    def PlotOverlaps(self, LengthToPixelRatio = False): 
        #self.overMapList é uma lista no formato [mapa, elemento sobreposto 1, elemento sobreposto 2]
        #ex: [ndarray1, 'O', 'Si']
        
        print(separator)
        print('Entrando no módulo FindAutoOverlap...')
        print('Encontrando as sobreposições de todos os elementos importados...')
        
        if self.overMapList == 0:
            self.overMapList = self.getElementsOverlapMaps()
        
        if len(self.overMapList) == 1:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((1,1),(0,0),rowspan=1,colspan=1)
            
        elif len(self.overMapList) == 2:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((1,2),(0,0),rowspan=1,colspan=1)
            g2=plt.subplot2grid((1,2),(0,1),rowspan=1,colspan=1)
            
        elif 2 < len(self.overMapList) <= 4:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,2),(0,0),rowspan=1,colspan=1)
            g2=plt.subplot2grid((2,2),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,2),(1,0),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,2),(1,1),rowspan=1,colspan=1)
    
        elif 4 < len(self.overMapList) <= 6:
            fig1=plt.figure(figsize=(10, 8),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,3),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,3),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,3),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,3),(1,0),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,3),(1,1),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,3),(1,2),rowspan=1,colspan=1)
        
        elif 6 < len(self.overMapList) <= 8:
            fig1=plt.figure(figsize=(12, 8),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,4),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,4),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,4),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,4),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,4),(1,0),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,4),(1,1),rowspan=1,colspan=1)
            g7=plt.subplot2grid((2,4),(1,2),rowspan=1,colspan=1)
            g8=plt.subplot2grid((2,4),(1,3),rowspan=1,colspan=1)
            
        elif 8 < len(self.overMapList) <= 10:
            fig1=plt.figure(figsize=(14, 7),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,5),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,5),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,5),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,5),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,5),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,5),(1,0),rowspan=1,colspan=1)
            g7=plt.subplot2grid((2,5),(1,1),rowspan=1,colspan=1)
            g8=plt.subplot2grid((2,5),(1,2),rowspan=1,colspan=1)
            g9=plt.subplot2grid((2,5),(1,3),rowspan=1,colspan=1)
            g10=plt.subplot2grid((2,5),(1,4),rowspan=1,colspan=1)
    
        elif 10 < len(self.overMapList) <= 12:
            fig1=plt.figure(figsize=(14, 16),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((3,4),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((3,4),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((3,4),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((3,4),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((3,4),(1,0),rowspan=1,colspan=1)
            g6=plt.subplot2grid((3,4),(1,1),rowspan=1,colspan=1)
            g7=plt.subplot2grid((3,4),(1,2),rowspan=1,colspan=1)
            g8=plt.subplot2grid((3,4),(1,3),rowspan=1,colspan=1)
            g9=plt.subplot2grid((3,4),(2,0),rowspan=1,colspan=1)
            g10=plt.subplot2grid((3,4),(2,1),rowspan=1,colspan=1)
            g11=plt.subplot2grid((3,4),(2,2),rowspan=1,colspan=1)
            g12=plt.subplot2grid((3,4),(2,3),rowspan=1,colspan=1)
            
        elif 12 < len(self.overMapList) <= 14:
            fig1=plt.figure(figsize=(10, 16),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,7),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,7),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,7),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,7),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,7),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,7),(0,5),rowspan=1,colspan=1)
            g7=plt.subplot2grid((2,7),(0,6),rowspan=1,colspan=1)
            g8=plt.subplot2grid((2,7),(1,0),rowspan=1,colspan=1)
            g9=plt.subplot2grid((2,7),(1,1),rowspan=1,colspan=1)
            g10=plt.subplot2grid((2,7),(1,2),rowspan=1,colspan=1)
            g11=plt.subplot2grid((2,7),(1,3),rowspan=1,colspan=1)
            g12=plt.subplot2grid((2,7),(1,4),rowspan=1,colspan=1)
            g13=plt.subplot2grid((2,7),(1,5),rowspan=1,colspan=1)
            g14=plt.subplot2grid((2,7),(1,6),rowspan=1,colspan=1)
            
        elif 14 < len(self.overMapList) <= 16:
            fig1=plt.figure(figsize=(14, 14),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((4,4),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((4,4),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((4,4),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((4,4),(1,0),rowspan=1,colspan=1)
            g6=plt.subplot2grid((4,4),(1,1),rowspan=1,colspan=1)
            g7=plt.subplot2grid((4,4),(1,2),rowspan=1,colspan=1)
            g8=plt.subplot2grid((4,4),(1,3),rowspan=1,colspan=1)
            g9=plt.subplot2grid((4,4),(2,0),rowspan=1,colspan=1)
            g10=plt.subplot2grid((4,4),(2,1),rowspan=1,colspan=1)
            g11=plt.subplot2grid((4,4),(2,2),rowspan=1,colspan=1)
            g12=plt.subplot2grid((4,4),(2,3),rowspan=1,colspan=1)
            g13=plt.subplot2grid((4,4),(3,0),rowspan=1,colspan=1)
            g14=plt.subplot2grid((4,4),(3,1),rowspan=1,colspan=1)
            g15=plt.subplot2grid((4,4),(3,2),rowspan=1,colspan=1)
            g16=plt.subplot2grid((4,4),(3,3),rowspan=1,colspan=1)
            
        elif 17 < len(self.overMapList) <= 18:
            fig1=plt.figure(figsize=(15, 20),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((3,6),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((3,6),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((3,6),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((3,6),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((3,6),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((3,6),(0,5),rowspan=1,colspan=1)
            g7=plt.subplot2grid((3,6),(1,0),rowspan=1,colspan=1)
            g8=plt.subplot2grid((3,6),(1,1),rowspan=1,colspan=1)
            g9=plt.subplot2grid((3,6),(1,2),rowspan=1,colspan=1)
            g10=plt.subplot2grid((3,6),(1,3),rowspan=1,colspan=1)
            g11=plt.subplot2grid((3,6),(1,4),rowspan=1,colspan=1)
            g12=plt.subplot2grid((3,6),(1,5),rowspan=1,colspan=1)
            g13=plt.subplot2grid((3,6),(2,0),rowspan=1,colspan=1)
            g14=plt.subplot2grid((3,6),(2,1),rowspan=1,colspan=1)
            g15=plt.subplot2grid((3,6),(2,2),rowspan=1,colspan=1)
            g16=plt.subplot2grid((3,6),(2,3),rowspan=1,colspan=1)
            g17=plt.subplot2grid((3,6),(2,4),rowspan=1,colspan=1)
            g18=plt.subplot2grid((3,6),(2,5),rowspan=1,colspan=1)
    
        elif 18 < len(self.overMapList) <= 20:
            fig1=plt.figure(figsize=(16, 18),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((4,5),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((4,5),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((4,5),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((4,5),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((4,5),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((4,5),(1,0),rowspan=1,colspan=1)
            g7=plt.subplot2grid((4,5),(1,1),rowspan=1,colspan=1)
            g8=plt.subplot2grid((4,5),(1,2),rowspan=1,colspan=1)
            g9=plt.subplot2grid((4,5),(1,3),rowspan=1,colspan=1)
            g10=plt.subplot2grid((4,5),(1,4),rowspan=1,colspan=1)
            g11=plt.subplot2grid((4,5),(2,0),rowspan=1,colspan=1)
            g12=plt.subplot2grid((4,5),(2,1),rowspan=1,colspan=1)
            g13=plt.subplot2grid((4,5),(2,2),rowspan=1,colspan=1)
            g14=plt.subplot2grid((4,5),(2,3),rowspan=1,colspan=1)
            g15=plt.subplot2grid((4,5),(2,4),rowspan=1,colspan=1)
            g16=plt.subplot2grid((4,5),(3,0),rowspan=1,colspan=1)
            g17=plt.subplot2grid((4,5),(3,1),rowspan=1,colspan=1)
            g18=plt.subplot2grid((4,5),(3,2),rowspan=1,colspan=1)
            g19=plt.subplot2grid((4,5),(3,3),rowspan=1,colspan=1)
            g20=plt.subplot2grid((4,5),(3,4),rowspan=1,colspan=1)
    
        elif 20 < len(self.overMapList) <= 25:
            fig1=plt.figure(figsize=(18, 18),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((5,5),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((5,5),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((5,5),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((5,5),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((5,5),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((5,5),(1,0),rowspan=1,colspan=1)
            g7=plt.subplot2grid((5,5),(1,1),rowspan=1,colspan=1)
            g8=plt.subplot2grid((5,5),(1,2),rowspan=1,colspan=1)
            g9=plt.subplot2grid((5,5),(1,3),rowspan=1,colspan=1)
            g10=plt.subplot2grid((5,5),(1,4),rowspan=1,colspan=1)
            g11=plt.subplot2grid((5,5),(2,0),rowspan=1,colspan=1)
            g12=plt.subplot2grid((5,5),(2,1),rowspan=1,colspan=1)
            g13=plt.subplot2grid((5,5),(2,2),rowspan=1,colspan=1)
            g14=plt.subplot2grid((5,5),(2,3),rowspan=1,colspan=1)
            g15=plt.subplot2grid((5,5),(2,4),rowspan=1,colspan=1)
            g16=plt.subplot2grid((5,5),(3,0),rowspan=1,colspan=1)
            g17=plt.subplot2grid((5,5),(3,1),rowspan=1,colspan=1)
            g18=plt.subplot2grid((5,5),(3,2),rowspan=1,colspan=1)
            g19=plt.subplot2grid((5,5),(3,3),rowspan=1,colspan=1)
            g20=plt.subplot2grid((5,5),(3,4),rowspan=1,colspan=1)
            g21=plt.subplot2grid((5,5),(4,0),rowspan=1,colspan=1)
            g22=plt.subplot2grid((5,5),(4,1),rowspan=1,colspan=1)
            g23=plt.subplot2grid((5,5),(4,2),rowspan=1,colspan=1)
            g24=plt.subplot2grid((5,5),(4,3),rowspan=1,colspan=1)
            g25=plt.subplot2grid((5,5),(4,4),rowspan=1,colspan=1)
            
        elif 26 < len(self.overMapList) <= 36:
            fig1=plt.figure(figsize=(20, 20),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((6,6),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((6,6),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((6,6),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((6,6),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((6,6),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((6,6),(0,5),rowspan=1,colspan=1)
            g7=plt.subplot2grid((6,6),(1,0),rowspan=1,colspan=1)
            g8=plt.subplot2grid((6,6),(1,1),rowspan=1,colspan=1)
            g9=plt.subplot2grid((6,6),(1,2),rowspan=1,colspan=1)
            g10=plt.subplot2grid((6,6),(1,3),rowspan=1,colspan=1)
            g11=plt.subplot2grid((6,6),(1,4),rowspan=1,colspan=1)
            g12=plt.subplot2grid((6,6),(1,5),rowspan=1,colspan=1)
            g13=plt.subplot2grid((6,6),(2,0),rowspan=1,colspan=1)
            g14=plt.subplot2grid((6,6),(2,1),rowspan=1,colspan=1)
            g15=plt.subplot2grid((6,6),(2,2),rowspan=1,colspan=1)
            g16=plt.subplot2grid((6,6),(2,3),rowspan=1,colspan=1)
            g17=plt.subplot2grid((6,6),(2,4),rowspan=1,colspan=1)
            g18=plt.subplot2grid((6,6),(2,5),rowspan=1,colspan=1)    
            g19=plt.subplot2grid((6,6),(3,0),rowspan=1,colspan=1)
            g20=plt.subplot2grid((6,6),(3,1),rowspan=1,colspan=1)
            g21=plt.subplot2grid((6,6),(3,2),rowspan=1,colspan=1)
            g22=plt.subplot2grid((6,6),(3,3),rowspan=1,colspan=1)
            g23=plt.subplot2grid((6,6),(3,4),rowspan=1,colspan=1)
            g24=plt.subplot2grid((6,6),(3,5),rowspan=1,colspan=1)
            g25=plt.subplot2grid((6,6),(4,0),rowspan=1,colspan=1)
            g26=plt.subplot2grid((6,6),(4,1),rowspan=1,colspan=1)
            g27=plt.subplot2grid((6,6),(4,2),rowspan=1,colspan=1)
            g28=plt.subplot2grid((6,6),(4,3),rowspan=1,colspan=1)
            g29=plt.subplot2grid((6,6),(4,4),rowspan=1,colspan=1)
            g30=plt.subplot2grid((6,6),(4,5),rowspan=1,colspan=1)
            g31=plt.subplot2grid((6,6),(5,0),rowspan=1,colspan=1)
            g32=plt.subplot2grid((6,6),(5,1),rowspan=1,colspan=1)
            g33=plt.subplot2grid((6,6),(5,2),rowspan=1,colspan=1)
            g34=plt.subplot2grid((6,6),(5,3),rowspan=1,colspan=1)
            g35=plt.subplot2grid((6,6),(5,4),rowspan=1,colspan=1)
            g36=plt.subplot2grid((6,6),(5,5),rowspan=1,colspan=1)
    
        elif 37 < len(self.overMapList) <= 49:
            fig1=plt.figure(figsize=(20, 20),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((7,7),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((7,7),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((7,7),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((7,7),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((7,7),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((7,7),(0,5),rowspan=1,colspan=1)
            g7=plt.subplot2grid((7,7),(0,6),rowspan=1,colspan=1)      
            g8=plt.subplot2grid((7,7),(1,0),rowspan=1,colspan=1)
            g9=plt.subplot2grid((7,7),(1,1),rowspan=1,colspan=1)
            g10=plt.subplot2grid((7,7),(1,2),rowspan=1,colspan=1)
            g11=plt.subplot2grid((7,7),(1,3),rowspan=1,colspan=1)
            g12=plt.subplot2grid((7,7),(1,4),rowspan=1,colspan=1)
            g13=plt.subplot2grid((7,7),(1,5),rowspan=1,colspan=1)
            g14=plt.subplot2grid((7,7),(1,6),rowspan=1,colspan=1)
            g15=plt.subplot2grid((7,7),(2,0),rowspan=1,colspan=1)
            g16=plt.subplot2grid((7,7),(2,1),rowspan=1,colspan=1)
            g17=plt.subplot2grid((7,7),(2,2),rowspan=1,colspan=1)
            g18=plt.subplot2grid((7,7),(2,3),rowspan=1,colspan=1)
            g19=plt.subplot2grid((7,7),(2,4),rowspan=1,colspan=1)
            g20=plt.subplot2grid((7,7),(2,5),rowspan=1,colspan=1)
            g21=plt.subplot2grid((7,7),(2,6),rowspan=1,colspan=1)
            g22=plt.subplot2grid((7,7),(3,0),rowspan=1,colspan=1)
            g23=plt.subplot2grid((7,7),(3,1),rowspan=1,colspan=1)
            g24=plt.subplot2grid((7,7),(3,2),rowspan=1,colspan=1)
            g25=plt.subplot2grid((7,7),(3,3),rowspan=1,colspan=1)
            g26=plt.subplot2grid((7,7),(3,4),rowspan=1,colspan=1)
            g27=plt.subplot2grid((7,7),(3,5),rowspan=1,colspan=1)
            g28=plt.subplot2grid((7,7),(3,6),rowspan=1,colspan=1)
            g29=plt.subplot2grid((7,7),(4,0),rowspan=1,colspan=1)
            g30=plt.subplot2grid((7,7),(4,1),rowspan=1,colspan=1)
            g31=plt.subplot2grid((7,7),(4,2),rowspan=1,colspan=1)
            g32=plt.subplot2grid((7,7),(4,3),rowspan=1,colspan=1)
            g33=plt.subplot2grid((7,7),(4,4),rowspan=1,colspan=1)
            g34=plt.subplot2grid((7,7),(4,5),rowspan=1,colspan=1)
            g35=plt.subplot2grid((7,7),(4,6),rowspan=1,colspan=1)
            g36=plt.subplot2grid((7,7),(5,0),rowspan=1,colspan=1)
            g37=plt.subplot2grid((7,7),(5,1),rowspan=1,colspan=1)
            g38=plt.subplot2grid((7,7),(5,2),rowspan=1,colspan=1)
            g39=plt.subplot2grid((7,7),(5,3),rowspan=1,colspan=1)
            g40=plt.subplot2grid((7,7),(5,4),rowspan=1,colspan=1)
            g41=plt.subplot2grid((7,7),(5,5),rowspan=1,colspan=1)
            g42=plt.subplot2grid((7,7),(5,6),rowspan=1,colspan=1)
            g43=plt.subplot2grid((7,7),(6,0),rowspan=1,colspan=1)
            g44=plt.subplot2grid((7,7),(6,1),rowspan=1,colspan=1)
            g45=plt.subplot2grid((7,7),(5,2),rowspan=1,colspan=1)
            g46=plt.subplot2grid((7,7),(6,3),rowspan=1,colspan=1)
            g47=plt.subplot2grid((7,7),(6,4),rowspan=1,colspan=1)
            g48=plt.subplot2grid((7,7),(6,5),rowspan=1,colspan=1)
            g49=plt.subplot2grid((7,7),(6,6),rowspan=1,colspan=1)
    
        elif 50 < len(self.overMapList) <= 64:
            fig1=plt.figure(figsize=(20, 20),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((8,8),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((8,8),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((8,8),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((8,8),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((8,8),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((8,8),(0,5),rowspan=1,colspan=1)
            g7=plt.subplot2grid((8,8),(0,6),rowspan=1,colspan=1)      
            g8=plt.subplot2grid((8,8),(0,7),rowspan=1,colspan=1)
            g9=plt.subplot2grid((8,8),(1,0),rowspan=1,colspan=1)
            g10=plt.subplot2grid((8,8),(1,1),rowspan=1,colspan=1)
            g11=plt.subplot2grid((8,8),(1,2),rowspan=1,colspan=1)
            g12=plt.subplot2grid((8,8),(1,3),rowspan=1,colspan=1)
            g13=plt.subplot2grid((8,8),(1,4),rowspan=1,colspan=1)
            g14=plt.subplot2grid((8,8),(1,5),rowspan=1,colspan=1)
            g15=plt.subplot2grid((8,8),(1,6),rowspan=1,colspan=1)
            g16=plt.subplot2grid((8,8),(1,7),rowspan=1,colspan=1)
            g17=plt.subplot2grid((8,8),(2,0),rowspan=1,colspan=1)
            g18=plt.subplot2grid((8,8),(2,1),rowspan=1,colspan=1)
            g19=plt.subplot2grid((8,8),(2,2),rowspan=1,colspan=1)
            g20=plt.subplot2grid((8,8),(2,3),rowspan=1,colspan=1)
            g21=plt.subplot2grid((8,8),(2,4),rowspan=1,colspan=1)
            g22=plt.subplot2grid((8,8),(2,5),rowspan=1,colspan=1)
            g23=plt.subplot2grid((8,8),(2,6),rowspan=1,colspan=1)
            g24=plt.subplot2grid((8,8),(2,7),rowspan=1,colspan=1)
            g25=plt.subplot2grid((8,8),(3,0),rowspan=1,colspan=1)
            g26=plt.subplot2grid((8,8),(3,1),rowspan=1,colspan=1)
            g27=plt.subplot2grid((8,8),(3,2),rowspan=1,colspan=1)
            g28=plt.subplot2grid((8,8),(3,3),rowspan=1,colspan=1)
            g29=plt.subplot2grid((8,8),(3,4),rowspan=1,colspan=1)
            g30=plt.subplot2grid((8,8),(3,5),rowspan=1,colspan=1)
            g31=plt.subplot2grid((8,8),(3,6),rowspan=1,colspan=1)
            g32=plt.subplot2grid((8,8),(3,7),rowspan=1,colspan=1)
            g33=plt.subplot2grid((8,8),(4,0),rowspan=1,colspan=1)
            g34=plt.subplot2grid((8,8),(4,1),rowspan=1,colspan=1)
            g35=plt.subplot2grid((8,8),(4,2),rowspan=1,colspan=1)
            g36=plt.subplot2grid((8,8),(4,3),rowspan=1,colspan=1)
            g37=plt.subplot2grid((8,8),(4,4),rowspan=1,colspan=1)
            g38=plt.subplot2grid((8,8),(4,5),rowspan=1,colspan=1)
            g39=plt.subplot2grid((8,8),(4,6),rowspan=1,colspan=1)
            g40=plt.subplot2grid((8,8),(4,7),rowspan=1,colspan=1)
            g41=plt.subplot2grid((8,8),(5,0),rowspan=1,colspan=1)
            g42=plt.subplot2grid((8,8),(5,1),rowspan=1,colspan=1)
            g43=plt.subplot2grid((8,8),(5,2),rowspan=1,colspan=1)
            g44=plt.subplot2grid((8,8),(5,3),rowspan=1,colspan=1)
            g45=plt.subplot2grid((8,8),(5,4),rowspan=1,colspan=1)
            g46=plt.subplot2grid((8,8),(5,5),rowspan=1,colspan=1)
            g47=plt.subplot2grid((8,8),(5,6),rowspan=1,colspan=1)
            g48=plt.subplot2grid((8,8),(5,7),rowspan=1,colspan=1)
            g49=plt.subplot2grid((8,8),(6,0),rowspan=1,colspan=1)
            g50=plt.subplot2grid((8,8),(6,1),rowspan=1,colspan=1)
            g51=plt.subplot2grid((8,8),(6,2),rowspan=1,colspan=1)
            g52=plt.subplot2grid((8,8),(6,3),rowspan=1,colspan=1)
            g53=plt.subplot2grid((8,8),(6,4),rowspan=1,colspan=1)
            g54=plt.subplot2grid((8,8),(6,5),rowspan=1,colspan=1)
            g55=plt.subplot2grid((8,8),(6,6),rowspan=1,colspan=1)
            g56=plt.subplot2grid((8,8),(6,7),rowspan=1,colspan=1)
            g57=plt.subplot2grid((8,8),(7,0),rowspan=1,colspan=1)
            g58=plt.subplot2grid((8,8),(7,1),rowspan=1,colspan=1)
            g59=plt.subplot2grid((8,8),(7,2),rowspan=1,colspan=1)
            g60=plt.subplot2grid((8,8),(7,3),rowspan=1,colspan=1)
            g61=plt.subplot2grid((8,8),(7,4),rowspan=1,colspan=1)
            g62=plt.subplot2grid((8,8),(7,5),rowspan=1,colspan=1)
            g63=plt.subplot2grid((8,8),(7,6),rowspan=1,colspan=1)
            g64=plt.subplot2grid((8,8),(7,7),rowspan=1,colspan=1)
    
        
        plt.subplots_adjust(wspace=1, hspace=1)
        
        
        print('Plotando os Overlapped Maps...')
        for MapListN in list(range(len(self.overMapList))):
            eval('g' + str(MapListN + 1)).set_title('OverMap ' + self.overMapList[MapListN][1] + '-' + self.overMapList[MapListN][2], fontsize=14)

            if LengthToPixelRatio == False:
                eval('g' + str(MapListN + 1)).tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
                eval('g' + str(MapListN + 1)).tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)

            elif LengthToPixelRatio != False:
                eval('g' + str(MapListN + 1)).set_ylabel('$\mu$m', labelpad=5, fontsize=14)
                eval('g' + str(MapListN + 1)).set_xlabel('$\mu$m', labelpad=5, fontsize=14)
                eval('g' + str(MapListN + 1)).tick_params(axis="y", labelleft=True, left=True, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
                eval('g' + str(MapListN + 1)).tick_params(axis="x", labelbottom=True, bottom=True, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)                
                eval('g' + str(MapListN + 1)).set_xticks([0, int(self.overMapList[MapListN][0].shape[1]/2), self.overMapList[MapListN][0].shape[1]-1])
                eval('g' + str(MapListN + 1)).set_xticklabels([str(0), str(int((self.overMapList[MapListN][0].shape[1]/2) * LengthToPixelRatio)), str(int(self.overMapList[MapListN][0].shape[1] * LengthToPixelRatio))])
                eval('g' + str(MapListN + 1)).set_yticks([0,int(self.overMapList[MapListN][0].shape[0]/2), self.overMapList[MapListN][0].shape[0]-1])
                eval('g' + str(MapListN + 1)).set_yticklabels([str(int(self.overMapList[MapListN][0].shape[0] * LengthToPixelRatio)), str(int((self.overMapList[MapListN][0].shape[0]/2) * LengthToPixelRatio)), str(0)])
    
            eval('g' + str(MapListN + 1)).imshow(self.overMapList[MapListN][0], alpha=0.8, cmap='Purples')
    
        plt.tight_layout()            
        fileNumber = Export.getFileNumber(self.folder, self.SampleName, 'AllOverLay', self.formato)
        fig1.savefig(self.folder + '/' + self.SampleName + '/' + 'AllOverLay' + fileNumber + '.' + self.formato, dpi = 400)

        plt.show()
        print('Saindo do módulo FindAutoOverlap...')       
        
        
        
        
        
    # Encontrando as sobreposições de elementos
    def ElementColorOverlay(self, LengthToPixelRatio = False):

        import itertools as itt
        
        #Abaixo se introduz os elementos que serão plotados em ColorOverlay        
        #----------------------------------------------------------------------------------------------------------------------------
        
        print(separator)
        print('Entrando no módulo FindElementOverlap...')
        print('Nesse módulo você pode selecionar os elementos que deseja plotar as sobreposições.')
        print('Você pode selecionar de 2 a 4 elementos.')
        print('(Após inserir todos os elementos desejados, digite *continuar*)')
        
        elementsSelected = []
        while True:
            print(separator)
            print('Elementos importados:')                            
            for element in self.elementsImported:
                print(element)
            print(separator)             
            if len(elementsSelected) > 0:
                print('Elementos selecionados para plotagem:')                            
                for element in sorted(elementsSelected):
                    print(element)
            print(separator)             
            print('Selecione um elemento para plotar sobreposições:')
            print('(Após inserir todos os elementos desejados, digite *continuar*)')
            elementToPlot = str(input())
            
            if elementToPlot in self.elementsImported:                           
                if elementToPlot not in elementsSelected:
                    elementsSelected.append(elementToPlot)
                    elementsSelected.sort() #Organiza a lista de elementos selecionados alfabeticamente
                                        
                else:
                    Erros.Errors.ElementAlreadySelected(elementToPlot)
                
            elif elementToPlot.lower() == 'continuar':                        
                if len(elementsSelected) >= 2:                 
                    break
                
                else:
                    Erros.Errors.wrongInput()
                    print('Para usar esse módulo você precisa importar de 2 a 4 mapas.')
                    continue

            elif elementToPlot.lower() == 'sair':                        
                quit()

            elif elementToPlot.lower() == 'help':
                helpMods()
            
            else:
                Erros.Errors.wrongInput()
                print('Inserir um elemento que foi importado.')
                continue
        
        #----------------------------------------------------------------------------------------------------------------------------
        print('Plotando os mapas com os elementos selecionados...')
        if 2 <= len(elementsSelected) <= 4:
            
            fig2=plt.figure(figsize=(6, 6),facecolor='w', edgecolor='k')
            cg1=plt.subplot2grid((1,1),(0,0), rowspan=1, colspan=1)
            cg1.set_title('Color Overlay', fontsize=14)

            if LengthToPixelRatio == False:
                cg1.tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
                cg1.tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)
            
            if LengthToPixelRatio != False:
                cg1.set_xlabel('$\mu$m', labelpad=5, fontsize=14)
                cg1.set_ylabel('$\mu$m', labelpad=5, fontsize=14)            
                cg1.set_xticks([0, int(self.BINMapsList[0].shape[1]/2), self.BINMapsList[0].shape[1]-1])
                cg1.set_xticklabels([str(0), str(int((self.BINMapsList[0].shape[1]/2) * LengthToPixelRatio)), str(int(self.BINMapsList[0].shape[1] * LengthToPixelRatio))])
                cg1.set_yticks([0,int(self.BINMapsList[0].shape[0]/2), self.BINMapsList[0].shape[0]-1])
                cg1.set_yticklabels([str(int(self.BINMapsList[0].shape[0] * LengthToPixelRatio)), str(int((self.BINMapsList[0].shape[0]/2) * LengthToPixelRatio)), str(0)])
        
        
            # Selecionando os elementos determinados e convertendo os mapas binários (255) 
            # para inteiros sequenciais (1,2,3,4,5,...) em função do número de mapas
            Comb_Img_List = []
            List_of_overlay_found = []
            match_counter = 1
            for element in elementsSelected:
                Comb_Img_List.append((self.BINMapsDic[element] / self.BINMapsDic[element].max()) * match_counter)
                List_of_overlay_found.append(element)
                match_counter += 1
        
               
            # Encontrando as possíveis combinações de elementos na amostra
            Elem_Comb_list = []
            Elem_Comb_Number_list = []
            
            for i in np.arange(1, len(List_of_overlay_found)+1, 1):
                els1 = [list(x) for x in itt.combinations(np.arange(1, len(List_of_overlay_found)+1, 1), i)]
                Elem_Comb_Number_list.append(els1)
                
                els2 = [list(x) for x in itt.combinations(List_of_overlay_found, i)]
                Elem_Comb_list.append(els2)
            
            Elem_Comb_Number_list_flat = [item for sublist in Elem_Comb_Number_list for item in sublist]
            Elem_Comb_list_flat = [item for sublist in Elem_Comb_list for item in sublist]
            
            Elem_Comb_Number_Array = []
            
            # Passando a lista de combinações para arrays
            for j in list(range(len(Elem_Comb_Number_list_flat))):
                Zero_array_line = np.zeros(len(Elem_Comb_Number_list))
                for i in list(range(len(Elem_Comb_Number_list_flat[j]))):
                    Zero_array_line[Elem_Comb_Number_list_flat[j][i]-1] = Elem_Comb_Number_list_flat[j][i]
                
                Elem_Comb_Number_Array.append(Zero_array_line)            
            
            # Convertendo as combinações em um escala quando há 3 entradas       
            if len(Comb_Img_List) == 2:
                Overlay_IMG = np.zeros(Comb_Img_List[0].shape)
                for Yval in list(range(len(Comb_Img_List[0]))):
                    for Xval in list(range(len(Comb_Img_List[0][Yval]))):
                        for comb_value_index in list(range(len(Elem_Comb_Number_Array))):
                            if Comb_Img_List[0][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][0]:
                                if Comb_Img_List[1][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][1]:
                                        Overlay_IMG[Yval, Xval] = (comb_value_index + 1)
                                        
                                
                # Determinando a tick list que será usada no gráfico                            
                tick_list = []
                for i in list(range(len(Elem_Comb_list_flat))):                            
                    if len(Elem_Comb_list_flat[i]) == 1:
                        tick_list.append(Elem_Comb_list_flat[i][0])
                    elif len(Elem_Comb_list_flat[i]) == 2:                 
                        tick_list.append(str(Elem_Comb_list_flat[i][0] + ' + ' + Elem_Comb_list_flat[i][1]))
                
                # verificando a presença de background (= 0)
                if Overlay_IMG.min() == 0:
                    tick_list = ['Background'] + tick_list
        
        
            # Convertendo as combinações em um escala quando há 4 entradas       
            elif len(Comb_Img_List) == 3:
                Overlay_IMG = np.zeros(Comb_Img_List[0].shape)
                for Yval in list(range(len(Comb_Img_List[0]))):
                    for Xval in list(range(len(Comb_Img_List[0][Yval]))):
                        for comb_value_index in list(range(len(Elem_Comb_Number_Array))):
                            if Comb_Img_List[0][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][0]:
                                if Comb_Img_List[1][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][1]:
                                    if Comb_Img_List[2][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][2]:
                                        Overlay_IMG[Yval, Xval] = (comb_value_index + 1)
                                        
                                
                # Determinando a tick list que será usada no gráfico                            
                tick_list = []
                for i in list(range(len(Elem_Comb_list_flat))):                            
                    if len(Elem_Comb_list_flat[i]) == 1:
                        tick_list.append(Elem_Comb_list_flat[i][0])
                    elif len(Elem_Comb_list_flat[i]) == 2:                 
                        tick_list.append(str(Elem_Comb_list_flat[i][0] + ' + ' + Elem_Comb_list_flat[i][1]))
                    elif len(Elem_Comb_list_flat[i]) == 3:
                        tick_list.append(str(Elem_Comb_list_flat[i][0] + ' + ' + Elem_Comb_list_flat[i][1] + ' + ' + Elem_Comb_list_flat[i][2]))
                
                # verificando a presença de background (= 0)
                if Overlay_IMG.min() == 0:
                    tick_list = ['Background'] + tick_list            
        
            # Convertendo as combinações em um escala quando há 5 entradas       
            elif len(Comb_Img_List) == 4:
                Overlay_IMG = np.zeros(Comb_Img_List[0].shape)
                for Yval in list(range(len(Comb_Img_List[0]))):
                    for Xval in list(range(len(Comb_Img_List[0][Yval]))):
                        for comb_value_index in list(range(len(Elem_Comb_Number_Array))):
                            if Comb_Img_List[0][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][0]:
                                if Comb_Img_List[1][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][1]:
                                    if Comb_Img_List[2][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][2]:
                                        if Comb_Img_List[3][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][3]:
                                            Overlay_IMG[Yval, Xval] = (comb_value_index + 1)
                                        
                                
                # Determinando a tick list que será usada no gráfico                            
                tick_list = []
                for i in list(range(len(Elem_Comb_list_flat))):                            
                    if len(Elem_Comb_list_flat[i]) == 1:
                        tick_list.append(Elem_Comb_list_flat[i][0])
                    elif len(Elem_Comb_list_flat[i]) == 2:                 
                        tick_list.append(str(Elem_Comb_list_flat[i][0] + ' + ' + Elem_Comb_list_flat[i][1]))
                    elif len(Elem_Comb_list_flat[i]) == 3:
                        tick_list.append(str(Elem_Comb_list_flat[i][0] + ' + ' + Elem_Comb_list_flat[i][1] + ' + ' + Elem_Comb_list_flat[i][2]))
                    elif len(Elem_Comb_list_flat[i]) == 4:
                        tick_list.append(str(Elem_Comb_list_flat[i][0] + ' + ' + Elem_Comb_list_flat[i][1] + ' + ' + Elem_Comb_list_flat[i][2] + ' + ' + Elem_Comb_list_flat[i][3]))
                
        
                # verificando a presença de background (= 0)
                if Overlay_IMG.min() == 0:
                    tick_list = ['Background'] + tick_list 
        
        
            cg2Axes = cg1.imshow(Overlay_IMG, cmap=self.getDiscrete_cmap(Overlay_IMG.max()+1, 'rainbow'))
        
            deltaTick = ((Overlay_IMG.max() - Overlay_IMG.min()) / (len(Elem_Comb_list_flat) + 1))
            Colbar2=fig2.colorbar(cg2Axes, fraction=0.04, 
                              pad=0.08, orientation='vertical',
                              ticks=list(np.arange(Overlay_IMG.min() + (deltaTick/2), Overlay_IMG.max()+1+(deltaTick/2), deltaTick)))
        
            Colbar2.set_label('Elements', fontsize=14)
            Colbar2.set_ticklabels(tick_list)
            Colbar2.ax.tick_params(labelsize=11)
            
            plt.tight_layout()                    
            fileNumber = Export.getFileNumber(self.folder, self.SampleName, 'ElementOverLay', self.formato)
            fig2.savefig(self.folder + '/' + self.SampleName + '/' + 'ElementOverLay' + fileNumber + '.' + self.formato, dpi = 400)
            
            plt.show()   
            print('Saindo do módulo ElementColorOverlay...')
            return
        
        else:
            Erros.Errors.simpleError()
            print('Para rodar esse módulo, você precisa selecionar de 2 a 4 elemetos de todos os importados.')
            print('Encerrando o módulo...')
            return
        
        
        
        
        
    # Encontrando a sobreposição de compostos
    def CompoundColorOverlay(self, LengthToPixelRatio = False):

        #Abaixo se introduz os elementos que serão plotados em ColorOverlay        
        #----------------------------------------------------------------------------------------------------------------------------

        print(separator)
        print('Entrando no módulo FindCompoundOverlap...')
        print('Nesse módulo você pode selecionar combinações de elementos para plotar as sobreposições de possíveis compostos.')
        print('Você pode selecionar de 2 ou 3 combinações de elementos.')
        print('Inserir a combinação dos elementos com hífen entre eles (Ex: *Al-Fe*, *Mg-O*)')
        print('(Após inserir todos os elementos desejados, digite *continuar*)')
        
        ListOfElementsSelected=[]
        while True:
            print(separator)
            print('Elementos importados:')                            
            for element in self.elementsImported:
                print(element)
            print(separator)  
            if len(ListOfElementsSelected) > 0:
                print('Combinações de elementos selecionadas para plotagem:')                            
                for comb in sorted(ListOfElementsSelected):
                    print(comb)
            print(separator) 
            print('Selecione uma combinação de elementos para plotar sobreposições:')
            print('Pelo menos duas combinações devem ser inseridas.')
            print('(Após inserir todas as combinações desejadas, digite *continuar*)')
            elementsCombToPlot = str(input())
            if elementsCombToPlot[1:2] == '-':
                if elementsCombToPlot[:1] in self.elementsImported and elementsCombToPlot[2:] in self.elementsImported:
                    if elementsCombToPlot not in ListOfElementsSelected:
                        ListOfElementsSelected.append(sorted([elementsCombToPlot[:1], elementsCombToPlot[2:]]))
                        ListOfElementsSelected.sort()
                                            
                    else:                    
                        Erros.Errors.simpleError()
                        print('Inserir uma combinação elementos que ainda foi selecionada.')
                        print('(Inserir a combinação dos elementos com hífen entre eles (Ex: *Al-Fe*, *Mg-O*))')
                
                else:
                    Erros.Errors.wrongInput()
                    print('Inserir uma combinação elementos que foram importados.')
                    print('(Inserir a combinação dos elementos com hífen entre eles (Ex: *Al-Fe*, *Mg-O*))')
                    continue
            
            elif elementsCombToPlot[2:3] == '-':
                if elementsCombToPlot[:2] in self.elementsImported and elementsCombToPlot[3:] in self.elementsImported:                           
                    if elementsCombToPlot not in ListOfElementsSelected:
                        ListOfElementsSelected.append(sorted([elementsCombToPlot[:2], elementsCombToPlot[3:]]))
                        ListOfElementsSelected.sort()
                                            
                    else:                    
                        Erros.Errors.simpleError()
                        print('Inserir uma combinação elementos que ainda foi selecionada.')
                        print('(Inserir a combinação dos elementos com hífen entre eles (Ex: *Al-Fe*, *Mg-O*))')
                
                else:
                    Erros.Errors.wrongInput()
                    print('Inserir uma combinação elementos que foram importados.')
                    print('(Inserir a combinação dos elementos com hífen entre eles (Ex: *Al-Fe*, *Mg-O*))')
                    continue
                    
            elif elementsCombToPlot.lower() == 'continuar':
                if len(ListOfElementsSelected) >= 2:
                    break
                
                else:
                    Erros.Errors.wrongInput()
                    print('Para usar esse módulo você precisa importar de 2 a 3 combinações de mapas.')
                    continue

            elif elementsCombToPlot.lower() == 'sair':                        
                quit()

            elif elementsCombToPlot.lower() == 'help':
                helpMods()
            
            else:
                Erros.Errors.wrongInput()
                print('Inserir uma combinação elementos que foram importados.')
                print('(Inserir a combinação dos elementos com hífen entre eles (Ex: *Al-Fe*, *Mg-O*))')
                continue

        if self.overMapList == 0:
            self.overMapList = self.getElementsOverlapMaps()
        
        Comb_Img_List = []
        List_of_overlay_found = []
        match_counter = 1
        for combination in ListOfElementsSelected:
            for list_number in list(range(len(self.overMapList))):
                if combination[0] in self.overMapList[list_number][1:] and combination[1] in self.overMapList[list_number][1:]:                                        
                    Comb_Img_List.append((self.overMapList[list_number][0] / self.overMapList[list_number][0].max()) * match_counter)
                    List_of_overlay_found.append([combination[0] + '-' + combination[1]])
                    match_counter += 1
        
        #----------------------------------------------------------------------------------------------------------------------------
        print('Plotando os mapas com os elementos selecionados...')
        if 2 <= len(Comb_Img_List) <= 3:    
            fig3=plt.figure(figsize=(6, 6),facecolor='w', edgecolor='k')
            cg3=plt.subplot2grid((1,1),(0,0), rowspan=1, colspan=1)
            cg3.set_title('Color Overlay', fontsize=14)

            if LengthToPixelRatio == False:
                cg3.tick_params(axis="y", labelleft=False, left=False, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
                cg3.tick_params(axis="x", labelbottom=False, bottom=False, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)

            elif LengthToPixelRatio != False:
                cg3.set_xlabel('$\mu$m', labelpad=5, fontsize=14)
                cg3.set_ylabel('$\mu$m', labelpad=5, fontsize=14)
            
                cg3.set_xticks([0, int(self.overMapList[0][0].shape[1]/2), self.overMapList[0][0].shape[1]-1])
                cg3.set_xticklabels([str(0), str(int((self.overMapList[0][0].shape[1]/2) * LengthToPixelRatio)), str(int(self.overMapList[0][0].shape[1] * LengthToPixelRatio))])
                cg3.set_yticks([0,int(self.overMapList[0][0].shape[0]/2), self.overMapList[0][0].shape[0]-1])
                cg3.set_yticklabels([str(int(self.overMapList[0][0].shape[0] * LengthToPixelRatio)), str(int((self.overMapList[0][0].shape[0]/2) * LengthToPixelRatio)), str(0)])
            
            # Encontrando as possíveis combinações de compostos na amostra
            Elem_Comb_list = []
            Elem_Comb_Number_list = []
            
            for i in np.arange(1, len(List_of_overlay_found)+1, 1):
                els1 = [list(x) for x in itt.combinations(np.arange(1, len(List_of_overlay_found)+1, 1), i)]
                Elem_Comb_Number_list.append(els1)
                
                els2 = [list(x) for x in itt.combinations(List_of_overlay_found, i)]
                Elem_Comb_list.append(els2)
            
            Elem_Comb_Number_list_flat = [item for sublist in Elem_Comb_Number_list for item in sublist]
            Elem_Comb_list_flat = [item for sublist in Elem_Comb_list for item in sublist]
            
            Elem_Comb_Number_Array = []
        
            # Passando a lista de combinações para arrays
            for j in list(range(len(Elem_Comb_Number_list_flat))):
                Zero_array_line = np.zeros(len(Elem_Comb_Number_list))
                for i in list(range(len(Elem_Comb_Number_list_flat[j]))):
                    Zero_array_line[Elem_Comb_Number_list_flat[j][i]-1] = Elem_Comb_Number_list_flat[j][i]
                
                Elem_Comb_Number_Array.append(Zero_array_line)            
            
            # Convertendo as combinações em um escala quando há 3 entradas       
            if len(Comb_Img_List) == 2:
                Overlay_IMG = np.zeros(Comb_Img_List[0].shape)
                for Yval in list(range(len(Comb_Img_List[0]))):
                    for Xval in list(range(len(Comb_Img_List[0][Yval]))):
                        for comb_value_index in list(range(len(Elem_Comb_Number_Array))):
                            if Comb_Img_List[0][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][0]:
                                if Comb_Img_List[1][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][1]:
                                        Overlay_IMG[Yval, Xval] = (comb_value_index + 1)
                                        
                                
                # Determinando a tick list que será usada no gráfico                            
                tick_list = []
                for i in list(range(len(Elem_Comb_list_flat))):                            
                    if len(Elem_Comb_list_flat[i]) == 1:
                        tick_list.append(Elem_Comb_list_flat[i][0][0])
                    elif len(Elem_Comb_list_flat[i]) == 2:                 
                        tick_list.append(str(Elem_Comb_list_flat[i][0][0] + ' + ' + Elem_Comb_list_flat[i][1][0]))
                
                # verificando a presença de background (= 0)
                if Overlay_IMG.min() == 0:
                    tick_list = ['Background'] + tick_list
        
        
            # Convertendo as combinações em um escala quando há 3 entradas       
            elif len(Comb_Img_List) == 3:
                Overlay_IMG = np.zeros(Comb_Img_List[0].shape)
                for Yval in list(range(len(Comb_Img_List[0]))):
                    for Xval in list(range(len(Comb_Img_List[0][Yval]))):
                        for comb_value_index in list(range(len(Elem_Comb_Number_Array))):
                            if Comb_Img_List[0][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][0]:
                                if Comb_Img_List[1][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][1]:
                                    if Comb_Img_List[2][Yval, Xval] == Elem_Comb_Number_Array[comb_value_index][2]:
                                        Overlay_IMG[Yval, Xval] = (comb_value_index + 1)
                                        
                                
                # Determinando a tick list que será usada no gráfico                            
                tick_list = []
                for i in list(range(len(Elem_Comb_list_flat))):                            
                    if len(Elem_Comb_list_flat[i]) == 1:
                        tick_list.append(Elem_Comb_list_flat[i][0][0])
                    elif len(Elem_Comb_list_flat[i]) == 2:                 
                        tick_list.append(str(Elem_Comb_list_flat[i][0][0] + ' + ' + Elem_Comb_list_flat[i][1][0]))
                    elif len(Elem_Comb_list_flat[i]) == 3:
                        tick_list.append(str(Elem_Comb_list_flat[i][0][0] + ' + ' + Elem_Comb_list_flat[i][1][0] + ' + ' + Elem_Comb_list_flat[i][2][0]))
                
                # verificando a presença de background (= 0)
                if Overlay_IMG.min() == 0:
                    tick_list = ['Background'] + tick_list                
        
            cg3Axes = cg3.imshow(Overlay_IMG, cmap=self.getDiscrete_cmap(Overlay_IMG.max()+1, 'rainbow'))
        
            deltaTick = ((Overlay_IMG.max() - Overlay_IMG.min()) / (len(Elem_Comb_list_flat) + 1))
            Colbar3=fig3.colorbar(cg3Axes, fraction=0.04, 
                              pad=0.08, orientation='vertical',
                              ticks=list(np.arange(Overlay_IMG.min() + (deltaTick/2), Overlay_IMG.max()+1+(deltaTick/2), deltaTick)))
        
            Colbar3.set_label('Compounds', fontsize=14)
            Colbar3.set_ticklabels(tick_list)
            Colbar3.ax.tick_params(labelsize=11)
            
            plt.tight_layout()        
            fileNumber = Export.getFileNumber(self.folder, self.SampleName, 'CompoundOverLay', self.formato)
            fig3.savefig(self.folder + '/' + self.SampleName + '/' + 'CompoundOverLay' + fileNumber + '.' + self.formato, dpi = 400)
                  
            plt.show()
            print('Saindo do módulo FindCompoundOverlap...')
            return
       
        
    # Encontrando a distribuição do tamanho de partículas
    def FindPartDist(self, LengthToPixelRatio):
        
        from skimage import measure
        from matplotlib import patches
        from skimage import segmentation
        
        print(separator)
        print('Entrando no módulo Particle Distribution...')
        print('Encontrando os tamanhos de partículas...')

        imgPropsDic = {}
        for imgN in range(len(self.BINMapsList)):
            clearedImg = segmentation.clear_border(self.BINMapsList[imgN])
            labImg = measure.label(clearedImg, connectivity=1)
            imgProps = measure.regionprops(labImg)                        
            
            if len(imgProps) > 50:
                imgPropsDic[self.elementsImported[imgN]] = imgProps
                continue
                
            else:
                Erros.Errors.simpleError()
                print('Foram encontradas menos que 50 partículas para o mapa:')
                print(self.elementsImported[imgN])
                print('Ignorando esse a distribuição para esse mapa.')
                continue
                
        PDistElemList = sorted(imgPropsDic.keys())
        
        if len(PDistElemList) == 1:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((1,1),(0,0),rowspan=1,colspan=1)
            
        elif len(PDistElemList) == 2:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((1,2),(0,0),rowspan=1,colspan=1)
            g2=plt.subplot2grid((1,2),(0,1),rowspan=1,colspan=1)
            
        elif 2 < len(PDistElemList) <= 4:
            fig1=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,2),(0,0),rowspan=1,colspan=1)
            g2=plt.subplot2grid((2,2),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,2),(1,0),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,2),(1,1),rowspan=1,colspan=1)
    
        elif 4 < len(PDistElemList) <= 6:
            fig1=plt.figure(figsize=(10, 8),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,3),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,3),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,3),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,3),(1,0),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,3),(1,1),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,3),(1,2),rowspan=1,colspan=1)
        
        elif 6 < len(PDistElemList) <= 8:
            fig1=plt.figure(figsize=(12, 8),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,4),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,4),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,4),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,4),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,4),(1,0),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,4),(1,1),rowspan=1,colspan=1)
            g7=plt.subplot2grid((2,4),(1,2),rowspan=1,colspan=1)
            g8=plt.subplot2grid((2,4),(1,3),rowspan=1,colspan=1)
            
        elif 8 < len(PDistElemList) <= 10:
            fig1=plt.figure(figsize=(14, 7),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((2,5),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((2,5),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((2,5),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((2,5),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((2,5),(0,4),rowspan=1,colspan=1)
            g6=plt.subplot2grid((2,5),(1,0),rowspan=1,colspan=1)
            g7=plt.subplot2grid((2,5),(1,1),rowspan=1,colspan=1)
            g8=plt.subplot2grid((2,5),(1,2),rowspan=1,colspan=1)
            g9=plt.subplot2grid((2,5),(1,3),rowspan=1,colspan=1)
            g10=plt.subplot2grid((2,5),(1,4),rowspan=1,colspan=1)
    
        elif 10 < len(PDistElemList) <= 12:
            fig1=plt.figure(figsize=(14, 16),facecolor='w', edgecolor='k')
            g1=plt.subplot2grid((3,4),(0,0),rowspan=1,colspan=1)        
            g2=plt.subplot2grid((3,4),(0,1),rowspan=1,colspan=1)
            g3=plt.subplot2grid((3,4),(0,2),rowspan=1,colspan=1)
            g4=plt.subplot2grid((3,4),(0,3),rowspan=1,colspan=1)
            g5=plt.subplot2grid((3,4),(1,0),rowspan=1,colspan=1)
            g6=plt.subplot2grid((3,4),(1,1),rowspan=1,colspan=1)
            g7=plt.subplot2grid((3,4),(1,2),rowspan=1,colspan=1)
            g8=plt.subplot2grid((3,4),(1,3),rowspan=1,colspan=1)
            g9=plt.subplot2grid((3,4),(2,0),rowspan=1,colspan=1)
            g10=plt.subplot2grid((3,4),(2,1),rowspan=1,colspan=1)
            g11=plt.subplot2grid((3,4),(2,2),rowspan=1,colspan=1)
            g12=plt.subplot2grid((3,4),(2,3),rowspan=1,colspan=1)
       
        plt.subplots_adjust(wspace=1, hspace=1)        
        
        if len(PDistElemList) >= 1:
            print('Plotando os mapas com as partículas identificadas...')
            for elementN in range(len(PDistElemList)):
                
                eval('g' + str(elementN + 1)).set_title('Tracked Map ' + PDistElemList[elementN], fontsize=14)
                eval('g' + str(elementN + 1)).set_ylabel('$\mu$m', labelpad=5, fontsize=14)
                eval('g' + str(elementN + 1)).set_xlabel('$\mu$m', labelpad=5, fontsize=14)
                eval('g' + str(elementN + 1)).tick_params(axis="y", labelleft=True, left=True, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
                eval('g' + str(elementN + 1)).tick_params(axis="x", labelbottom=True, bottom=True, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)                
                eval('g' + str(elementN + 1)).set_xticks([0, int(self.BINMapsDic[PDistElemList[elementN]].shape[1]/2), self.BINMapsDic[PDistElemList[elementN]].shape[1]-1])
                eval('g' + str(elementN + 1)).set_xticklabels([str(0), str(int((self.BINMapsDic[PDistElemList[elementN]].shape[1]/2) * LengthToPixelRatio)), str(int(self.BINMapsDic[PDistElemList[elementN]].shape[1] * LengthToPixelRatio))])
                eval('g' + str(elementN + 1)).set_yticks([0,int(self.BINMapsDic[PDistElemList[elementN]].shape[0]/2), self.BINMapsDic[PDistElemList[elementN]].shape[0]-1])
                eval('g' + str(elementN + 1)).set_yticklabels([str(int(self.BINMapsDic[PDistElemList[elementN]].shape[0] * LengthToPixelRatio)), str(int((self.BINMapsDic[PDistElemList[elementN]].shape[0]/2) * LengthToPixelRatio)), str(0)])
                eval('g' + str(elementN + 1)).imshow(self.BINMapsDic[PDistElemList[elementN]], alpha=0.8, cmap='Blues')
                
                for region in imgPropsDic[PDistElemList[elementN]]:
                    if ((self.BINMapsDic[PDistElemList[elementN]].shape[0] * self.BINMapsDic[PDistElemList[elementN]].shape[1]) * 0.3) >= region.area >= 10:
                        minr, minc, maxr, maxc = region.bbox
                        rect = patches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=0.5)
                        eval('g' + str(elementN + 1)).add_patch(rect)
                        
            plt.tight_layout()            
            fileNumber = Export.getFileNumber(self.folder, self.SampleName, 'TrackedPart', self.formato)
            fig1.savefig(self.folder + '/' + self.SampleName + '/' + 'TrackedPart' + fileNumber + '.' + self.formato, dpi = 400)


        if len(PDistElemList) == 1:
            fig2=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            f1=plt.subplot2grid((1,1),(0,0),rowspan=1,colspan=1)
            
        elif len(PDistElemList) == 2:
            fig2=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            f1=plt.subplot2grid((1,2),(0,0),rowspan=1,colspan=1)
            f2=plt.subplot2grid((1,2),(0,1),rowspan=1,colspan=1)
            
        elif 2 < len(PDistElemList) <= 4:
            fig2=plt.figure(figsize=(10, 10),facecolor='w', edgecolor='k')
            f1=plt.subplot2grid((2,2),(0,0),rowspan=1,colspan=1)
            f2=plt.subplot2grid((2,2),(0,1),rowspan=1,colspan=1)
            f3=plt.subplot2grid((2,2),(1,0),rowspan=1,colspan=1)
            f4=plt.subplot2grid((2,2),(1,1),rowspan=1,colspan=1)
    
        elif 4 < len(PDistElemList) <= 6:
            fig2=plt.figure(figsize=(10, 8),facecolor='w', edgecolor='k')
            f1=plt.subplot2grid((2,3),(0,0),rowspan=1,colspan=1)        
            f2=plt.subplot2grid((2,3),(0,1),rowspan=1,colspan=1)
            f3=plt.subplot2grid((2,3),(0,2),rowspan=1,colspan=1)
            f4=plt.subplot2grid((2,3),(1,0),rowspan=1,colspan=1)
            f5=plt.subplot2grid((2,3),(1,1),rowspan=1,colspan=1)
            f6=plt.subplot2grid((2,3),(1,2),rowspan=1,colspan=1)
        
        elif 6 < len(PDistElemList) <= 8:
            fig2=plt.figure(figsize=(12, 8),facecolor='w', edgecolor='k')
            f1=plt.subplot2grid((2,4),(0,0),rowspan=1,colspan=1)        
            f2=plt.subplot2grid((2,4),(0,1),rowspan=1,colspan=1)
            f3=plt.subplot2grid((2,4),(0,2),rowspan=1,colspan=1)
            f4=plt.subplot2grid((2,4),(0,3),rowspan=1,colspan=1)
            f5=plt.subplot2grid((2,4),(1,0),rowspan=1,colspan=1)
            f6=plt.subplot2grid((2,4),(1,1),rowspan=1,colspan=1)
            f7=plt.subplot2grid((2,4),(1,2),rowspan=1,colspan=1)
            f8=plt.subplot2grid((2,4),(1,3),rowspan=1,colspan=1)
            
        elif 8 < len(PDistElemList) <= 10:
            fig2=plt.figure(figsize=(14, 7),facecolor='w', edgecolor='k')
            f1=plt.subplot2grid((2,5),(0,0),rowspan=1,colspan=1)        
            f2=plt.subplot2grid((2,5),(0,1),rowspan=1,colspan=1)
            f3=plt.subplot2grid((2,5),(0,2),rowspan=1,colspan=1)
            f4=plt.subplot2grid((2,5),(0,3),rowspan=1,colspan=1)
            f5=plt.subplot2grid((2,5),(0,4),rowspan=1,colspan=1)
            f6=plt.subplot2grid((2,5),(1,0),rowspan=1,colspan=1)
            f7=plt.subplot2grid((2,5),(1,1),rowspan=1,colspan=1)
            f8=plt.subplot2grid((2,5),(1,2),rowspan=1,colspan=1)
            f9=plt.subplot2grid((2,5),(1,3),rowspan=1,colspan=1)
            f10=plt.subplot2grid((2,5),(1,4),rowspan=1,colspan=1)
    
        elif 10 < len(PDistElemList) <= 12:
            fig2=plt.figure(figsize=(14, 16),facecolor='w', edgecolor='k')
            f1=plt.subplot2grid((3,4),(0,0),rowspan=1,colspan=1)        
            f2=plt.subplot2grid((3,4),(0,1),rowspan=1,colspan=1)
            f3=plt.subplot2grid((3,4),(0,2),rowspan=1,colspan=1)
            f4=plt.subplot2grid((3,4),(0,3),rowspan=1,colspan=1)
            f5=plt.subplot2grid((3,4),(1,0),rowspan=1,colspan=1)
            f6=plt.subplot2grid((3,4),(1,1),rowspan=1,colspan=1)
            f7=plt.subplot2grid((3,4),(1,2),rowspan=1,colspan=1)
            f8=plt.subplot2grid((3,4),(1,3),rowspan=1,colspan=1)
            f9=plt.subplot2grid((3,4),(2,0),rowspan=1,colspan=1)
            f10=plt.subplot2grid((3,4),(2,1),rowspan=1,colspan=1)
            f11=plt.subplot2grid((3,4),(2,2),rowspan=1,colspan=1)
            f12=plt.subplot2grid((3,4),(2,3),rowspan=1,colspan=1)
       
        plt.subplots_adjust(wspace=1, hspace=1)  


        if len(PDistElemList) >= 1:                     
            print('Plotando as distribuições com os tamanhos das partículas identificadas...')
            for elementN in range(len(PDistElemList)):                
                PartSizeList = []
                for region in imgPropsDic[PDistElemList[elementN]]:
                    if ((self.BINMapsDic[PDistElemList[elementN]].shape[0] * self.BINMapsDic[PDistElemList[elementN]].shape[1]) * 0.3) >= region.area >= 10:
                        PartSize = region.equivalent_diameter
                        PartSizeList.append(PartSize)
                
                eval('f' + str(elementN + 1)).set_title('Particle Distribution: ' + PDistElemList[elementN], fontsize=14)
                eval('f' + str(elementN + 1)).set_ylabel('Frequency', labelpad=5, fontsize=14)
                eval('f' + str(elementN + 1)).set_xlabel('$\mu$m', labelpad=5, fontsize=14)
                eval('f' + str(elementN + 1)).tick_params(axis="y", labelleft=True, left=True, labelright=False, right=False, colors='k', width=1.5, length=3.5, labelsize=11)
                eval('f' + str(elementN + 1)).tick_params(axis="x", labelbottom=True, bottom=True, labeltop=False, top=False, colors='k', width=1.5,length=3.5, labelsize=11)            
                eval('f' + str(elementN + 1)).hist(PartSizeList, bins=20)
                   
            plt.tight_layout()            
            fileNumber = Export.getFileNumber(self.folder, self.SampleName, 'PartDistribution', self.formato)
            fig2.savefig(self.folder + '/' + self.SampleName + '/' + 'PartDistribution' + fileNumber + '.' + self.formato, dpi = 400)
    
            plt.show()
        
        print('Saindo do módulo FindParticleDistribution...')                       