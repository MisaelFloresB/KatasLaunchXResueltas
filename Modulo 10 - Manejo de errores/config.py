def main():
    try:
        configuration = open('config1.txt')
    #Mensaje a mostrar si el archivo no existe
    except FileNotFoundError:
    #except Exception:
        print("Couldn't find the config.txt file!")
    #Mensaje a mostrar si el no se tienen permisos para acceder al archivo
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    #Mensaje a mostrar si se tarda demasiado el sistema en poder leer el archivo
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()