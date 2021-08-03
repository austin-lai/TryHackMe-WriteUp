
import re
import socket
import requests
from urllib import request


HOST = '10.10.159.183'  # The server's hostname or IP address
StartPORT = 3010       # The port used by the server
LivePort = 1337        # This the port we want to get correct order of number
int_port = 0
Num = 0
StartNum = 0
TotalNum = 0
second_true = ''


try:
    # FIRST CONNECT with default given port 3010
    if (StartPORT == 3010):
        with request.urlopen('http://'+HOST+':'+str(StartPORT)+'/') as response:
            content = response.read().decode('utf-8')

            # Trim the response - 767 btyes anything before
            http_trim = content[767:]

            # Split the response into array with space
            data_list = list(http_trim.split(" "))
            # print(data_list)

            # Get the length of array
            # print("Length="+str(len(data_list)))

            # Find the 30th index of array
            index_30 = str(data_list[30])
            # print(index_30, end = ' ') # Print without new line # Sample output of content # "http://"+window.location.hostname+":34232"</script>

            # Split the data inside array
            # split_index_30 = data_list[30].split(':')
            # print(split_index_30)

            # if(port != StartPORT):

            # Extract all number from the response
            port = re.findall(r'\d+', index_30)

            # Change to int
            int_port=int(port[0])
            # print(type(int_port))

            # print(index_30+str(int_port))
            StartPORT=int_port

    # print('Current Start Port = '+str(StartPORT))
    print('\nFirst request on port 3010 done ... Current port is set to = '+str(StartPORT))


    while (StartPORT != 9765):
        try:
            if (StartPORT != 1337):

                second_true = 'false'
                print('Starting while loop here ... Current port is '+str(StartPORT))

                with request.urlopen('http://'+HOST+':'+str(StartPORT)+'/') as response:
                    content = response.read().decode('utf-8')
                    # print(content) # Sample output of content # multiply 1 6783

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
                # print(content) # Sample output of content # multiply 1 6783

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
