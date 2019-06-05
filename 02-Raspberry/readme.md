# raspberry

## series port
refer to the [article](https://zhuanlan.zhihu.com/p/38853178) which guide us to configure the hardware-series in the configuration  
- hardware series:  
    - 硬件串口需要配置，把功能映射到IO上。
- USB series:  
    - 'lsusb'：查看usb上挂的设备
    - 'ls -l /dev/tty*' ：查看usb串口号 ttyUSB1
    - 'python -m serial.tools.list_ports'：用python查看可用的串口
