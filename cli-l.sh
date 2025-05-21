#!/bin/bash
files=("srv-dhcp-dns-ftp-kys-itp.txt" "PrSO.txt")
$tmp=0
tmp=0
clear
for i in ${files[@]}; do
    tmp=$((tmp + 1))
    echo "$tmp. $i"
done

read -p "number> " num
echo ${files[$(($num - 1))]}

curl -so- "https://ksawix0.github.io/WebPage/cli-docs/${files[$(($num - 1))]}" 