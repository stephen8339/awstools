#!/bin/sh
python /data/aws/aws_ec2_info.py > /data/aws/ipinfotmp
echo 'Name|Status|PublicDnsName|PublicIP|PrivateDnsName|PrivateIP' > /data/aws/ipinfo
awk -F , -vOFS=' | ' '{print $1,$7,$6,$10,$32}' /data/aws/ipinfotmp |  sed "s/u'\|{\|'\|}\|PublicDnsName\|\[\|Association\|PublicIp\|PrivateIpAddresses\|PrivateDnsName\|]\|PrivateIpAddress\|Status\|://g" >> /data/aws/ipinfo
rm -rf /data/aws/ipinfotmp
cat /data/aws/ipinfo
echo '127.0.0.1 A-Management-JP-172.31.30.109' > /etc/hosts
awk -F'|' '{print $6,$1}' /data/aws/ipinfo | sed "s/PublicDnsName\|PrivateIP\|Name//g" >> /etc/hosts
