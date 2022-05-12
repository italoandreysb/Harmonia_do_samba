import os
# inicializando a variável
acao = 0
#Cabeçalho
print('SSSSSSSS  AAAAAAAA  MMM   MMM  BBBBBBB   AAAAAAAA \n' 
      'SS        AA    AA  MM M M MM  BB   BBB  AA    AA \n'
      'SSSSSSSS  AAAAAAAA  MM MMM MM  BBBBBBBB  AAAAAAAA \n'
      '      SS  AA    AA  MM  M  MM  BB   BBB  AA    AA \n'
      'SSSSSSSS  AA    AA  MM     MM  BBBBBBB   AA    AA \n'
      'D E V E L O P E D - B Y - I T A L O - A N D R E Y \n')
#Menu
print('1. Atualizar as Bibliotecas \n'
      '2. verificar status do SAMBA \n'
      '3. Instalar SAMBA \n'
      '4. Desinstalar SAMBA \n')
try:
    acao = int(input('O que deseja fazer? \n (1, 2, 3 ou 4) \n'))
except (ValueError, TypeError, NameError):
    print('Erro, Por favor digite um número entre de 1 e 4')

"""Atualizando Bibliotecas"""
if acao == 1: 
    print('Atualizando bibliotecas...')
    os.system('sudo apt update')
    print('Bibliotecas atualizadas')

"""Verificando status do SAMBA"""
elif acao == 2: 
    print('Verificnado status do SAMBA...')
    os.system('systemctl status smbd.service')
      
"""Instalando o SAMBA"""
elif acao == 3:
    print('instalando SAMBA...')
    os.system('sudo apt install samba')
    os.system('y')
    os.system('cp auto_samba /etc/samba/') #Copiando arquivo de configuração primária
    os.system('sudo mkdir -p /srv/samba/share') #Criando diretório
    os.system('sudo chown nobody:nogroup /srv/samba/share/')#Declarando as permissões
    os.system('sudo systemctl restart smbd.service nmbd.service') #reiniciando o serviço
    print('Samba instalado \n Diretórios criados \n Permissões ajustadas ')
      
"""Desinstalando samba"""
elif acao == 4:
    desinstalando = str(input('Tem certeza que deseja desinstalar o SAMBA? \n Digite Sim ou Nao \n'))
    if desinstalando.lower() == 'sim':
        print('Parando serviço SAMBA...')
        os.system('systemctl stop smbd.service')
        print('Desinstalando SAMBA...')
        os.system('sudo apt remove samba')
        os.system('rm /srv/samba')  #removendo diretório #Removendo diretório
    else:
        print('Desinstalação cancelada')
if acao >= 5:
    print('Favor inserir um número menor que 5')
else:
    print('Operação finalizada')
