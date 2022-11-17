from models import Process, List
from threading import Thread, Event
import time

event = Event()

start_time = time.time()

def main():
    list_active = List(start_time)
    list_active.name = 'list_active'

    historical = List(start_time)
    historical.name = 'historical_list'
    
    process1 = Process("One", 0, 2)
    process2 = Process("Two", 0, 5)
    process3 = Process("Three", 0, 7)
    process4 = Process("Four", 0, 3)

    

    list_active.add_process(process1)
    list_active.add_process(process2)
    list_active.add_process(process3)
    list_active.add_process(process4)

    # Create Principal Thread
    principal_list_thread = Thread(target=principal_list,args=(list_active, historical, ))
    principal_list_thread.start()

    # Create Historical Thread
    history_list_thread = Thread(target=history_list,args=(historical, ))
    history_list_thread.start()

    
def principal_list(list, historical):
    while True:
        list.execute(historical)

def history_list(list):
    while True:
        list.print_list()
        time.sleep(2)


if __name__ == '__main__':
    main()