from log import *
import os





n = input("Nombre del log: ")

logger = Log(current_time(), n, f"{get_appdata_folder('TomasKalau', 'PyTests')}/logs/", True)
logger.log(current_time(), "Class","Log")
logger.log(current_time(), "Log","xD")

op = input("Selecciona una opcion: \n1. Borrar log file\n2. Escribir log\n3. Probar getters\n4. Cerrar programa\n")
if op == "1":
    logger.delete_file()
    print("Archivo eliminado con exito")
    logger.close_file()
elif op == "2":
    log_input = input("Esribe el log:\n")
    logger.log(current_time(), "Log",log_input)
    logger.close_file()
    print(str(check_logvars("auth=True", 1, logger.get_directory())))
elif op == "3":
    print(logger.get_directory())
    print(logger.get_folder())
    print(logger.get_file_name())
    logger.close_file()
elif op == "4":
    logger.close_file()
    exit()
else:
    print("Opcion es incorrecta o no existe")