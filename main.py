# from scrapy import cmdline
#
# cmdline.execute("scrapy crawl mm  -a years=2016,2017,2018,2019,2020,2021,2022 -a keys=emotion,affective -o emotion.csv".split())

# cmdline.execute("scrapy crawl nips  -a years=2016,2017,2018,2019,2020,2021,2022 -a keys=emotion,affective -o emotion.csv".split())
#
# # cmdline.execute("scrapy crawl nips  -a years=2015 -a keys=video -o test.csv".split())
# # cmdline.execute("scrapy crawl eccv  -a years=2020,2021,2022 -a keys=video -o output.csv -s JOBDIR=folder6".split())

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hello PhD life!')
    parser.add_argument(
        'confs', type=str, help='What years you want to crawl?')
    parser.add_argument(
        '--years',
        default="2022",
        type=str,
        help='What years you want to crawl?')
    parser.add_argument(
        '--queries', default="", help='What keywords you want to query?')

    args = parser.parse_args()

    confs = args.confs
    years = args.years
    queries = args.queries

    setting = get_project_settings()
    process = CrawlerProcess(setting)

    for conf in confs.split(','):
        process.crawl(conf, years=years, queries=queries)

    process.start()
