
import Crawler
import Alert
import ArticleResources
from FList import LIST
import json
import random

popular_sources = ArticleResources.get_popular_sources()
google_sources = ArticleResources.get_google_sources()
metaverse_sources = ArticleResources.get_metaverse_sources()
raw_sources = LIST.flatten(popular_sources, google_sources)
no_dups = list(set(raw_sources))
count = len(no_dups)

TOTAL_THRESHOLD = 10000
MAX_THRESHOLD = 1000

LAM_VER = "1.0.2"

def lambda_handler(event, context):
    init_metaverse_crawler()
    body = {
        "message": "Tiffany Crawler Function executed successfully!"
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def get_random_source():
    ran_dom = random.randint(0, count)
    url = no_dups[ran_dom]
    return url

def get_random_metaverse_source():
    m_count = len(metaverse_sources)
    ran_dom = random.randint(0, m_count)
    url = metaverse_sources[ran_dom]
    return url

def init_metaverse_crawler():
    url = get_random_metaverse_source()
    run_crawler(url, 0)

""" -> BASE FUNCTION <- """
def run_crawler(url, c=0):
    keep_total_count = c
    Alert.send_alert(f"STARTING Metaverse Crawler with URL: [ {url} ]")
    crawler = Crawler.run_suicideMode(url=url, maxQueue=MAX_THRESHOLD)
    Alert.send_alert(f"FINISHED Metaverse Crawler with count: [ {crawler.total_count} ]")
    keep_total_count = crawler.total_count + keep_total_count
    if keep_total_count < TOTAL_THRESHOLD:
        run_crawler(get_random_metaverse_source(), keep_total_count)

if __name__ == '__main__':
    init_metaverse_crawler()