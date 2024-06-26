import scrapy


class TwitterSpiderSpider(scrapy.Spider):
    name = "twitter_spider"
    #allowed_domains = ["twitter.com"]
    start_urls = ["https://twitter.com/POTUS"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # Extract the tweets from the page
        tweets = response.css('.tweet-text::text').getall()
        # Print the tweets
        for tweet in tweets:
            print(tweet)
