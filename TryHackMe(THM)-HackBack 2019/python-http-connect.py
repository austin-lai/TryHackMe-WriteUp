
import re
import socket
import requests
from urllib import request


HOST = '10.10.159.183'  # The server's hostname or IP address
StartPORT = 3010        # The port used by the server
LivePort = 1337         # This the port we want to get correct order of number
int_port = 0            # Variable to store the given port number from instruction as integer
Num = 0                 # Variable to store dynamic value given from instruction
StartNum = 0            # Variable and set to 0 from start to clear any value
TotalNum = 0            # Variable to store value from calculation
second_true = ''        # Counter check for second while loop


try:
    # FIRST CONNECT with default given port 3010
    if (StartPORT == 3010):
        with request.urlopen('http://'+HOST+':'+str(StartPORT)+'/') as response:
            
            # Store the conetnt of http response into variable content
            content = response.read().decode('utf-8')

            # Trim 767 btyes off from the response - for the first http response
            http_trim = content[767:]

            # Split and store the response into list type variable data_list with space
            data_list = list(http_trim.split(" "))
            
            # Check and print the content of list type variable data_list
            # print(data_list)

            # Get the length of list type variable data_list
            # print("Length="+str(len(data_list)))

            # Find the 30th index of list
            index_30 = str(data_list[30])
            
            # Check and print the content inside list type variable index_30 --- without new line 
            # Sample output of content
            # "http://"+window.location.hostname+":34232"</script>
            # print(index_30, end = ' ')  

            # Split the data inside the list type variable data_list
            # split_index_30 = data_list[30].split(':')
            
            # Check and print the content inside list type variable split_index_30 
            # print(split_index_30)
            
            # Extract all number from the response which currently store inside list type variable index_30
            port = re.findall(r'\d+', index_30)

            # Change to int
            int_port=int(port[0])
            
            # Check and confirm the type of variable int_port
            # print(type(int_port))

            # Set value of int_port as StartPORT
            StartPORT=int_port

    print('\nFirst request on port 3010 done ... Current port is set to = '+str(StartPORT))

    
    # Start first while loop that the StartPORT is not 9765
    while (StartPORT != 9765):
        try:
            if (StartPORT != 1337):

                second_true = 'false'
                print('Starting while loop here ... Current port is '+str(StartPORT))

                with request.urlopen('http://'+HOST+':'+str(StartPORT)+'/') as response:
                    content = response.read().decode('utf-8')
                    
                    # Sample output of content 
                    # multiply 1 6783
                    # print(content) 

                    data_list=content.split(" ")

                    # print('Operation: '+data_list[0]+', number: '+ data_list[1]+', next port: '+ data_list[2])

                    int_port=int(data_list[2])

                StartPORT=int_port
                print('Checking current port before next loop = '+str(StartPORT)+'\n')
            else:
                second_true = 'true'
                print('Second true is '+second_true+'. Checking current port before next loop = '+str(StartPORT)+'\n')
                break
        except Exception:
            pass


    while (second_true == 'true') and (StartPORT != 9765):
        try:

            print('Second true is '+second_true+'. Current port set = '+str(StartPORT))
            with request.urlopen('http://'+HOST+':'+str(StartPORT)+'/') as response:

                content = response.read().decode('utf-8')
                
                # Sample output of content 
                # multiply 1 6783
                # print(content) 

                data_list=content.split(" ")

                print('Operation: '+data_list[0]+', number: '+ data_list[1]+', next port: '+ data_list[2])

                int_port=int(data_list[2])

                StartPORT=int_port
                print('Current port set = '+str(StartPORT))

                print('Current StartNum = '+str(StartNum))

                Num = float(data_list[1])

                if(data_list[0] == 'add'):
                    StartNum =  (StartNum + Num)
                    print('Current StartNum = '+str(StartNum))
                elif(data_list[0] == 'minus'):
                    StartNum =  (StartNum - Num)
                    print('Current StartNum = '+str(StartNum))
                elif(data_list[0] == 'multiply'):
                    StartNum =  (StartNum  * Num)
                    print('Current TotalNum = '+str(StartNum))
                elif(data_list[0] == 'divide'):
                    StartNum =  (StartNum  / Num)
                    print('Current TotalNum = '+str(StartNum))
                
            TotalNum = StartNum
            print('Current TotalNum before next loop = '+str(TotalNum)+'\n\n')

        except Exception:
            pass

except KeyboardInterrupt:
    print('interrupted!')
