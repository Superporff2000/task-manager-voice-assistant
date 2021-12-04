from os import system

# Implementation of End task (GUI-less)

def endTask(processName):
    killProcess = 'taskkill /im {} /F'.format(processName)  # Statement to be executed
    os.system(killProcess)

endTask('taskmgr.exe')  #Test function call to close Task Manager window if it is open