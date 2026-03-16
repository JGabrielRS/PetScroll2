import paramiko

# TODO configurar senha e usuário do mysql

# TEMP
config = {'MYSQL_USER': '', 'MYSQL_PASSWORD': ''}

# TODO Falta copiar o arquivo sql
def execMysql(sqlpath):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('200.19.177.46', username='pet', key_filename='/home/petcompufc/.ssh/petdc')
    stdin, stdout, stderr = ssh.exec_command('mysql --user='+config.get('MYSQL_USER')+' --password='+config.get('MYSQL_PASSWORD'))
    
    # CUIDADO! o send aqui roda no banco de dados
    stdin.channel.send("\. "+sqlpath)
    stdin.channel.shutdown_write()
    
    # TODO formatar saida
    print(stdout.read().decode())
    print(stderr.read().decode())

execMysql()

def transferirArquivo(caminho_arquivo): 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('200.19.177.46',username='pet',key_filename='/home/petcompufc/.ssh/petdc')

    sftp = ssh.open_sftp()
    sftp.put(caminho_arquivo, 'sac_2025.png')

    sftp.close()
    ssh.close()