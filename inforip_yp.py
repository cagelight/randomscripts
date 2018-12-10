#!/bin/python

import sys
import requests
import datetime
from lxml import html, etree

yp_added_creators = []
user_added_creators = []
auto_posts = []
user_posts = []
all_posts = []
shared_files = []
watches = [
	"ajna",
	"aka6",
	"ancesra",
	"animo",
	"aomori",
	"AzelynArt",
	"blackjrXIII",
	"bluefield",
	"bonk",
	"boosterpang",
	"BottleofBourbon",
	"cavafly01",
	"cowchop",
	"CyanCapsule",
	"Daiidalus",
	"DeadDogInc",
	"demicoeur",
	"deroichi",
	"Desterotica",
	"DimWitDog",
	"djcomps",
	"dmitrys",
	"DocProxy",
	"doxydoo",
	"DragonFU",
	"etheross",
	"evulchibi",
	"flannaganthered",
	"fluffkevlar",
	"FR95",
	"Freckles",
	"furlana",
	"gisacomic",
	"hioshiru",
	"huskie666",
	"InCaseArt",
	"incorgnito",
	"iskra",
	"joix",
	"jmgn",
	"juliatdc",
	"kaibun",
	"kardie",
	"karukuji",
	"kevinsano",
	"kyotocat",
	"LDRaptor",
	"LiveForTheFunk",
	"Luckypan",
	"lyzer",
	"M6",
	"makkuart",
	"Marble_Soda",
	"MariArt",
	"marikazemus",
	"McTranceFox",
	"Michi",
	"Mindmachine",
	"Modeseven",
	"Monkeyspirit",
	"monorirogue",
	"Nyuunzi",
	"Onnanoko",
	"oouna",
	"personalami",
	"Pupuliini",
	"rajii",
	"razalor",
	"riendonut",
	"rmk",
	"Salkitten",
	"Scappo",
	"SigmaX",
	"Skygracer",
	"spindles",
	"spottyjaguar",
	"SSOCRATES",
	"studiocutepet",
	"suelix",
	"tanraakarts",
	"tarakanovich",
	"tf8",
	"tokifuji",
	"tortuga",
	"toxxy",
	"tsaiwolf",
	"Tsampikos",
	"vempire",
	"vipery_07art",
	"wo262",
	"winterblack",
	"Wyntersun",
	"Xpray",
	"yinyue",
	"yuurikin"
]
watches = [w.upper() for w in watches]

time = None
for i in range(int(sys.argv[1])):
	url = "https://yiff.party/activity?p={}".format(i+1)
	print(url)
	req = requests.get(url)
	tree = html.fromstring(req.content)

	posts = tree.xpath('//div[@class="yp-activity-main"]')

	for post in posts:
		artist = post[0][0].text
		timeutc = int(post[0][1].get('data-utc'))
		
		tdelt = datetime.datetime.now() - datetime.datetime.fromtimestamp(timeutc)
		tdeltt = tdelt.seconds + tdelt.days * 86400
		tdelth, tdeltt = divmod(tdeltt, 3600)
		tdeltm, tdelts = divmod(tdeltt, 60)
		time = '{:02d}:{:02d}:{:02d}'.format(tdelth, tdeltm, tdelts)
		info = post[1].text_content()
		
		if 'Creator was added by a user' in info:
			user_added_creators.append((artist, timeutc, time))
		elif 'Creator was added by yiff.party' in info:
			yp_added_creators.append((artist, timeutc, time))
		elif 'imported by yiff.party' in info:
			auto_posts.append((artist, timeutc, time))
			all_posts.append((artist, timeutc, time))
		elif 'imported by a user' in info:
			user_posts.append((artist, timeutc, time))
			all_posts.append((artist, timeutc, time))
		elif 'was approved' in info:
			shared_files.append((artist, timeutc, time))
		else:
			print('UNKNOWN POST TYPE ENCOUNTERED!!!')

'''
print('Automatically Added Creators:')
for artist in sorted(set(yp_added_creators), key=lambda tup: tup[1]):
	print('\t{}'.format(artist))
	
print('Automatically Added Posts:')
for artist in sorted(set(auto_posts), key=lambda tup: tup[1]):
	print('\t{}'.format(artist))
'''
	
print('User Added Creators:')
for artist in sorted(user_added_creators, key=lambda tup: tup[1]):
	print('\t[{} ago] {}'.format(artist[2], artist[0]))
	
print('User Added Posts:')
for artist in sorted(user_posts, key=lambda tup: tup[1]):
	print('\t[{} ago] {}'.format(artist[2], artist[0]))
	
print('Shared Files:')
for artist in sorted(shared_files, key=lambda tup: tup[1]):
	print('\t[{} ago] {}'.format(artist[2], artist[0]))
	
print('Watched Updates:')
for artist in sorted(all_posts, key=lambda tup: tup[1]):
	if (artist[0].upper() in watches):
		print('\t[{} ago] {}'.format(artist[2], artist[0]))
		
print('Watched Shares:')
for artist in sorted(shared_files, key=lambda tup: tup[1]):
	if (artist[0].upper() in watches):
		print('\t[{} ago] {}'.format(artist[2], artist[0]))
		
print('This scan covers the previous {}'.format(time))
