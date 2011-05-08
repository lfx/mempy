import psutil
import sys

mb = 1024*1024

def get_mem(_name):
    pids = psutil.get_pid_list()
    mem = 0
    for i in pids:
        try:
            p = psutil.Process(i)
            if p.name.upper().find(_name.upper()) > -1:
                m=p.get_memory_info()
                mem+=m[0]
        except:
            pass
    
    print 'Memory usage for '+_name+' is: '+str(mem/mb)+' Mb'	

if __name__=='__main__':
    if len(sys.argv)>1:
        get_mem(sys.argv[1])
    else:
        print 'Non app selected. Use "mem2.py google" or etc. '        