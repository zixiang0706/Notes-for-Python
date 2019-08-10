# Java

一个Java源码只能定义一个public类型的class，并且class名称和文件名要完全一致；

使用javac可以将.java源码编译成.class字节码；

使用java可以运行一个已编译的Java程序，参数是类名。
##cheatsheet
1. java函数传递的是指针，所以函数的传参是array的时候要小心
2. 构造一个函数：
    - declare: public class Name{ }
    - field: public int cnt;
    - constructor: public Name(int cnt, int cnt2){this.cnt=cnt}
    - method: public void methodName(int arg){something;}
    - abstraction: public abstract void abstractionName(int arg);
    - override: @override  public void abstractionName(int arg){something;}
    - override and overload: the method of child class is fully same as super class 
    - 继承用extend，interface用implement
    - public：公有 private：完全私有 protected：子类可以用  final:不可以修改类型
    - finial: class不能被继承，method不能被改写，field不能被重新赋值
    - 一个class只能继承一个class，但是可有多个interface
    - static method: the method of class, only contain static field
    - static field: the field of class, all instance of this class share one


3. architecture
    - 如果不确定是否需要public，就不声明为public，即尽可能少地暴露对外的字段和方法。
    - 把方法定义为package权限有助于测试，因为测试类和被测试类只要位于同一个package，测试代码就可以访问被测试类的package权限方法。
    - 一个.java文件只能包含一个public类，但可以包含多个非public类。如果有public类，文件名必须和public类的名字相同。
4. ctr+shift+f  快速代码优化


##变量
基本类型变量
引用类型变量
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
`for (int i=0; i<ns.length; i++) {
    System.out.println("i = " + i + ", ns[i] = " + ns[i]);
    sum = sum + ns[i];
}`

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

#### 参数传递
结论：基本类型参数的传递，是调用方值的复制。双方各自的后续修改，互不影响。
还有传递应用参数的
和传入数据的可变不可变类型有关系，起始传递进去的是地址
#### 构造方法 constructor
实例在创建时通过new操作符会调用其对应的构造方法，构造方法用于初始化实例；
没有定义构造方法时，编译器会自动创建一个默认的无参数构造方法；
可以定义多个构造方法，编译器根据参数自动判断；
可以在一个构造方法内部调用另一个构造方法，便于代码复用。


指的是在构造方法的时候，也初始化field
Person p = new Person("Xiao Ming", 15);
class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }
}

#### 方法重载overload
如果有一系列方法，它们的功能都是类似的，只有参数有所不同，那么，可以把这一组方法名做成同名方法
这种方法名相同，但各自的参数不同，称为方法重载（Overload）。
注意：方法重载的返回值类型通常都是相同的。
方法重载的目的是，功能类似的方法使用同一名字，更容易记住，因此，调用起来更简单。

#### 继承 inherit
Java使用extends关键字来实现继承：
class Student extends Person {
在OOP的术语中，我们把Person称为超类（super class），父类（parent class），基类（base class），把Student称为子类（subclass），扩展类（extended class）。
Java只允许一个class继承自一个类，因此，一个类有且仅有一个父类。只有Object特殊，它没有父类。
继承有个特点，就是子类无法访问父类的private字段或者private方法。例如，Student类就无法访问Person类的name和age字段：
用protected修饰的字段可以被子类访问：
super关键字表示父类（超类）
---
在构建的时候，没有用super，编译器会自己加个没有参数的super（）
---
子类不会继承任何父类的构造方法。子类默认的构造方法是编译器自动生成的，不是继承的。

这种把一个子类类型安全地变为父类类型的赋值，被称为向上转型（upcasting）。
不能把父类变为子类，因为子类功能比父类多，多的功能无法凭空变出来。
因此，向下转型很可能会失败。失败的时候，Java虚拟机会报ClassCastException。
为了避免向下转型出错，Java提供了instanceof操作符，可以先判断一个实例究竟是不是某种类型：
Student s = new Student();
System.out.println(s instanceof Person); // true
System.out.println(s instanceof Student); // true

#### 分区继承和组合
具有has关系不应该使用继承，而是使用组合，即Student可以持有一个Book实例
    class Student extends Person {
    protected Book book;
    protected int score;
}因此，继承是is关系，组合是has关系。

### 多态 polymorphic
在继承关系中，子类如果定义了一个与父类方法签名完全相同的方法，被称为覆写（Override）
Override和Overload不同的是，如果方法签名如果不同，就是Overload，Overload方法是一个新方法；如果方法签名相同，并且返回值也相同，就是Override。
加上@Override可以让编译器帮助检查是否进行了正确的覆写。希望进行覆写，但是不小心写错了方法签名，编译器会报错。
----
Java的实例方法调用是基于运行时的实际类型的动态调用，而非变量的声明类型。
多态是指，针对某个类型的方法调用，其真正执行的方法取决于运行时期实际类型的方法
所以，多态的特性就是，运行期才能动态决定调用的子类方法。对某个类型调用某个方法，执行的实际方法可能是某个子类的覆写方法
----
用final修饰的方法不能被Override
如果一个类不希望任何其他类继承自它，那么可以把这个类本身标记为final。用final修饰的类不能被继承
对于一个类的实例字段，同样可以用final修饰。用final修饰的字段在初始化后不能被修改

#### 重新object
因为所有的class最终都继承自Object，而Object定义了几个重要的方法：

toString()：把instance输出为String；
equals()：判断两个instance是否逻辑相等；
hashCode()：计算一个instance的哈希值。

#### 抽象类

如果父类的方法本身不需要实现任何功能，仅仅是为了定义方法签名，目的是让子类去覆写它，那么，可以把父类的方法声明为抽象方法：
如果一个class定义了方法，但没有具体执行代码，这个方法就是抽象方法，抽象方法用abstract修饰。

因为无法执行抽象方法，因此这个类也必须申明为抽象类（abstract class）。

使用abstract修饰的类就是抽象类。我们无法实例化一个抽象类：

Person p = new Person(); // 编译错误
因为抽象类本身被设计成只能用于被继承，因此，抽象类可以强迫子类实现其定义的抽象方法，否则编译会报错。因此，抽象方法实际上相当于定义了“规范”。

#### 面向抽象编程
这种尽量引用高层类型，避免引用实际子类型的方式，称之为面向抽象编程。

面向抽象编程的本质就是：

上层代码只定义规范（例如：abstract class Person）；

不需要子类就可以实现业务逻辑（正常编译）；

具体的业务逻辑由不同的子类实现，调用者并不关心。
大家都是引用共有属性，所以可以面向抽象编程，不用关心子类
#### 接口 interface
如果一个抽象类没有字段，所有方法全部都是抽象方法：就可以把该抽象类改写为接口：interface。
interface Person {
    void run();
    String getName();
}
**它连字段都不能有**。因为接口定义的所有方法默认都是public abstract的，所以这两个修饰符不需要写出来（写不写效果都一样）。
当一个具体的class去实现一个interface时，需要使用implements关键字
default方法，那么子类就不必全部修改

####静态方法和字段
用static修饰的字段
对于静态字段，无论修改哪个实例的静态字段，效果都是一样的：所有实例的静态字段都被修改了，原因是静态字段并不属于实例：
因此，不推荐用实例变量.静态字段去访问静态字段，因为在Java程序中，实例对象并没有静态字段。在代码中，实例对象能访问静态字段只是因为编译器可以根据实例类型自动转换为类名.静态字段来访问静态对象。

有静态字段，就有静态方法。用static修饰的方法称为静态方法。
---
因为静态方法属于class而不属于实例，因此，静态方法内部，无法访问this变量，也无法访问实例字段，它只能访问静态字段
---
interface是可以有静态字段的，并且静态字段必须为final类型：
public interface Person {
    // 编译器会自动加上public statc final:
    int MALE = 1;
    int FEMALE = 2;
}

#### 包 package
package ming; // 申明包名ming
public class Person {
}
没有定义包名的class，它使用的是默认包，非常容易引起名字冲突，因此，不推荐不写包名的做法。

位于同一个包的类，可以访问包作用域的字段和方法。不用public、protected、private修饰的字段和方法就是包作用域

// 导入mr.jun包的所有class:
import mr.jun.`*`;
还有一种import static的语法，它可以导入可以导入一个类的静态字段和静态方法：


// Main.java
package test;
import java.text.Format;
public class Main {
    public static void main(String[] args) {
        java.util.List list; // ok，使用完整类名 -> java.util.List
        Format format = null; // ok，使用import的类 -> java.text.Format
        String s = "hi"; // ok，使用java.lang包的String -> java.lang.String
        System.out.println(s); // ok，使用java.lang包的System -> java.lang.System
        MessageFormat mf = null; // 编译错误：无法找到MessageFormat: MessageFormat cannot be resolved to a type
    }
}

因此，编写class的时候，编译器会自动帮我们做两个import动作：
- 默认自动import当前package的其他class；
- 默认自动import java.lang.`*`。

最后，包作用域是指一个类允许访问同一个package的没有public、private修饰的class，以及没有public、protected、private修饰的字段和方法。
注意，包名必须完全一致，包没有父子关系，com.apache和com.apache.abc是不同的包

在方法内部定义的变量称为局部变量，局部变量作用域从变量声明处开始到对应的块结束。方法参数也是局部变量。
使用局部变量时，应该尽可能把局部变量的作用域缩小，尽可能延后声明局部变量。

#### classPath
java -classpath .;C:\work\project1\bin;C:\shared abc.xyz.Hello
在IDE中运行Java程序，IDE自动传入的-cp参数是当前工程的bin目录和引入的jar包。

jar包就是用来干这个事的，它可以把package组织的目录层级，以及各个目录下的所有文件（包括.class文件和其他文件）都打成一个jar文件

##核心类
### String
结论：两个字符串比较，必须总是使用equals()方法。
要忽略大小写比较，使用equalsIgnoreCase()方法。
"Hello".contains("ll"); // true
"Hello".indexOf("l"); // 2
"Hello".lastIndexOf("l"); // 3
"Hello".startsWith("He"); // true
"Hello".endsWith("lo"); // true
"Hello".substring(2); // "llo"
"Hello".substring(2, 4); "ll"

#### trim
使用trim()方法可以移除字符串首尾空白字符。空白字符包括空格，\t，\r，\n：
"  \tHello\r\n ".trim(); // "Hello"
另一个strip()方法也可以移除字符串首尾空白字符。它和trim()不同的是，类似中文的空格字符\u3000也会被移除：

String还提供了isEmpty()和isBlank()来判断字符串是否为空和空白字符串：

#### replace
String s = "hello";
s.replace('l', 'w'); // "hewwo"，所有字符'l'被替换为'w'
s.replace("ll", "~~"); // "he~~o"，所有子串"ll"被替换为"~~"

String s = "A,,B;C ,D";
s.replaceAll("[\\,\\;\\s]+", ","); // "A,B,C,D"

#### split
要分割字符串，使用split()方法，并且传入的也是正则表达式：
String s = "A,B,C,D";
String[] ss = s.split("\\,"); // {"A", "B", "C", "D"}

#### join
拼接字符串使用静态方法join()，它用指定的字符串连接字符串数组：

String[] arr = {"A", "B", "C"};
`String s = String.join("***", arr); // "A***B***C"`

#### valueChange
要把任意基本类型或引用类型转换为字符串，可以使用静态方法valueOf()。这是一个重载方法，编译器会根据参数自动选择合适的方法：
String.valueOf(123); // "123"
String.valueOf(45.67); // "45.67"
String.valueOf(true); // "true"
String.valueOf(new Object()); // 类似java.lang.Object@636be97c

要把字符串转换为其他类型，就需要根据情况。例如，把字符串转换为int类型：
int n1 = Integer.parseInt("123"); // 123
int n2 = Integer.parseInt("ff", 16); // 按十六进制转换，255

要特别注意，Integer有个getInteger(String)方法，它不是将字符串转换为int，而是把该字符串对应的系统变量转换为Integer：
Integer.getInteger("java.version"); // 版本号，11

#### char
String和char[]类型可以互相转换，方法是：

char[] cs = "Hello".toCharArray(); // String -> char[]
String s = new String(cs); // char[] -> String

###字符编码
始终牢记：Java的String和char在内存中总是以Unicode编码表示。
ASCII--Unicode-utf-8
一个字节  两个字节  不定长
UTF-8编码的另一个好处是容错能力强。如果传输过程中某些字符出错，不会影响后续字符，因为UTF-8编码依靠高字节位来确定一个字符究竟是几个字节，它经常用来作为传输编码。
byte[] b2 = "Hello".getBytes("UTF-8"); // 按UTF-8编码转换
byte[] b2 = "Hello".getBytes("GBK"); // 按GBK编码转换
byte[] b3 = "Hello".getBytes(StandardCharsets.UTF_8); // 按UTF-8编码转换

byte[] b = ...
String s1 = new String(b, "GBK"); // 按GBK转换
String s2 = new String(b, StandardCharsets.UTF_8); // 按UTF-8转换

#### StringBuilder
就是为了减少拼接string生成过多的temp variable，所以可以使用StringBuilder
为了能高效拼接字符串，Java标准库提供了StringBuilder，它是一个可变对象，可以预分配缓冲区，这样，往StringBuilder中新增字符时，不会创建新的临时对象：
#### StringJoiner
可以指定加入元素的分隔
慢着！用StringJoiner的结果少了前面的"Hello "和结尾的"!"！遇到这种情况，需要给StringJoiner指定“开头”和“结尾”：
String还提供了一个静态方法join()，这个方法在内部使用了StringJoiner来拼接字符串，在不需要指定“开头”和“结尾”的时候，用String.join()更方便：
String[] names = {"Bob", "Alice", "Grace"};
var s = String.join(", ", names);
#### 包装类型 wrapper class
就是把基本类型转为一个class
java的数据类型有基本类型和引用类型
引用类型可以是空，但是基本类型不能是null
比如，想要把int基本类型变成一个引用类型，我们可以定义一个Integer类，它只包含一个实例字段int，这样，Integer类就可以视为int的包装类（Wrapper Class）：

这种直接把int变为Integer的赋值写法，称为自动装箱（Auto Boxing），反过来，把Integer变为int的赋值写法，称为自动拆箱（Auto Unboxing）。

所有的wrapper class都是不变类
对两个Integer实例进行比较要特别注意：绝对不能用==比较，因为Integer是引用类型，必须使用equals()比较：
Java和python一样，也会对小int做内存优化

Integer n = Integer.valueOf(100);

#### 静态工厂方法
我们把能创建“新”对象的静态方法称为静态工厂方法。Integer.valueOf()就是静态工厂方法，它尽可能地返回缓存的实例以节省内存

### JavaBean
在Java中，有很多class的定义都符合这样的规范：
- 若干private实例字段；
- 通过public方法来读写实例字段。

简单地说：bean就是Java的set和get方法
我们通常把一组对应的读方法（getter）和写方法（setter）称为属性（property）
- 对应的读方法是String getName()
- 对应的写方法是setName(String)

### 枚举 enumerate
Weekday day = Weekday.SUN;
        if (day == Weekday.SAT || day == Weekday.SUN) {
            System.out.println("Work at home!");
        } else {
            System.out.println("Work at office!");
        }
enum Weekday {
    SUN, MON, TUE, WED, THU, FRI, SAT;
}

通过enum定义的枚举类，和其他的class有什么区别？
答案是没有任何区别。enum定义的类型就是class，只不过它有以下几个特点：
定义的enum类型总是继承自java.lang.Enum，且无法被继承；
只能定义出enum的实例，而无法通过new操作符创建enum的实例；
定义的每个实例都是引用类型的唯一实例；
可以将enum类型用于switch语句。

## Exception
Java使用异常来表示错误，并通过try ... catch捕获异常
Java的异常是class，并且从Throwable继承；

而Exception则是运行时的错误，它可以被捕获并处理。
- RuntimeException以及它的子类；
- 非RuntimeException（包括IOException、ReflectiveOperationException等等）

Java规定：
- 必须捕获的异常，包括Exception及其子类，但不包括RuntimeException及其子类，这种类型的异常称为Checked Exception。
- 不需要捕获的异常，包括Error及其子类，RuntimeException及其子类。

在方法定义的时候，使用throws Xxx表示该方法可能抛出的异常类型。调用方在调用的时候，必须强制捕获这些异常
可以使用多个catch语句，每个catch分别捕获对应的Exception及其子类。JVM在捕获到异常后，会从上到下匹配catch语句，匹配到某个catch后，执行catch代码块，然后不再继续匹配。
简单地说就是：多个catch语句只有一个能被执行。
finally语句块保证有无错误都会执行
Example:
catch (IOException | NumberFormatException e)
		try {
			int c = stringToInt(a);
			int d = stringToInt(b);
			System.out.println(c * d);
		}catch (Exception e) {
			System.out.println(e);
			e.printStackTrace();
			System.out.println("please debug");
		}finally {
			System.out.println("always print");
		}

### 抛出异常
   throw new NullPointerException();
   因此，在catch中抛出异常，不会影响finally的执行。JVM会先执行finally，然后抛出异常
这说明finally抛出异常后，原来在catch中准备抛出的异常就“消失”了，因为只能抛出一个异常。没有被抛出的异常称为“被屏蔽”的异常（Suppressed Exception）。

### customer define exception
Exception
│
├─ RuntimeException
│  │
│  ├─ NullPointerException
│  │
│  ├─ IndexOutOfBoundsException
│  │
│  ├─ SecurityException
│  │
│  └─ IllegalArgumentException
│     │
│     └─ NumberFormatException
│
├─ IOException
│  │
│  ├─ UnsupportedCharsetException
│  │
│  ├─ FileNotFoundException
│  │
│  └─ SocketException
│
├─ ParseException
│
├─ GeneralSecurityException
│
├─ SQLException
│
└─ TimeoutException

public class BaseException extends RuntimeException { }
public class UserNotFoundException extends BaseException { }
自定义的BaseException应该提供多个构造方法：

### assert
assert x >= 0 : "x must >= 0";
这样，断言失败的时候，AssertionError会带上消息x must >= 0，更加便于调试
Java断言的特点是：断言失败时会抛出AssertionError，导致程序结束退出。因此，断言不能用于可恢复的程序错误，只应该用于开发和测试阶段。

## 反射 reflection
Java的反射是指程序在运行期可以拿到一个对象的所有信息。
所以，反射是为了解决在运行期，对某个实例一无所知的情况下，如何调用其方法。

无继承关系的数据类型无法赋值：
每加载一种class，JVM就为其创建一个Class类型的实例，并关联起来
一个Class实例包含了该class的所有完整信息：
这种通过Class实例获取class信息的方法称为反射（Reflection）。

方法一：直接通过一个class的静态变量class获取：
Class cls = String.class;

方法二：如果我们有一个实例变量，可以通过该实例变量提供的getClass()方法获取：
String s = "Hello";
Class cls = s.getClass();

方法三：如果知道一个class的完整类名，可以通过静态方法Class.forName()获取：
Class cls = Class.forName("java.lang.String");

用instanceof不但匹配当前类型，还匹配当前类型的子类。而用==判断class实例可以精确地判断数据类型，但不能作子类型比较。

注意到数组（例如String[]）也是一种Class，而且不同于String.class，它的类名是[Ljava.lang.String。此外，JVM为每一种基本类型如int也创建了Class，通过int.class访问。

动态加载class的特性对于Java程序非常重要。利用JVM动态加载class的特性，我们才能在运行期根据条件加载不同的实现类。

###访问field
获得field的所有属性
Field f = String.class.getDeclaredField("value");
f.getName(); // "value"
f.getType(); // class [B 表示byte[]类型
int m = f.getModifiers();
Modifier.isFinal(m); // true
Modifier.isPublic(m); // false
Modifier.isProtected(m); // false
Modifier.isPrivate(m); // true
Modifier.isStatic(m); // false

获得值
        Object p = new Person("Xiao Ming");
        Class c = p.getClass();
        Field f = c.getDeclaredField("name");
        Object value = f.get(p);
        System.out.println(value); // "Xiao Ming"

而反射是一种非常规的用法，使用反射，首先代码非常繁琐，其次，它更多地是给工具或者底层框架来使用，目的是在不知道目标实例任何信息的情况下，获取特定字段的值。

###调用方法
Method getMethod(name, Class...)：获取某个public的Method（包括父类）
Method getDeclaredMethod(name, Class...)：获取当前类的某个Method（不包括父类）
Method[] getMethods()：获取所有public的Method（包括父类）
Method[] getDeclaredMethods()：获取当前类的所有Method（不包括父类）


一个Method对象包含一个方法的所有信息：
getName()：返回方法名称，例如："getScore"；
getReturnType()：返回方法返回值类型，也是一个Class实例，例如：String.class；
getParameterTypes()：返回方法的参数类型，是一个Class数组，例如：{String.class, int.class}；
getModifiers()：返回方法的修饰符，它是一个int，不同的bit表示不同的含义。

对Method实例调用invoke就相当于调用该方法，invoke的第一个参数是对象实例，即在哪个实例上调用该方法，后面的可变参数要与方法参数一致，否则将报错。
Integer n = (Integer) m.invoke(null, "12345");
Method.setAccessible(true)





