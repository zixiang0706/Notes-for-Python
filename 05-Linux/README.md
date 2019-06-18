[TOC]

# Shell-command

| 命令     | 举例                                                         | 作用                                                         | 补充 |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| who am i |                                                              | 显示用户名字                                                 |      |
| pwd      |                                                              | 显示当前路径                                                 |      |
| cd       | cd ..                                                        | parent dictionary                                            |      |
|          | cd ~                                                         | user                                                         |      |
|          | cd /                                                         | root                                                         |      |
| ls       | ls -lh                                                       | 人性化显示                                                   |      |
|          | ls -a                                                        | 显示隐藏文件                                                 |      |
|          | ls -d                                                        | 当前这个目录                                                 |      |
| cat      | cat [test.txt]                                               | View a document                                              |      |
| Vim      | vim [test.txt]                                               | Edit a document. <br />for details, refer to other chapter   |      |
| Nano     | nano [test.txt]                                              | Edit a document using an lite tool                           |      |
| date     |                                                              | view and set the date                                        |      |
| clear    |                                                              | clear the history of ssh                                     |      |
| Man      | man [clear]                                                  | view the help document of [command]                          |      |
| Who      |                                                              | view the login user                                          |      |
| w        |                                                              | view the login user                                          |      |
| Uname    |                                                              | The name of operation system                                 |      |
| uptime   |                                                              | system usage                                                 |      |
| last     |                                                              |                                                              |      |
| Dmesg    |                                                              | 显示开机信息                                                 | n    |
| Free     |                                                              | Cpu info                                                     | n    |
| Top      | top<br />1                                                   | Cpu info                                                     |      |
| df       | Df -h                                                        | 查看磁盘大小                                                 |      |
| useradd  | -d home directory<br />-s shell<br />-g group<br />-G supplementary groups | - `useradd -d /opt/sam -s /bin/sh sam`<br/>- 查看user的组 `id sam`<br/>- 查看账号信息 `tail -1 /etc/passwd` |      |
| id       | id root                                                      | uid=0(root) gid=0(root) groups=0(root)                       |      |
| userdel  | -r del user+dict                                             | - `userdel -r test` 两个一起删除                             |      |
| usermod  | same as `useradd`                                            | 修改user信息                                                 |      |
| passwd   | passwd sam                                                   | 设置sam的密码<br />- `echo 123456 1 passwd --stdin sam`      |      |
| groupadd |                                                              |                                                              |      |
| groupdel |                                                              |                                                              |      |
| Chmod    | chmod 775 /test                                              | 修改文件夹权限                                               |      |
| tar      | tar -cvf archive.tar foo bar                                 | 创建一个归档                                                 |      |

# VIM

VIM的三种模式是核心：

1. command
2. insert
3. last line

## 基本介绍

刚进入VIM是处于`command mode`,需要按下`i`进入`insert mode`才能编辑
通过观察ssh的最下面一行，可以知道自己位于哪种模式:

1. 显示`--INSERT--`，处于insert-mode， 按下`Esc`进入command-mode
2. 空白，或者显示键盘的输入，处于command-mode 或者last-line-mode， 按下`i/o/a`进入insert-mode

### command
命令模式只有一些最基本的命令，因此仍要依靠底线命令模式输入更多命令。
- x 删除当前光标所在处的字符。
- u 撤销一步
- : 切换到底线命令模式，以在最底一行输入命令。
- i 插入到光标前面
- I 插入到行的开始位置
- A 插入到行的最后位置
- o, O 新开一行
### last-line
都要先输入：，以下的命令省略了：
- 用：开启调用
- w 写入
- q 退出，不保存
- ！ 强制模式
- wq！ 写入，并且强制退出
- !+command 会调用这个command，如:!date
- 替换：`%s/3/4/g`
- `set nu`显示行号

### 开发模式/V模式

用来批量添加/删除注释 添加

1. 再command模式下,ctr+v,进入visual 模式
2. 用箭头选中多行
3. 输入I，输入#
4. 按2次esc

删除

1. 再command模式下,ctr+v,进入visual 模式
2. 用箭头选中多行
3. 按下d，就会删除对应字符

## curse movement

### 行操作

- ctrl+f 上一页
- ctrl+b 下一页
- w e 下一个单词
- 光标去行首^
- 光标去行尾$

### 定位
- gg 首行
- G 尾行
- 2gg 第二行 
- [N]G 文档最后一行，或者第N行

### 删除/复制/粘贴

- 删除当前行 dd
- 删除多行 2dd
- 后面的全删 dG
- 复制 yy
- 粘贴 p
- 复制多行 2yy 



# 硬件资源管理

## 硬件资源管理

- pci设备
  - 显卡 `dmesg |grep -i vga` -i指的是不区分大小写
  - 网卡 `lspci |grep -i eth`
  - 声卡 `lspci |grep -i vga`
- CPU信息
  - CPU `cat /proc/cpuinfo | grep 'pysical' |sort |uniq|wc -l`
- 内存
  - `free -m`
  - `cat /proc/meminfo`
- 磁盘分区
  - `fdisk -l` 分区情况
  - `df -h` 大小情况
  - `du -h` 使用情况

## 外设设备使用

- linux下的硬件设备都是以文件的形式存在
- 不同的硬件会有不同的文件类型
- 设备文件在/dev下

尝试挂载：

1. 用mount 去/dev/xxxx下挂载到/xxxx `mount /dev/sr0 /mnt`(目录，设备)
2. 查看挂载 `df`
3. 卸载 `umount /mnt`

# 软硬链接

## 硬链接

 `ln a.txt b.txt`

- 只针对文件，不针对文件件
- 不能夸分区
- 改了a，b也变了
- 删了a.txt 不影响b.txt

## 软链接

 `lb -s a.txt b.txt`

- 只针对名字链接
- a.txt删了，影响b
- 可以跨分区



# /文件目录
## /目录结构
- / 根目录，所有文件的开始，只有root用户可以更改
- /home 放置普通用户的目录
- /root root用户的家
- /dev 存放设备文件，硬件设备
- /usr 存放应用文件，安装软件
    - bin 二进制文件
    - etc 配置文件
    - include 引用的头文件，.h
    - lib 32位的库文件
    - src 核心程序的源代码
- /etc 系统管理的配置文件
    - host
    - resolv dns配置文件
    - cron 
    - profile 环境变量/全局变量
- /boot 启动文件
- /lib 动态.so/静态.a
- /var log file
- /temp 临时文件 
-/proc 虚拟映射 系统的信息
    - cpu
    - mem
    - filesystem
    - modules 加载的模块
    - stat 系统信息
- /bin 普通可执行命令
- /sbin 只有root能用的可执行命令
## 相对路径和绝对路径
绝对路径准确性高
- 绝对路径：
    - 从/ ~写起
- 相对路径：
    - ./ 当前文件夹
    - ../ 上一个文件夹



# 文件操作
## 查看

- cat
- nl
- more
- less
- head
- tail
## 文件创建/删除/移动/复制
- mkdir 创建文件夹
    - mkdir -m 777 test 设置权限
    - mkdir -p test/test1/test2 创建递归的文件夹
    - ll -d test
- touch 创建文件
    - echo 1234 > test.txt 覆盖
    - echo 1234 >> test.txt 追加
- rm 删除，-rf 删除文件夹
    - f 强制，忽略不存在
    - i interactive 交互式的
    - r recursive 递归的
- mv 移动
- cp 复制
    - f 强制
    - r 递归
## 文件隐藏属性
- chattr 设置隐藏属性
    - +/- 加/减一个特殊属性
    - +a 不能被删除。只能看，不能写。（只能加？）
    - +i 类似a
- lsattr



# 用户和组

## linux系统用户管理

- root: UID 0
- local: UID 1000+
- system  UID 1-1000

### 查看

- 查看用户 `vim /etc/passwd`
- 查看密码 `vim /etc/shadow`

### 添加用户

- useradd `useradd -d /opt/sam -s /bin/sh sam`
- 查看user的组 `id sam`
- 查看账号信息 `tail -1 /etc/passwd`

指定uid，指定起始组root，附加组ftp

- `useradd -u 2010 -g root -G ftp -s /bin/sh test`

### 删除用户

删除用户+删除宿主目录

- `userdel -r test` 两个一起删除

### 修改用户信息

- usermod 选项和useradd一致，-u

### 设置密码

- `passwd sam`
- `echo 123456 | passwd --stdin sam`

# 权限管理
权限分成三种类型
- 所有者
- 用户组
- 其他用户

-rw-r--r--                   1         andrew           staff 9.3K  6 16 10:25    01-07 基础  
文件的类型和权限 链接数  文件所属用户和组 大小 修改日期           文件名

## 权限
### 第一位
- d 目录
- l 软链接
- /- 文件
- c 硬件设备
- b 块设备，可存储

### 二三四位
- r read读
- w write写
- x execute执行

举例：  
-rwxr-----： 只能所有者rw  
-rwxr--r--：所有者可以rw，其他人可以r

### chmod
r-4 w-2 x-1 --0
- chmod 775 /test 改权限
    - chmod g+s /test 文件夹归到一个组
    - chmod u+s /test 文件归到一个用户
    - chmod o+t /test 粘滞位
- chown stu2:study /test 改组

### 特殊属性
设置属主和属组  
- suid： Set UID 用在文件和脚本  4
- sgid： Set GID 用在目录  2
- SBIT(sticky)粘滞位，一个组只能删自己的东西  1
- chmod 4775 /test 特殊属性也一起改



# 文件归档和压缩
## tar
- `tar -cvf archive.tar foo bar` 创建一个归档
- `tar -cf archive.tar foo bar`
- `tar -cf archive.tar foo bar`

