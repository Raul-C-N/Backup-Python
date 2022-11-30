# Python program to explain shutil.copytree() method
	
# importing os module
import os

# importing shutil module
import shutil

from datetime import date


# path
path = 'D:/Backup -DTC'

#define a data de hoje
today = date.today()
today_str = str(today)

# Source path
src = 'W:/ATIVOS DE T.I'


#Source list
src_list = ('//10.75.37.2/dtc/ATIVOS DE T.I','//10.75.37.2/dtc/SOLICITACOES DE ACESSO REMOTO','//10.75.37.2/47889004')
sl = src_list


#destination list end - cria lista com o nome das pastas iteradas da pasta src para ser utilizada para criação do nome de destino
dest_list_end=[]

for pasta in src_list:
    print (pasta)
    print (pasta.strip('W:/'))
    dest_list_end.append(pasta.strip('W:/'))
#dest_list_end 

# Destination path using today's timestamp
dest_temp = path+'/'+today_str

# Destination list
dest_list = []

# Cria a lista de destinos final contendo o timestamp e o nome da pasta que foi copiada
for item in range(len(src_list)):
    print (dest_temp+'/'+dest_list_end[item])
    dest_list.append(dest_temp+'/'+dest_list_end[item])
#dest_list


def Backup(src,dest): 
    # List files and directories
    # in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'
    print("Before copying file:")
    print(os.listdir(path))

    # Copy the content of
    # source to destination
    destination = shutil.copytree(src, dest)

    # List files and directories
    # in "C:/Users / Rajnish / Desktop / GeeksforGeeks"
    print("After copying file:")
    print(os.listdir(path))

    # Print path of newly
    # created file
    print("Destination path:", destination)

#Main
# Itera pelas pastas da lista de fontes (src) e chama a função de Backup para cada uma
for i in  range(len(src_list)):
    print (src_list[i]) #fonte
    print (dest_list[i]) #destino
    Backup(src_list[i],dest_list[i])

    
    




