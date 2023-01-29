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
    parser = argparse.ArgumentParser(description="Crawl conference paper info")
    parser.add_argument(
        "conference",
        type=str,
        help="Conference names, seperated by comma. Supported names include "
        "cvpr, iccv, eccv, neurips, aaai, icml, iclr, wacv",
    )
    parser.add_argument(
        "years",
        type=str,
        help="Years of the conference, separated by comma",
    )
    parser.add_argument(
        "--queries", default="", help="What keywords you want to query?"
    )

    args = parser.parse_args()

    conference = args.conference
    years = args.years
    queries = args.queries

    setting = get_project_settings()
    process = CrawlerProcess(setting)

    for conf in conference.split(","):
        process.crawl(conf, years=years, queries=queries)

    process.start()
