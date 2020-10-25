
class helpMods(object):
    '''Apresenta os módulos a serem escolhidos após a importação das imagens'''
    
    def __init__(self):
        
        print('\n-------------------------------------------------')
        print('Acessando o módulo Help...')
        print('\nMódulos disponíveis para processamento dos mapas:')

        print('')
        print('*PlotPanel*')
        print('Plota todos os mapas importados em um painel.')

        print('')
        print('*FindAutoOverlap*')
        print('Encontra sobreposições (Overlaps) de `elementos` nos mapas de EDS.')
        print('Encontra e plota automaticamente todos as sobreposições dos elementos importados.')
        print('A sobreposição é encontrada dois a dois.')
        print('Ex: Al-O, Mg-O, Si-O')
        print('(Esse modo faz uso de imagens binarizadas)')

        print('')
        print('*FindElementOverlap*')
        print('Encontra sobreposições (Overlaps) de `elementos` nos mapas de EDS.')
        print('Dentre os elementos importados, selecione os elementos cuja sobreposição você deseja plotar.')
        print('(Esse modo faz uso de imagens binarizadas)')

        print('') 
        print('*FindCompoundOverlap*')
        print('Encontra sobreposições de possíveis `compostos` nos mapas de EDS.')
        print('Dentre os elementos importados, selecione associações de elementos para encontrar as sobreposições de compostos.')        
        print('(Esse modo faz uso de imagens binarizadas)')

        print('')
        print('*FindParticleDistribution*')
        print('Plota a distribuição de partículas presente na amostra')        
        print('(Esse modo faz uso de imagens binarizadas)')
            
        print('')
        print('*FindPorosity*')
        print('Revela os poros da amostra considerando as regiões onde não há signal')        
        print('(Esse modo faz uso de imagens binarizadas)')
        print('ATENÇÃO: Para cálculo preciso da porosidade, assegurar que todos os elementos encontrados na amostra sejam importados para processamento')
        print('-------------------------------------------------\n')
