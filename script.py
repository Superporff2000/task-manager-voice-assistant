from os import system

# Implementation of End task (GUI-less)

def endTask(processName):
    killProcess = 'taskkill /im {} /F'.format(processName)  # Statement to be executed
    
    try:
        os.system(killProcess)
    except PermissionError as pe:
        print(pe, ' :The task could not be ended due to Permission Error')

endTask('taskmgr.exe')  #Test function call to close Task Manager window if it is open