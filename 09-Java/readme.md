# Java

一个Java源码只能定义一个public类型的class，并且class名称和文件名要完全一致；

使用javac可以将.java源码编译成.class字节码；

使用java可以运行一个已编译的Java程序，参数是类名。

##格式
类
    方法

ctr+shift+f  快速代码优化
##变量
基本类型变量
引用类型变量·
基本数据类型是CPU可以直接进行运算的类型。Java定义了以下几种基本数据类型：
- 整数类型：byte，short，int，long
- 浮点数类型：float，double
- 字符类型：char
- 布尔类型：boolean

15=0xf＝0b1111
对于float类型，需要加上f后缀

注意char类型使用单引号'，且仅有一个字符，要和双引号"的字符串类型区分开。
定义变量的时候，如果加上final修饰符，这个变量就变成了常量：
常量在定义时进行初始化后就不可再次赋值，再次赋值会导致编译错误。
根据习惯，常量名通常全部大写。

因此，使用var定义变量，仅仅是少写了变量类型而已。
StringBuilder sb = new StringBuilder();
var sb = new StringBuilder();

在Java中，多行语句用{ }括起来。很多控制语句，例如条件判断和循环，都以{ }作为它们自身的范围，例如：
而在语句块中定义的变量，它有一个作用域，就是从定义处开始，到语句块结束。超出了作用域引用这些变量，编译器会报错

## 运算
/ 整除
% 求余
如果对一个负数进行右移，最高位的1不动，结果仍然是一个负数：
还有一种不带符号的右移运算，使用>>>，它的特点是符号位跟着动，因此，对一个负数进行>>>右移，它会变成正数，原因是最高位的1变成了0：

在Java的计算表达式中，运算优先级从高到低依次是：
()
! ~ ++ --
* / %
+ -
<< >> >>>
&
|
`+= -= *= /=`
记不住也没关系，只需要加括号就可以保证运算的优先级正确。

在运算过程中，如果参与运算的两个数类型不一致，那么计算结果为较大类型的整型。例如，short和int计算，结果总是int，原因是short首先自动被转型为int：

在一个复杂的四则运算中，两个整数的运算不会出现自动提升的情况

整数运算在除数为0时会报错，而浮点数运算在除数为0时，不会报错，但会返回几个特殊值：
NaN表示Not a Number
Infinity表示无穷大
-Infinity表示负无穷大

强制转型
可以将浮点数强制转型为整数。在转型时，浮点数的小数部分会被丢掉。如果转型后超过了整型能表示的最大范围，将返回整型的最大值
如果要进行四舍五入，可以对浮点数加上0.5再强制转型：

Java还提供一个三元运算符b ? x : y，它根据第一个布尔表达式的结果，分别返回后续两个表达式之一的计算结果

在Java中，字符和字符串是两个不同的类型。
它们都占用两个字节。要显示一个字符的Unicode编码，只需将char类型直接赋值给int类型即可：
还可以直接用转义字符\u+Unicode编码来表示一个字符

如果用+连接字符串和其他数据类型，会将其他数据类型先自动转型为字符串，再连接：
注意要区分空值null和空字符串""，空字符串是一个有效的字符串对象，它不等于null。

定义一个数组类型的变量，使用数组类型“类型[]”，例如，int[]。和单个基本类型变量不同，数组变量初始化必须使用new int[5]表示创建一个可容纳5个int元素的数组。
数组所有元素初始化为默认值，整型都是0，浮点型是0.0，布尔型是false；
数组一旦创建后，大小就不可改变。
要访问数组中的某一个元素，需要使用索引。数组索引从0开始，例如，5个元素的数组，索引范围是0~4。
可以修改数组中的某一个元素，使用赋值语句，例如，ns[1] = 79;。
可以用数组变量.length获取数组大小
int[] ns = new int[5];
int[] ns = new int[] { 68, 79, 91, 85, 62 };
int[] ns = { 68, 79, 91, 85, 62 };



 89 print 是没有换行的
 90 println 是print line，有换行
 91 printf 格式化输出，使用占位符%？ 可以把后面的参数格式化
 92 System.out.printf("%.4f\n", d); // 显示4位小数3.1416
 93 System.out.printf("n=%d, hex=%08x", n, n); // 注意，两个%占位符必须传入两个数
 94 占位符  说明
 95 %d  格式化输出整数
 96 %x  格式化输出十六进制整数
 97 %f  格式化输出浮点数
 98 %e  格式化输出科学计数法表示的浮点数
 99 %s  格式化字符串
100
101 ### 输入
102 import java.util.Scanner;
103 public class Main {
104     public static void main(String[] args) {
105         Scanner scanner = new Scanner(System.in); // 创建Scanner对象
106         System.out.print("Input your name: "); // 打印提示
107         String name = scanner.nextLine(); // 读取一行输入并获取字符串
108         System.out.print("Input your age: "); // 打印提示
109         int age = scanner.nextInt(); // 读取一行输入并获取整数
110         System.out.printf("Hi, %s, you are %d\n", name, age); // 格式化输出
111     }
112 }

### 判断
在Java中，判断值类型的变量是否相等，可以使用==运算符。
但是，判断引用类型的变量是否相等，==表示“引用是否相等”，或者说，是否指向同一个对象。例如，下面的两个String类型，它们的内容是相同的，但是，分别指向不同的对象，用==判断，结果为false：
要判断引用类型的变量内容是否相等，必须使用equals()方法：s1.equals(s2)

switch语句根据switch (表达式)计算的结果，跳转到匹配的case结果，然后继续执行后续语句，直到遇到break结束执行。
switch语句还可以匹配字符串。字符串匹配时，是比较“内容相等”。
switch表达式是作为Java 12的预览特性
int option = 1;
        switch (option) {
        case 1:
            System.out.println("Selected 1");
            break;
### while do-while for
while (something){
something;
}

do{
something;
}while(something);

for (int i=1; i<=100; i++) {
    sum = sum + i;
}

遍历数组
for (int i=0; i<ns.length; i++) {
    System.out.println("i = " + i + ", ns[i] = " + ns[i]);
    sum = sum + ns[i];
}

遍历数组  for each循环无法指定遍历顺序，也无法获取数组的索引
int[] ns = { 1, 4, 9, 16, 25 };
for (int n : ns) {
    System.out.println(n);
}

break会跳出当前循环，也就是整个循环都不会执行了。而continue则是提前结束本次循环，直接继续执行下次循环


### sorting
冒泡排序使用两层for循环实现排序；
交换两个变量的值需要借助一个临时变量。
可以直接使用Java标准库提供的Arrays.sort()进行排序；
对数组排序会直接修改数组本身。

#### 多维数组
        int[][] ns = {
            { 1, 2, 3, 4 },
            { 5, 6, 7, 8 },
            { 9, 10, 11, 12 }
visit specified element:
    System.out.println(ns[1][2]); // 7

print multi array:
    for (int[] arr : ns) {
    for (int n : arr) {
        System.out.print(n);
        System.out.print(', ');
    }
    System.out.println();
}

or use the lib:
        System.out.println(Arrays.deepToString(ns));

### optional argument
run javac [name]
then run java [name]

public class Main {
	public static void main(String[] args) {
		for (String arg : args) {
			if (arg.equals("-version")) {
				System.out.println("version: 1.0");
			}
			
		}
		System.out.println("Done!");
	}
}


## OOP
面向对象的基本概念，包括：
- 类 class
- 实例 instatnce
- 方法 method
- 字段 field, property

面向对象的实现方式，包括：
- 封装 package
- 继承 inherit
- 多态 polymorphic

Java语言本身提供的机制，包括：
- package
- classpath
- jar

以及Java标准库提供的核心类，包括：
- 字符串
- 包装类型
- JavaBean
- 枚举
- 常用工具类

### 基础
定义private方法的理由是内部方法是可以调用private方法的
Person ming = new Person();
注意区分Person ming是定义Person类型的变量ming，而new Person()是创建Person实例。

#### add field/method
public class Main {
    public static void main(String[] args) {
        Person ming = new Person();
        ming.setBirth(2008);
        System.out.println(ming.getAge());
    }
}

class Person {
    private String name;
    private int birth;

    public void setBirth(int birth) {
        this.birth = birth;
    }

    public int getAge() {
        return calcAge(2019); // 调用private方法
    }

    // private方法:
    private int calcAge(int currentYear) {
        return currentYear - this.birth;
    }
}
命名没有冲突的话，指的是field和其他冲突。可以省略this：name就是this.name
：





