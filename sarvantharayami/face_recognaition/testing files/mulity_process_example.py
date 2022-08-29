from multiprocessing import Process

def example_function():
    i=0
    while i<20:
        print("hello"+str(i))
        i+=1
   
p = Process(target=example_function)
p1 = Process(target=example_function)
      
if __name__ =="__main__":
    p.start()
    p1.start()
    p.join()
    p1.join()