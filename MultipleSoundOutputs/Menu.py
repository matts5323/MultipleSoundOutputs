import pyaudio
import sys
import subprocess
import os
from tkinter import *
from tkinter import messagebox
p = pyaudio.PyAudio()
root = Tk()
root.title('Multi Sound Out')
root.geometry("625x150")
root.resizable(False, False)
photo = PhotoImage(file = "icon.png")
root.iconphoto(False, photo)


inputlist = ""
outputlist = ""
def input(event):     
    cable_out = clicked.get()[0]
    return cable_out

inlabel = Label(text = "Input Device:")
inlabel.pack(fill = BOTH, side=LEFT)
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        inputdevices = (str(i) + " - " + p.get_device_info_by_host_api_device_index(0, i).get('name') + ",*/*<")
        inputlist += inputdevices
        options = inputlist.split(",*/*<")
        inputlength = (str(i))
               
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options[:-1], command=input)
drop.pack(padx=5, pady=10, side=LEFT)

outlabel = Label(text = "Output Devices:")
outlabel.pack(fill = BOTH, side=LEFT)
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
        outputdevices = (p.get_device_info_by_host_api_device_index(0, i).get('name') + ",*/*<")
        outputlist += outputdevices
        options2 = outputlist.split(",*/*<")

my_scrollbar = Scrollbar(orient=VERTICAL)

list = Listbox(root, selectmode = "multiple", width=30, yscrollcommand=my_scrollbar.set)
list.pack(padx=5, pady=10, side=LEFT)
for each_item in range(len(options2[:-1])):

    list.insert(END, (options2[each_item]))

def getSelection(list):
    values = list.curselection()  
    os.system('taskkill /im py.exe')
    while len(values) > 0:
        pyfile = ""
        cable_in = values[0] + int(inputlength) + 1
        cable_out = input(clicked)
        mediafile = "{}".format(cable_in) + "_output.py"
        f = open(mediafile , "w")
        f.write("import os\rimport sys\rimport pyaudio\rclass audio():\r    CHUNK = 1024\r    CHUNK = 1024\r    FORMAT = pyaudio.paInt16\r    CHANNELS = 2\r    RATE = 44100\r    cable_out = " + str(cable_out) + " # device index found by p.get_device_info_by_index(ii)\r    cable_in = " + str(cable_in) + "\r    p = pyaudio.PyAudio()\r    stream = p.open(\r        format=FORMAT,\r        channels=CHANNELS,\r        rate=RATE,\r        input=True,\r        input_device_index = cable_out,\r        output=True,\r        output_device_index = cable_in,\r        frames_per_buffer = CHUNK,\r        )  \r    while 0==0:\r        data = stream.read(CHUNK)\r        stream.write(data)\r")
        f.close()
        values = values[1:]
        directory = os.getcwd()   
        os.system('Start /min ' + directory + '/' + mediafile)
    
def stop():
    os.system('taskkill /im py.exe')
    
buttonas= Button(root, text="Start Sound", command= lambda: getSelection(list))
buttonas.pack()
buttonas.place(relx = .03, rely = .6, height=50, width=150)

buttons= Button(root, text="Stop Sound", command = lambda: stop())
buttons.pack()
buttons.place(relx = .3, rely = .6, height=50, width=150)

my_scrollbar.config(command=list.yview)
my_scrollbar.pack(side=RIGHT, fill='y')

root.mainloop()

