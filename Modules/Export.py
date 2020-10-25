'''Funções para exportar imagens'''
import os

def getFileNumber(folder, SampleName, ImageName, formato):
    FileList = os.listdir(folder + '/' + SampleName)
    fileNumber = 1
    for fileName in FileList:
        if fileName[:len(ImageName)] == ImageName:
            if fileName[-len(formato):] == formato:
                try:
                    if fileNumber <= int(fileName[len(ImageName):-len(formato)-1]):
                        fileNumber = int(fileName[len(ImageName):-len(formato)-1]) + 1
                except ValueError:
                    continue
    return str(fileNumber)
            
        