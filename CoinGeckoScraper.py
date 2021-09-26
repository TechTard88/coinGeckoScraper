import requests
from pyquery import PyQuery

coins = []

class Coin:
	def __init__(self, ticker, price, oneH, twentyFourH, sevenDay, twentyFourHourVol, mkt_Cap):
		self.ticker = ticker
		self.price = price
		self.oneH = oneH
		self.twentyFourH = twentyFourH
		self.sevenDay = sevenDay
		self.twentyFourHourVol = twentyFourHourVol
		self.mkt_Cap = mkt_Cap

	def getTicker(self):
		return self.ticker

	def getPrice(self):
		return self.price

	def getOneHour(self):
		return self.oneH

	def getTwentyFourHour(self):
		return self.twentyFourH

	def getSevenDay(self):
		return self.sevenDay

	def getTwentyFourHourVol(self):
		return self.twentyFourHourVol

	def getMarketCap(self):
		return self.mkt_Cap

def scrapePage(pageNum):
	if pageNum == 0:
		URL = "https://www.coingecko.com/en"
	else:
		URL = "https://www.coingecko.com/en?page="+str(pageNum)

	r = requests.get(URL)

	doc = PyQuery(r.text)

	columns = [price.text() for price in doc('tbody tr td').items()]

	attributeCount = 0

	# print(len(columns))
	for column in columns:
		# print("column: "+column)
		# print()
		if attributeCount == 2:
			ticker = str(column).rsplit(' ', 1)[1]
			if ticker == "":
				ticker = "INFO NOT AVAILABLE"
			# print(ticker)
		elif attributeCount == 3:
			price = str(column).strip(" ")
			if price == "":
				price = "INFO NOT AVAILABLE"
			# print(price)
		elif attributeCount == 4:
			oneH = str(column).strip(" ")
			if oneH == "":
				oneH = "INFO NOT AVAILABLE"
			# print(oneH)
		elif attributeCount == 5:
			twentyFourH = str(column).strip(" ")
			if twentyFourH == "":
				twentyFourH = "INFO NOT AVAILABLE"
			# print(twentyFourH)
		elif attributeCount == 6:
			sevenDay = str(column).strip(" ")
			if sevenDay == "":
				sevenDay = "INFO NOT AVAILABLE"
			# print(sevenDay)
		elif attributeCount == 7:
			twentyFourHourVol = str(column).strip(" ")
			if twentyFourHourVol == "":
				twentyFourHourVol = "INFO NOT AVAILABLE"
			# print(twentyFourHourVol)
		elif attributeCount == 8:
			mkt_Cap = str(column).strip(" ")
			if mkt_Cap == "":
				mkt_Cap = "INFO NOT AVAILABLE"
			# print(mkt_Cap)

		if attributeCount == 9:
			attributeCount = 0
			coin = Coin(ticker, price, oneH, twentyFourH, sevenDay, twentyFourHourVol, mkt_Cap)
			coins.append(coin)
		else:
			attributeCount = attributeCount + 1
	
def getMaxPageNum():
	URL = "https://www.coingecko.com/en"
	r = requests.get(URL)
	doc = PyQuery(r.text)
	pages = doc('li .page-link')
	lastPage = int(pages[-2].text)
	return lastPage

print("Processing, please wait....")
for x in range(getMaxPageNum()+1):
	scrapePage(x)

# print(len(coins))
for coin in coins:
	print(coin.getTicker())	
	print(coin.getPrice())
	print(coin.getOneHour())
	print(coin.getTwentyFourHour())
	print(coin.getSevenDay())
	print(coin.getTwentyFourHourVol())
	print(coin.getMarketCap())
