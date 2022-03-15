# Harmonia_do_samba
Automação de instalação e configuração básica do SAMBA com Pyhton

1. Acesse o servidor via SSH, utlizando o Putty ou xshell

2. Instale o Python e o Vim (ou outro de sua preferência):

```sudo apt install python3```
```sudo apt install vim```

3. Crie e abra o arquivo python:

```$ vim harmonia_do_samba.py```

4. Digite ou copie o código abaixo para o arquivo criado:

```python
# Harmonia do samba v.2.2
import os
acao = 0# inicializando a variável

print('SSSSSSSS  AAAAAAAA  MMM   MMM  BBBBBBB   AAAAAAAA \n' #Cabeçalho
      'SS        AA    AA  MM M M MM  BB   BBB  AA    AA \n'
      'SSSSSSSS  AAAAAAAA  MM MMM MM  BBBBBBBB  AAAAAAAA \n'
      '      SS  AA    AA  MM  M  MM  BB   BBB  AA    AA \n'
      'SSSSSSSS  AA    AA  MM     MM  BBBBBBB   AA    AA \n'
      'D E V E L O P E D - B Y - I T A L O - A N D R E Y \n')

print('1. Atualizar as Bibliotecas \n' #Menu
      '2. verificar status do SAMBA \n'
      '3. Instalar SAMBA \n'
      '4. Desinstalar SAMBA \n')
try:
    acao = int(input('O que deseja fazer? \n (1, 2, 3 ou 4) \n'))
except (ValueError, TypeError, NameError):
    print('Erro, Por favor digite um número entre de 1 e 4')
if acao == 1: #atualizando Bibliotecas
    print('Atualizando bibliotecas...')
    os.system('sudo apt update') #Atualizando
    print('Bibliotecas atualizadas')
elif acao == 2: #Verificando status do SAMBA
    print('Verificnado status do SAMBA...')
    os.system('systemctl status smbd.service')
elif acao == 3:#Instalando o SAMBA
    print('instalando SAMBA...')
    os.system('sudo apt install samba')
    os.system('y')
    os.system('cp auto_samba /etc/samba/') #Copiando arquivo de configuração primária
    os.system('sudo mkdir -p /srv/samba/share') #Criando diretório
    os.system('sudo chown nobody:nogroup /srv/samba/share/')#Declarando as permissões
    os.system('sudo systemctl restart smbd.service nmbd.service') #reiniciando o serviço
    print('Samba instalado \n Diretórios criados \n Permissões ajustadas ')
elif acao == 4:# Desinstalando samba
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
    
```

