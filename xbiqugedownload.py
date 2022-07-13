import requests
import parsel

url="https://www.xbiquge.la/1/1690/"
response=requests.get(url)
response.encoding="utf-8"
selector=parsel.Selector(response.text)
novel_name=selector.css("#info h1::text").get()#小说名字
href=selector.css("#list dd a::attr(href)").getall()#小说章节url
for link in href:
	link_url="https://www.xbiquge.la"+link
	response_1=requests.get(link_url)
	response_1.encoding="utf-8"
	selector_1=parsel.Selector(response_1.text)
	title=selector_1.css('.bookname h1::text').get()#章节名字
	content_list=selector_1.css('#content::text').getall()#小说内容
	content="\n".join(content_list)
	
	with open(novel_name+".txt", mode="a",encoding="utf-8") as f:
		try:
			f.write(title)
			f.write("\n")
			f.write(content)
			f.write('\n')
		except Exception as e:
			raise e
		
	print(title)