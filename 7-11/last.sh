#! /bin/sh

queryString=""
for var in "$@"
do
    queryString+=" $var"
done
# echo $queryString
while true
do 
	# print coin category and price followed by current time and append them to text file
	python scrape.py $queryString | tee -a coin_prices.txt
	echo $(date) | tee -a coin_prices.txt
	# wait 30 seconds
	sleep 30
done

