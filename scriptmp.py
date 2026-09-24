import os
import shutil as sh
import tempfile as temp


def obtenerTamano(ruta):
    if os.path.isfile(ruta):
        return os.path.getsize(ruta)
    elif os.path.isdir(ruta):
        tamanoTotal = 0
        for raiz, carpetas, archivos in os.walk(ruta):
            for nombreArchivo in archivos:
                rutaArchivo = os.path.join(raiz, nombreArchivo)
                try:
                    tamanoTotal += os.path.getsize(rutaArchivo)
                except OSError:
                    pass
        return tamanoTotal
    return 0


def formatearTamano(bytesTotales):
    for unidad in ["B", "KB", "MB", "GB"]:
        if bytesTotales < 1024:
            return f"{bytesTotales:.1f} {unidad}"
        bytesTotales /= 1024
    return f"{bytesTotales:.1f} TB"


def mostrarNumeroArchivos(idioma):
    carpetaWindowsTemp = os.path.join(os.environ["SystemRoot"], "Temp")
    if idioma == "ES":
        print(f"Tienes actualmente {len(os.listdir(temp.gettempdir()))} archivos dentro de la carpeta tmp y {len(os.listdir(carpetaWindowsTemp))} en la carpeta temp de windows")
    elif idioma == "G":
        print(f"Tes agora {len(os.listdir(temp.gettempdir()))} arquivos dentro da carpeta tmp e {len(os.listdir(carpetaWindowsTemp))} na carpeta temp de windows")
    else:
        print(f"You currently have {len(os.listdir(temp.gettempdir()))} files inside the tmp folder and {len(os.listdir(carpetaWindowsTemp))} into the Windows temp folder")


idioma = input("Choose your language, write ES for Spanish, E for English, G for Galician: ")

carpetaTemporal = temp.gettempdir()


if idioma == "ES":
    print(f"Vamos a limpiar todos los archivos temporales en Windows, localizados en la ruta {carpetaTemporal}")
    mostrarNumeroArchivos(idioma)
    confirmacion = input("Está seguro de que quiere proceder a la eliminación de los archivos? S/n: ")

    while confirmacion not in ("n", "S"):
        print("Seleccione una opción válida para proceder")
        confirmacion = input("S/n: ")

    if confirmacion == "n":
        print("Se va a detener el borrado de los archivos del programa...")
        exit()
    else:
        print("Procedemos a la eliminación...")

elif idioma == "G":
    print(f"Imos limpar todos os archivos temporais en Windows, localizados na ruta {carpetaTemporal}")
    mostrarNumeroArchivos(idioma)
    confirmacion = input("Está seguro de que quere proceder á eliminación dos arquivos? S/n: ")

    while confirmacion not in ("n", "S"):
        print("Seleccione unha opción válida para proceder")
        confirmacion = input("S/n: ")

    if confirmacion == "n":
        print("Vaise deter o borrado dos arquivos do programa...")
        exit()
    else:
        print("Procedemos á eliminación...")

elif idioma == "E":
    print(f"We're going to erase all Windows files located in the route {carpetaTemporal}")
    mostrarNumeroArchivos(idioma)
    confirmacion = input("Are you sure you want to proceed with the deletion of the files? S/n: ")

    while confirmacion not in ("n", "S"):
        print("Select a valid option to proceed")
        confirmacion = input("S/n: ")

    if confirmacion == "n":
        print("The file deletion process will now stop...")
        exit()
    else:
        print("Proceeding with the deletion...")

else:
    raise ValueError("Choose the correct language")

contador = 0
espacioLiberado = 0

listaDeArchivos = os.listdir(carpetaTemporal)
for archivo in listaDeArchivos:
    rutaIndividualDeCadaArchivo = os.path.join(carpetaTemporal, archivo)
    try:
        tamano = obtenerTamano(rutaIndividualDeCadaArchivo)

        if os.path.isfile(rutaIndividualDeCadaArchivo):
            os.remove(rutaIndividualDeCadaArchivo)
        elif os.path.isdir(rutaIndividualDeCadaArchivo):
            sh.rmtree(rutaIndividualDeCadaArchivo)

        espacioLiberado += tamano

    except OSError:
        print(f"No se ha podido borrar el archivo {archivo} porque actualmente se encuentra en uso")
        contador += 1

carpetaWindowsTemp = os.path.join(os.environ["SystemRoot"], "Temp")
listaDeArchivos = os.listdir(carpetaWindowsTemp)

for archivo2 in listaDeArchivos:
    rutaIndividualDeCadaArchivo = os.path.join(carpetaWindowsTemp, archivo2)
    try:
        tamano = obtenerTamano(rutaIndividualDeCadaArchivo)

        if os.path.isfile(rutaIndividualDeCadaArchivo):
            os.remove(rutaIndividualDeCadaArchivo)
        elif os.path.isdir(rutaIndividualDeCadaArchivo):
            sh.rmtree(rutaIndividualDeCadaArchivo)

        espacioLiberado += tamano

    except OSError:
        print(f"No se ha podido borrar el archivo {archivo2} porque actualmente se encuentra en uso")
        contador += 1


if idioma == "ES":
    print(f"Se ha completado el borrado, han faltado por eliminar {contador} archivos entre las dos carpetas")
    print(f"Espacio liberado: {formatearTamano(espacioLiberado)}")
elif idioma == "G":
    print(f"Completouse o borrado de {contador} archivos entre as dúas carpetas")
    print(f"Espazo liberado: {formatearTamano(espacioLiberado)}")
else:
    print(f"{contador} files were deleted between both folders")
    print(f"Freed space: {formatearTamano(espacioLiberado)}")

input("Presione enter para terminar...")