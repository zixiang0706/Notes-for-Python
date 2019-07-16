
import time
import threading,queue
import UI
import interface

q=queue.Queue()
t1=threading.Thread(target=UI.main,args=(q,))
t2=threading.Thread(target=interface.main,args=(q,))
t1.start()
t2.start()
t1.join()
t2.join()





