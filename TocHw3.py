#!/usr/bin/python
#	-*-	coding:	utf-8	-*-	
import	sys,urllib,json,re,urlparse
url	=	str(sys.argv[1])
location	=	str(sys.argv[2]).decode("utf8")
roadName	=	str(sys.argv[3]).decode("utf8")
year	=	int(sys.argv[4])	*	100	#year+month
avg_price	=	0
num	=	0				#num	of 	data	
data	=	urllib.urlopen(url)
js	=	json.load(data)
dataLocation	=	'鄉鎮市區'.decode("utf8")
dataRoadName	=	'土地區段位置或建物區門牌'.decode("utf8")
dataYear	=	'交易年月'.decode("utf8")
dataPrice	=	'總價元'.decode("utf8")
for	show	in	js:
	if	location	in	show[dataLocation]:
		if	roadName	in	show[dataRoadName]:
			if	year	<=	int(show[dataYear]):
				#print	re.sub('"(.*?)"', r'\1', json.dumps(show[dataLocation],	ensure_ascii=False)),	
				#print	re.sub('"(.*?)"', r'\1',json.dumps(show[dataRoadName],	ensure_ascii=False)),
				#print	json.dumps(show[dataYear]),
				#print	json.dumps(show[dataPrice])
				avg_price	=	avg_price	+	int(show[dataPrice])
				num	=	num	+	1
if	num	!=	0:
	avg_price	=	avg_price	/	num
avg_price	=	(int(avg_price))
print	avg_price
