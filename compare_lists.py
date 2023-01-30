def compareLists(cel_1, cel_2):

    comp_list=[]
        
    for index1 in range(0, len(cel_1)):
    
        for index2 in range(0, len(cel_2)):

            if cel_1[index1][1] == cel_2[index2][1]:

                if cel_1[index1][2] > cel_2[index2][2]:
                    creation_date = 'Celular 1'
                else:
                    creation_date = 'Celular 2'

                lista = [cel_1[index1][0],cel_1[index1][1],cel_2[index2][0],creation_date]
                comp_list.append(lista)     #lista com contatos com números idênticos (contato cel1, telefone, contato cel2) 
    
    with open('C:\\Temp\\scan-android-device\\compared_list.txt', 'w') as f: 
      f.write(str(comp_list))

    return comp_list
    