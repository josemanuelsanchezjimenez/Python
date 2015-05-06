import sock1 #this is an external file 
import ftplib
import socket
import csv

def main():

    """
    FTP using Sockets Default Proxy

    No Args:
    ----------
    """
    
    #Set-Up the Proxy
    sock1.setdefaultproxy(sock1.PROXY_TYPE_SOCKS5, PROX_ADDRESS, PROXY_PORT)
    socket.socket = sock1.socksocket
    
    #Set-Up the FTP Connection
    ftp = ftplib.FTP(FTP_SERVER_IP)
    ftp.login(FTP_USER, FTP_PASSWORD)
    #ftp.set_debuglevel(2)
        
    #Check if conn is OK
    #import urllib2
    #print urllib2.urlopen('http://www.google.com').read()
    
    #Open the file where The progam stores the Log
    c = csv.writer(open("data_log.csv", "wb"))
    
    #Open the file where there is the Files Path to Upload
    with open('data.csv', 'rb') as f:
        
        #Loop the Csv File
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            new_row =[]
            new_row_error =[]
            
            #Retrieve the Properties of Origin Files to be UpLoad
            origin_folder = row[0]
            origin_file_name = row[1]
            origin_file = origin_folder + origin_file_name
            
            #Retrieve the Properties of FTP Paths
            FTP_Folder = row[2]
            FTP_file_name = row[3]
            FTP_File = FTP_Folder + "/" + FTP_file_name
            
            print FTP_File
            
            try:
              
                #try to open The file
                f = open(origin_file, "rb") #open in normal read mode
                #Change the Folder of FTP
                ftp.cwd(FTP_Folder)
                #print ftp.dir()
                
                #Copy line by line a Text File
                #ftp.storlines("STOR " + fichero_Destino, open(file_origen))
                
                #Set-UP the mode of Upload the information
                ftp.sendcmd("TYPE I")  
                #Upload the information
                ftp.storbinary("STOR %s" % FTP_File,f)  
                
                f.close()
                #print ftp.dir()            
                
                #ADD the ifnormation to CSV Log
                new_row.append("Origin File: " + origin_file + " copied in: " + FTP_File)
                c.writerow(new_row)

            except:  
                new_row_error.append("Error Origin File: " + origin_file + " NOT copied in: " + FTP_File)
                c.writerow(new_row_error)


            
    ftp.quit()     
    ftp.close()
    print "====================================="
    print "FTP Close"
    
# main selector
if(__name__=="__main__"):

    #running the unittest methods
    #unittest.main()
    #we set the main and start the element
    main()
