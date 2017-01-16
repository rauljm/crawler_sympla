import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html[0])
    return cleantext

# urls_sp_tes.json
# scrapy crawl sympla_catch_data -o sp_events.csv -a file=urls_sp_tes