# Python program to explain shutil.copytree() method
	
# importing os module
import os

# importing shutil module
import shutil

from datetime import date


# path
path = 'C:/Users/47889004/Documents/teste'

#define a data de hoje
today = date.today()
today_str = str(today)

# Source path
src = 'W:/ATIVOS DE T.I'

#Source list
src_list = ('W:/ATIVOS DE T.I','W:/SOLICITACOES DE ACESSO REMOTO')
sl = src_list


#destination list end - cria lista com o nome das pastas iteradas da pasta src para ser utilizada para criação do nome de destino
dest_list_end=[]
for pasta in src_list:
#    print (pasta)
    print (pasta.strip('W:/'))
    dest_list_end.append(pasta.strip('W:/'))
dest_list_end 

# Destination path using today's timestamp
dest = path+'/'+today_str

def Backup(src,dest):
    # Copy the content of
    # source to destination
    shutil.copytree(src, dest)

# Itera pelas pastas da lista de fontes e chama a função de Backup
for pasta in src_list:
    print (pasta)
    #define o destino adicionando dest_end depois do timestamp
    

# List files and directories
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'
print("Before copying file:")
print(os.listdir(path))




# List files and directories
# in "C:/Users / Rajnish / Desktop / GeeksforGeeks"
print("After copying file:")
print(os.listdir(path))

# Print path of newly
# created file
print("Destination path:", destination)
