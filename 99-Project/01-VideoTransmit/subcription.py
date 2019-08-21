import paho.mqtt.client as mqtt
import time
import datetime
import cv2
import numpy as np

HOST = "47.96.174.116"
PORT = 1883
NAME = "Pi1"
cnt=0
def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
    client.username_pw_set("admin", "123456")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(HOST, PORT, 60)

    client.loop_forever()

def on_connect(client, userdata, flags, rc):

    print("Connected with result code "+str(rc))
    client.subscribe("video")

def on_message(client, userdata, msg):
    # print('time: {}, topic: {}, payload:{}'.
    #       format(datetime.datetime.now(),msg.topic,msg.payload.decode("utf-8")))
    # print(msg.payload.decode("utf-8"))
    image = np.asarray(bytearray(msg.payload), dtype="uint8")
    img_decode = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print(time.time(),'   ',(img_decode.shape))
    cv2.imshow('name',img_decode)
    cv2.waitKey(1)



if __name__ == '__main__':
    client_loop()
