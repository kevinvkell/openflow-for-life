sudo mn --mac --custom ~/openflow-for-life/Subnet.py --topo direct --pre ~/openflow-for-life/setup_direct.sh --controler remote,ip=0.0.0.0

h1 ~/D-ITG-2.8.1-r1023/bin/ITGRecv
h2 ~/D-ITG-2.8.1-r1023/bin/ITGRecv
h3 ~/D-ITG-2.8.1-r1023/bin/ITGRecv
h4 ~/D-ITG-2.8.1-r1023/bin/ITGRecv

h1 ~/D_ITG-2.8.1-r1023/bin/ITGSend -T UDP -a 192.168.12.4 -c 100 -C 10 -t 15000 -l sender.log -x receiver.log
h2 ~/D_ITG-2.8.1-r1023/bin/ITGSend -T UDP -a 192.168.12.3  -c 100 -C 10 -t 15000 -l sender.log -x receiver.log
h3 ~/D_ITG-2.8.1-r1023/bin/ITGSend -T UDP -a 192.168.12.1 -c 100 -C 10 -t 15000 -l sender.log -x receiver.log
h4 ~/D_ITG-2.8.1-r1023/bin/ITGSend -T UDP -a 192.168.12.2 -c 100 -C 10 -t 15000 -l sender.log -x receiver.log
