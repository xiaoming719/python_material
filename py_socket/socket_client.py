# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:15:50 2018

@author: xiaoming
"""

if __name__=="__main__":    
        import socket    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        sock.connect(('localhost', 8001))    
        import time    
        flag = '1'  
        while True:   
                time.sleep(3)    
                print ('send to server with value: '+ flag)   
                sock.send(flag.encode(encoding="gb2312"))    
                print (sock.recv(1024).decode("gb2312"))   
                flag = (flag=='1') and '2' or '1' #change to another type of value each time  
  
                  
        sock.close()  
      
      
