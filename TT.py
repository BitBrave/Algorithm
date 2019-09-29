# encoding = utf-8

# BitBrave, 2019-05-30
# Describetion: 
'''
    1. find match pacp with excel labels
    2. compute charactics in database
    3. labeled all flows pcap file
    4. create a demo to test neural network model
'''
import os
import csv
from xml.dom.minidom import parse
import xml.dom.minidom

os.chdir('C:/Users/gf/Desktop/ISCX-IDS-2012/labeled_flows_xml/')

import xml.sax

Tuple_flows = {}
count = 0
malcount = 0
class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.source = ""
        self.sourcePort = ""
        self.destination = ""
        self.destinationPort = ""
        self.Tag = ""
    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "Tag": pass
            
        return

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "source":
            self.source = content
        elif self.CurrentData == "sourcePort":
            self.sourcePort = content
        elif self.CurrentData == "destination":
            self.destination = content
        elif self.CurrentData == "destinationPort":
            self.destinationPort = content
        elif self.CurrentData == "Tag":
            self.Tag = content
            print(self.source, " ") #, self.sourcePort, " ",self.destination, " ", self.destinationPort, " ", self.Tag)

            global count
            global malcount
            global Tuple_flows
            count += 1
            if self.Tag != 'Normal': malcount += 1
            
            tuple_flow = self.source + self.sourcePort + self.destination + self.destinationPort
            tuple_flow_ = self.destination + self.destinationPort + self.source + self.sourcePort
            if tuple_flow in Tuple_flows:
                if Tuple_flows[tuple_flow] == "Normal":
                    Tuple_flows[tuple_flow] = self.Tag
            elif tuple_flow_ in Tuple_flows:
                if Tuple_flows[tuple_flow_] == "Normal":
                    Tuple_flows[tuple_flow_] = self.Tag
            else:
                Tuple_flows[tuple_flow] = self.Tag
            self.CurrentData = ""
        return

def ReadXML2(path, a, b):
    global count
    global malcount
    global Tuple_flows
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    parser.parse(path)
    print(path, "Get label dict: ", len(Tuple_flows), "; flows: ", count, '; Mal: ', malcount)
    return b


# return dict{ tuple:Tag }
def ReadXML(path, tag, tuple_flows):
    DOMTree = xml.dom.minidom.parse(path)
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print ("Root element : %s" % collection.getAttribute("shelf"))

    # 在集合中获取所有TestbedSunJun13Flows
    flows = collection.getElementsByTagName(tag)

    # 打印每部电影的详细信息
    
    tuple_flow = ""
    count = 0
    for flow in flows:
        count += 1
        source = flow.getElementsByTagName('source')[0]
        tuple_flow = source.childNodes[0].data
        sourcePort = flow.getElementsByTagName('sourcePort')[0]
        tuple_flow += "_" + sourcePort.childNodes[0].data
        destination = flow.getElementsByTagName('destination')[0]
        tuple_flow += "_" + destination.childNodes[0].data
        destinationPort = flow.getElementsByTagName('destinationPort')[0]
        tuple_flow += "_" + destinationPort.childNodes[0].data

        Tag = flow.getElementsByTagName('Tag')[0]

        tuple_flow_ = tuple_flow.split('_')
        tuple_flow_ = tuple_flow[2] + tuple_flow[3] + tuple_flow[0] + tuple_flow[1]
        

        if tuple_flow in tuple_flows:
            if tuple_flows[tuple_flow] == "Normal":
                tuple_flows[tuple_flow] = Tag.childNodes[0].data
        elif tuple_flow_ in tuple_flows:
            if tuple_flows[tuple_flow_] == "Normal":
                tuple_flows[tuple_flow_] = Tag.childNodes[0].data
        else:
            tuple_flows[tuple_flow] = Tag.childNodes[0].data
        tuple_flow = ""
    print(path, "Get label dict: ", len(tuple_flows), "; flows: ", count)
    return tuple_flows

# return dict{ tuple:Tag }
def ReadCSV(path, tuple_flows):
    with open(path, 'r', encoding='utf-8') as csvfile:
        read = csv.reader(csvfile)
        count = 0
        malcount = 0
        for i in read: break
        for item in read:
            count += 1
            if item[-1] != 'BENIGN': malcount += 1
            tup = item[1] + "_" + item[2] + "_" +item[3] + "_" + item[4]
            if tup in tuple_flows:
                if tuple_flows[tup] == "BENIGN": tuple_flows[tup] = item[-1]
            elif (item[3] + "_" + item[4] + "_" + item[1] + "_" + item[2]) in tuple_flows:
                tup_ = item[3] + "_" + item[4] + "_" + item[1] + "_" + item[2]
                if tuple_flows[tup_] == "BENIGN": tuple_flows[tup_] = item[-1]
            else:
                tuple_flows[tup] = item[-1]
                
    print(path, "Get label dict: ", len(tuple_flows), "; CSV lines: ", count, "; Mal: ", malcount)
    return tuple_flows

# return list[pcapname1, pcapname2, ...]
def ReadPcap(path, pcap_list = []):
    pcap_list = os.listdir(path)
    print("Get pcap files list: ", len(pcap_list))
    return pcap_list

# write result label_ed
def WriteLabel(pcap, tuple_flows, record):
    wr = open(record, 'w')
    count = 0
    malcount = 0
    for item in pcap:
        item = item[:-5]
        if item in tuple_flows:
            count += 1
            if (tuple_flows[item]!="Normal") & (tuple_flows[item]!="BENIGN"): malcount += 1
            wr.write(item + "\t" + tuple_flows[item] + "\n")
        else:
            titem = item.split('_')
            titem = titem[2]+'_'+titem[3]+"_"+titem[0]+"_"+titem[1]
            if titem in tuple_flows:
                count += 1
                if (tuple_flows[titem]!="Normal") & (tuple_flows[titem]!="BENIGN"): malcount += 1
                wr.write(item + "\t" + tuple_flows[titem] + "\n")
    print("Write OK, dict: ", len(tuple_flows), "; pcap files: ", len(pcap), "; labeled: ", count, "; Mal: ", malcount)
    wr.close()
    return

def ISCX2012():
    tuple_flows = {}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    tuple_flows = ReadXML("C:/Users/gf/Desktop/ISCX-IDS-2012/labeled_flows_xml/TestbedThuJun17-1Flows.xml", "TestbedThuJun17-1Flows", tuple_flows)
    tuple_flows = ReadXML("C:/Users/gf/Desktop/ISCX-IDS-2012/labeled_flows_xml/TestbedThuJun17-2Flows.xml", "TestbedThuJun17-2Flows", tuple_flows)
    tuple_flows = ReadXML("C:/Users/gf/Desktop/ISCX-IDS-2012/labeled_flows_xml/TestbedThuJun17-3Flows.xml", "TestbedThuJun17-3Flows", tuple_flows)
    pcap_list = []
    pcap_list = ReadPcap('C:/Users/gf/Desktop/cuted_data/Data_XJ/ISCX-IDS-2012/testbed-17jun/ret/', pcap_list)
    WriteLabel(pcap_list, tuple_flows, "TestbedThuJun17Flows.txt")

def CIC2017():
    tuple_flows = {}
    tuple_flows = ReadCSV("C:/Users/gf/Desktop/CIC-IDS-2017/GeneratedLabelledFlows/TrafficLabelling_/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv", tuple_flows)
    tuple_flows = ReadCSV("C:/Users/gf/Desktop/CIC-IDS-2017/GeneratedLabelledFlows/TrafficLabelling_/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv", tuple_flows) 
    tuple_flows = ReadCSV("C:/Users/gf/Desktop/CIC-IDS-2017/GeneratedLabelledFlows/TrafficLabelling_/Friday-WorkingHours-Morning.pcap_ISCX.csv", tuple_flows)
    pcap_list = []
    pcap_list = ReadPcap('C:/Users/gf/Desktop/cuted_data/Data_XJ/CIC-IDS-2017/Friday-WorkingHours/ret/', pcap_list)
    WriteLabel(pcap_list, tuple_flows, "Friday-WorkingHours.txt")
    return


def StatFileNum(path):
    file_list = os.listdir(path)
    num = 0
    for i in file_list:
        tnum = len(os.listdir(path + '/' + i))
        print(path + '/' + i, "\t", tnum)
        num += tnum
    
    print('-'*50)
    print(path, "\t", num)
    return
if __name__ == "__main__":
    #CIC2017()    
    #ISCX2012()
    StatFileNum("G:/台式机file/file/fang/WoTrH18/white/white_tuples")
 