import socket
import xml.etree.ElementTree as ET
import re,time


def main(q):
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    # HOST1 = '10.1.110.1'
    # PORT = 55655
    #
    # s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s1.connect((HOST1,PORT))

    while True:
        # data = s1.recv(1024)
        # data_xml = data.decode('utf-8').rstrip('\n\x00')
        with open('abnormal', 'r') as f:
            data_xml=f.read()
        print(data_xml)
        print('\n')
        data_xml_list = re.findall(r'<\?xml.*?</.*?>', data_xml, re.S)
        info = {}
        for item in data_xml_list:
            tree = ET.ElementTree(ET.fromstring(item))
            root = tree.getroot()
            for child in root:
                dic=child.attrib
                for key,value in dic.items():
                    info[key]=value
            q.put(info)
            time.sleep(1)
