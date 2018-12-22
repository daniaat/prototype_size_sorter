''''
Author: Mostafa Elkabir & Taha Anwar
Project: Size Sorter
Company: Daniaat

#### here will have the code to 1) controll motors
#### 2) run a video and get size results
'''

import size_sorter # function to get size of dates using kmeans
import cv2   ## used mainly to un a video
import arduino_communication as ard_com  ### used to comunicate with the arduino
import time   ### will be used mainly for sleep, and measure obustness of code

size_to_command = {'size':'Adruino Command'}
size_to_command.update({'small':0,'meduim':2,'large':4,'partB_open':8,'partB_close':9})

def init_model(init_frame):
    size_class = size_sorter.DominantColors(init_frame,2)
    size_class.init_model(init_frame)
    ### then we will keep using this model
    return size_class

def get_size(size_class,frame):
    # sc = size_sorter.DominantColors(frame,2)
    size = size_class.output_size(frame)
    return size

if __name__ == '__main__':
    connection = ard_com.init_connection()
    flag, frame = cv2.VideoCapture()
    class_model = init_model(frame)
    while flag:
        date_size = get_size(class_model,frame)
        ## communicate with Arduino ###
        ard_com.send_to_arduino(connection,size_to_command['partB_open'])
        ard_com.send_to_arduino(connection,size_to_command[date_size])
        ard_com.send_to_arduino(connection,size_to_command['partB_close'])
        time.sleep(0.1)
    ard_com.close_connection(connection)