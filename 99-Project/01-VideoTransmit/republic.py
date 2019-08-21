import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import datetime
import time
import cv2
import numpy as np



HOST = "47.96.174.116"
PORT = 1883
NAME = "Pi1"
cnt=0


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("video")


def on_message(client, userdata, msg):
    # print('time: {}, topic: {}, payload:{}'.
    #       format(datetime.datetime.now(),msg.topic,msg.payload.decode("utf-8")))
    # print(msg.payload.decode("utf-8"))
    image = np.asarray(bytearray(msg.payload), dtype="uint8")
    img_decode = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print(time.time(),'   ',(img_decode.shape))
    cv2.imshow('name',img_decode)
    cv2.waitKey(1)

class My_publish():
    def __init__(self):
        client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.client = mqtt.Client(client_id)  # ClientId不能重复，所以使用当前时间
        self.client.username_pw_set("admin", "123456")  # 必须设置，否则会返回「Connected with result code 4」
        self.client.on_connect = on_connect
        # self.client.on_message = on_message
        self.client.connect(HOST, PORT, 60)
        self.client.loop_start()
        # self.client.loop_forever()


if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    camera.set(3,640)
    camera.set(4,480)
    my_pub = My_publish()
    while 1:
        t1=time.time()
        rec, img = camera.read()
        # img = cv2.resize(img, (640, 480))
        img_encode = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])[1]
        data_encode = np.array(img_encode)
        str_encode = data_encode.tostring()

        t2 = time.time()
        my_pub.client.publish("video",str_encode,qos=0)
        print("total delay:{:.3f} publish delay:{:.3f} publish size:{}KB "
              .format(time.time() - t1 , time.time()-t2,len(str_encode)//1024))
        time.sleep(0.1)
