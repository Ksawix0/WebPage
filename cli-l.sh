#!/bin/bash
files=("srv-dhcp-dns-ftp-kys-itp.txt" "PrSO.txt")
$tmp=0
$num=1
tmp=0
clear
for i in ${files[@]}; do
    echo "$tmp. $i"
    tmp=$((tmp + 1))
done
echo "----------------------"
read -p "number> " num
echo ${files[num]}
echo "----------------------"
curl -so- "https://ksawix0.github.io/WebPage/cli-docs/${files[$num]}" 