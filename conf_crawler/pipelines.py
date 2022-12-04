# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re

from scrapy.exceptions import DropItem


class PaperItemPipeline:

    def process_item(self, item, spider):
        # Process the item one at a time.
        abstract = item["abstract"]
        title = item["title"]
        # replace any special characters from the abstract with a space.
        clean_title = re.sub(r'\W+', ' ', title).lower()
        clean_abstract = re.sub(r'\W+\-', ' ', abstract).lower()
        tokens = set(clean_title.split(' ') + clean_abstract.split(' '))

        if spider.queries:
            matched_queries = [
                query for query in spider.queries if query in tokens
            ]
        else:
            matched_queries = ''

        # If the queries are found in the abstract, then return the item
        # otherwise drop it.
        if len(matched_queries) or matched_queries == '':
            if not item.get('code_url'):
                urls = re.findall(r'(https?://github.com\S+)', abstract)
                item['code_url'] = [url.rstrip('".})') for url in urls]
            item['matched_queries'] = matched_queries
            return item
        else:
            raise DropItem(f"No query hit in {item['title']}")
