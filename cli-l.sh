#!/bin/bash
web="bash <(wget -qO- https://ksawix0.github.io/WebPage/cli-l.sh)"
files=("srv-dhcp-dns-ftp-kys-itp.txt" "PrSO.txt" "pk2.txt")
$tmp=0
$num=1
tmp=0
clear
for i in ${files[@]}; do
    tmp=$((tmp + 1))
    echo "$tmp. $i"
done
echo "----------------------"
read -p "number> " num;
num=$((num - 1))
echo ${files[num]}
echo "----------------------"
curl -so- "https://ksawix0.github.io/WebPage/cli-docs/${files[$num]}" | less