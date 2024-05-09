import subprocess
import sys
import urllib.parse

def ejecutar_comandos(comandos):
    for comando in comandos:
        if comando.endswith("/"):
            comando = comando[:-1]
        ejecutar_comando(comando)

def ejecutar_comando(comando):
    try:
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for linea in proceso.stdout:
            print(linea, end='')

        proceso.wait()
        
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando:", e)

def main():
    args = sys.argv[1:]
    if args[0].startswith("cmd://"):
        args[0] = args[0][6:]
    
    args = [urllib.parse.unquote(arg) for arg in args]

    comandos = ' '.join(args).split(';')
    comandos = [comando.strip() for comando in comandos if comando.strip()]

    ejecutar_comandos(comandos)

    input("Presione una tecla para cerrar el programa...")

if __name__ == "__main__":
    main()