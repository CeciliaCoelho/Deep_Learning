from bs4 import BeautifulSoup
import os

#file_label -> folder where Pascal VOC annotations are stored
#file_label_write -> folder where the converted CSV annotations will be stored

def PascalToCSV(file_label , file_label_write):

    for _,_,f in os.walk(file_label):
        for file in f:
            with open(file_label + file,'r') as fd:
                lines = fd.read()
            xml = BeautifulSoup(lines)
            filename = file_label + xml.find("filename").text
            name = list(map(lambda x: x.text,xml.findAll("name")))
            xmin = list(map(lambda x: x.text,xml.findAll("xmin")))
            xmax = list(map(lambda x: x.text,xml.findAll("xmax")))
            ymin = list(map(lambda x: x.text,xml.findAll("ymin")))
            ymax = list(map(lambda x: x.text,xml.findAll("ymax")))


            with open(file_label_write + file.split(".")[0] + ".csv",'a') as fd:
                for i,name_i in enumerate(name):
                    #-------Add dataset labels here
                    if name_i == '0':
                        name_i = 'pool'
                    #-------
                    fd.write(",".join([filename,xmin[i],ymin[i],xmax[i],ymax[i],name_i]))
                    fd.write("\n")
