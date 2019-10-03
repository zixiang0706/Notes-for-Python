ip=$(cat file)
for i in $ip
do 
    ping -c 2 -i 0.2 
    if [$? -eq 0]
    then
        echo "$i host is up"
    else
        echo "$i host is down"
    fi
don
