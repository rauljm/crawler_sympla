# crawler_sympla

### Install Dependencies
---------------------------------------
First, please, create a virtualenv to project and follow the instructions below.

```sudo apt-get install build-essential```
<br>
```sudo apt-get install libxml2-dev libxslt1-dev python-dev```
<br>
```sudo pip install -r requirements.txt```
<br>	
```sudo pip install cryptography```
<br>
```sudo pip install Scrapy```

### Examples
<br>
scrapy crawl sympla_generate_url -o urls_sp.json -a complement=sao-paulo-sp
<br>
scrapy crawl sympla_catch_data -o sp_events.csv -a file=urls_sp
