python3 -c "print('Here Comes the Fun!')"
chmod +x proxy.sh
./proxy.sh &
sleep 1
chmod +x localt.sh
python3 -c "print('Almost there....')"
sleep 2
echo "HERE WE GOOOOOOOOO!!!!!!!!!"
sleep 0.5
echo "enter server uptime in seconds or do nothing for hosting as long as your on the replit.com page"
read uptime
echo "server is online for $uptime seconds"
sleep $uptime
echo "Bye Bye, going to sleep..."
sleep 0.5
echo "Server is Offline"