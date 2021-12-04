from os import system
import signal

processName = 'kited.exe'
killProcess = 'taskkill /im {} /F'.format(processName)
os.system(killProcess)