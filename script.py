from os import system

# End task (GUI-less, voice-input-less)
def endTask(processName):
    killProcess = 'taskkill /im {} /F'.format(processName)  # Statement to be executed

    try:
        system(killProcess)
    except OSError as e:
        print(e, ' :The task could not be ended due to Permission Error')

#  Set Priority (GUI-less, Voice-input-less)
def setPriority(value):
    from psutil import Process

    priorityStatus = {
        64 : 'Low',
        16384 : 'Below Normal',
        32:'Normal',
        32768: 'Above Normal',
        128 : 'High'
    }

    '''Set the Process Priority'''
    p = Process()

    if value in priorityStatus:
        p.nice(value)

    # Console Output statement for confirmation
        for i in priorityStatus:
            if i == value:
                print( 'The current program\'s priority has been set to {0}'.format(priorityStatus[value]) )
    else:
        print('The given value is not valid')

setPriority(32)

# Create debug log and store it