from datetime import datetime
import os.path

def get_appdata_folder(company, appName):
    datapath = os.getenv('APPDATA').replace('Roaming', 'LocalLow')
    datapath += f"/{company}"
    if not os.path.isdir(datapath):
        os.mkdir(datapath)

    datapath += f"/{appName}"
    if not os.path.isdir(datapath):
        os.mkdir(datapath)
    return datapath

def current_time():
    return datetime.now()

class Log:
    def __init__(self, ct, name, directory=None, saveOnExit=False):
        ct0 = ct.strftime("%d.%m.%Y %H:%M:%S")
        ct_1 = ct.strftime("%d.%m.%Y_%H.%M.%S")

        _dir = ""

        if directory is not None:
            _dir = directory
            if not os.path.isdir(directory):
                os.mkdir(directory)

        if not os.path.isdir(directory + '/crashes/'):
            os.mkdir(directory + '/crashes/')
        _file_name = f'[{ct_1}]_{name}.logfile'

        _dir += _file_name

        _file_exists = os.path.exists(_dir)

        if _file_exists:
            os.remove(_dir)

        f = open(_dir, "w")
        f.write(f'LogFile: init=True auth=False authAsk=False saveFile={str(saveOnExit)} \n')
        _t = f'[Init][{ct0}] Iniciando Logs... \n'
        f.write(str(_t))

        self._f = f
        self._dir = _dir
        self._folder = directory
        self._file_name = _file_name
# Create Logs
    def log(self, ct, type,text):
        ct = ct.strftime("%d.%m.%Y %H:%M:%S")
        t = f'[{type}][{ct}] {text}\n'
        self._f.write(str(t))
# File Managment
    def delete_file(self):
        self._f.close()

        _file_exists = os.path.exists(self._dir)
        if _file_exists:
            os.remove(self._dir)
            return True
        else:
            return False

    def close_file(self):
        self._f.write(f'LogFile: closed=True')
        self._f.close()
        return True

# File getters
    def get_file(self):
        return self._f

    def get_file_name(self):
        return self._file_name

    def get_folder(self):
        if self._folder:
            return self._folder
        else:
            return ""

    def get_directory(self):
        return self._dir

def check_logvars(var, varPlace, filePath): # Encontrar variables
    find = "LogFile: "
    if varPlace == 0:
        find +="init "
    else:
        find+="close"

    with open(filePath) as log_file:
        filedata = log_file.readlines()
        for line in filedata:
            if find in line:
                if var in line:
                    return True
                else:
                    return False
            else:
                return "No line"

        log_file.close()






