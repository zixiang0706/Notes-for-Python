
# 文件归档和压缩

> **tar命令详解**
>
> -c: 建立压缩档案
>
> -x：解压
>
> -t：查看内容
>
> -r：向压缩归档文件末尾追加文件
>
> -u：更新原压缩包中的文件
>
> 这五个是独立的命令，压缩解压都要用到其中一个，可以和别的命令连用但只能用其中一个。
>
> 下面的参数是根据需要在压缩或解压档案时可选的。
>
> -z：有gzip属性的
>
> -j：有bz2属性的
>
> -Z：有compress属性的
>
> -v：显示所有过程
>
> -O：将文件解开到标准输出
>
> 参数-f是必须的
>
> -f: 使用档案名字，切记，这个参数是最后一个参数，后面只能接档案名。

## tar归档

- `tar -cf archive.tar foo bar` 创建一个归档
- `tar -xf archive.tar`解压一个归档	
- `tar -xf archive.tar -C [path]`解压一个归档到指定目录
- `du -sh [file]`显示文件的大小

## 压缩
格式有gz，bz2，zip

### gz
- `tar -zcf archive.tar.gz foo bar` 创建一个压缩的归档
- `tar -xzf archive.tar.gz -C [path]` 解压压缩的归档

### bz2
- `tar -jcf archive.tar.bz2 foo bar` 创建一个压缩的归档
- `tar -jxf archive.tar.bz2 -C [path]` 解压压缩的归档

### zip
- `zip -r a.zip [path]`
- `unzip a.zip -d [path]`

## file
- file [1.txt]: 确定文件类型
