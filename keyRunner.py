from threading import Thread
import subprocess
import os
import sys
import obspython as S

#t1 = Thread(target=subprocess.run, args=(["python", "keyListener.py"],))
#t1.start()

#os.system('cmd  /k python C:/Users/PatHQ/Desktop/obs/data/obs-plugins/frontend-tools/scripts/keyListener.py')
#os.system('cmd  /k python X:\Python\OBSeventListener\keyListener.py')
#p = subprocess.Popen([sys.executable, 'cmd  /k python "C:/Users/PatHQ/Desktop/obs/data/obs-plugins/frontend-tools/scripts/keyListener.py"'], 
#                                    stdout=subprocess.PIPE, 
#                                    stderr=subprocess.STDOUT)
#X:\Python\OBSeventListener\keyListener.py

if (S.obs_frontend_streaming_active()):
    p = subprocess.Popen(['cmd /k python keyListener.py'],
                     shell = True,
                     stdin = None,
                     stdout = None,
                     stderr = None,
                     close_fds = True)

    print("subProcess active")

if (S.obs_frontend_recording_active()):
    p = subprocess.Popen(['cmd /k python keyListener.py'],
                     shell = True,
                     stdin = None,
                     stdout = None,
                     stderr = None,
                     close_fds = True)

    print("subProcess active")
#t1.join()
