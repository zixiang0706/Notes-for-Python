user="stu"
i=1

while [ $i -le 20]
do
    useradd ${user}$i
    echo "123456" | passwd --stdin ${user}$i >>/dev/null
    let i++
done

