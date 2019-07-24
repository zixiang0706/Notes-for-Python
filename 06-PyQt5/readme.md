# PyQt5
PyQt5类分为很多模块，主要模块有：

- QtCore 包含了核心的非GUI的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用。
- QtGui 包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类。
- QtWidgets 包含了一系列创建桌面应用的UI元素 
- QtMultimedia 包含了处理多媒体的内容和调用摄像头API的类
- QtBluetooth 包含了查找和连接蓝牙的类
- QtNetwork 包含了网络编程的类，这些工具能让TCP/IP和UDP开发变得更加方便和可靠
- QtPositioning 包含了定位的类，可以使用卫星、WiFi甚至文本
- Enginio 包含了通过客户端进入和管理Qt Cloud的类
- QtWebSockets 包含了WebSocket协议的类
- QtWebKit 包含了一个基WebKit2的web浏览器
- QtWebKitWidgets 包含了基于QtWidgets的WebKit1的类
- QtXml 含了处理xml的类，提供了SAX和DOM API的工具。 
- QtSvg 提供了显示SVG内容的类，Scalable Vector Graphics (SVG)是一种是一种基于可扩展标记语言（XML），用于描述二维矢量图形的图形格式（这句话来自于维基百科
- QtSql 提供了处理数据库的工具
- QtTest 提供了测试PyQt5应用的工具

## menu
- 主窗口 所有的内容都是在主窗口内
- 菜单栏 
- 工具栏目
- 状态栏 显示状态信息，位于界面底部
- 右键菜单

## layout
- 绝对定位
- layout类
    - vertical
    - horizon 
    - grid
    
## signal and event
- source
- event
- target

事件触发的时候，发生一个signal，slot是用来被Python调用的（相当于一个句柄？这个词也好恶心，就是相当于事件的绑定函数）slot只有在事件触发的时候才能调用。

## diaglog
使用dialog可以调出一个输入框，方便各种类型的输入
- 字符输入
- 颜色输入
- 字体输入
- 文件操作

## widget
控件就像房子的砖块。
- checkbox
- pushbutton
- toggleButton
- slider
- progressBar
- calendarWidget
