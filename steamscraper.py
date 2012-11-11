import json
import urllib2
from searchscraper import scrapeSearchPage

class SteamScraper():
	def __init__(self):
		self.entries = []
		for i in xrange(self.findNumberOfPages()):
			url = 'http://store.steampowered.com/search/results?sort_by=Name&sort_order=ASC&category1=998&page=' + str(i+1)
			self.entries += scrapeSearchPage(url)
		
	def findNumberOfPages(self):
		url = 'http://store.steampowered.com/search/results?sort_by=Name&sort_order=ASC&category1=998&page=1' 
		html = urllib2.urlopen(url).read()
		html = html[html.index('<div class="search_pagination_left">')+36:]
		html = html[:html.index('</div>')].strip()
		numEntries = int(html[html.index('of')+3:])
		numPages = numEntries / 25 + 1
		return numPages

	def outputJSON(self):
		JSONoutput = ""
		for entry in self.entries:
			JSONoutput += json.dumps(entry) + '\n'
		JSONoutput = JSONoutput.replace('\",', '\",\n\t').strip().encode('utf-8')
		open("steamdata.json", "w").write(JSONoutput)

scraper = SteamScraper()
scraper.outputJSON()