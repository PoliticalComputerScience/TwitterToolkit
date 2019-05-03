

import requests
from bs4 import BeautifulSoup
import sqlite3
from utils import *


diction = dict()
db_filename = '/tmp/SourceScores.db'
connection = sqlite3.connect(db_filename)
cursor = connection.cursor()


def get_results(bias_name, bias_num, end_p):
    print("hello")
    main_url = "https://web.archive.org/web/20190328175019/https://mediabiasfactcheck.com/" + bias_name + "/"
    result = requests.get(main_url)
    print(result.status_code)
    src = result.content
    # print(src)
    soup = BeautifulSoup(src, 'lxml')

    score_urls = []
    for p_tag in soup.find_all("p")[2:end_p]:
        # print(p_tag)
        for a_tag in p_tag.find_all("a"):
            if "media" in str(a_tag):
                score_urls.append(a_tag.attrs["href"])
    # print(score_urls)
    prev = "prev"
    # change!!!!!!!!
    for url in score_urls:
        url_res = requests.get(url)
        if url_res.status_code != 200:
            continue;
        score_src = url_res.content
        score_soup = BeautifulSoup(score_src, 'lxml' )
        # print(score_soup.find("title"))
        source_name = str(score_soup.find("title"))[7: -31].replace("amp; ", " ")

        domain_name = get_domains([get_domain_name(score_soup, source_name)])[0]
        if bias_name == "fake-news":
            diction[source_name] = scoreNode(bias_num, 0, domain_name)
        else:
            diction[source_name] = scoreNode(bias_num, get_fact_check(score_soup, source_name, prev), domain_name)
            prev = source_name


    # links = soup.find_all("a")[42: -92]


def get_domain_name(sc_soup, sc_name):
    for p_tag in sc_soup.find_all("p"):
        # print(p_tag)
        if "Source:" in str(p_tag) or "Sources:" in str(p_tag):
            # print(p_tag)
            for a_tag in p_tag.find_all("a"):
                # print(a_tag)
                start = str(a_tag.attrs["href"])[1:].find("http")
                return (str(a_tag.attrs["href"])[start+1:-1])
    for p_tag in sc_soup.find_all("p"):
        if "Notes" in str(p_tag) and "wiki" not in str(p_tag):
            # print(p_tag)
            for a_tag in p_tag.find_all("a"):
                # print(a_tag)
                start = str(a_tag.attrs["href"])[1:].find("http")
                return (str(a_tag.attrs["href"])[start+1:-1])
    return None;




# Notes:&nbsp;
def get_fact_check(sp, ur, pr):
    for strong_tag in sp.find_all("strong"):
        if "MIXED" in str(strong_tag) or " MIXED" in str(strong_tag):
            return 3;
        elif "VERY LOW" in str(strong_tag):
            return 1;
        elif "VERY HIGH" in str(strong_tag) or "VERY-HIGH" in str(strong_tag):
            return 5;
        elif "HIGH" in str(strong_tag) or "HIGH (No pun intended)" in str(strong_tag) or "HIGH " in str(strong_tag) or " HIGH" in str(strong_tag) or "high" in str(strong_tag) or "GH" in str(strong_tag) or "High" in str(strong_tag) or "VERY&nbsp;HIGH" in str(strong_tag):
            return 4;
        elif "LOW" in str(strong_tag):
            return 2;


    for span_tag in sp.find_all("span"):
        # print(span_tag)
        if "MIXED" in str(span_tag) or " MIXED" in str(span_tag):
            return 3;
        elif "VERY LOW" in str(span_tag):
            return 1;
        elif "VERY HIGH" in str(span_tag) or "VERY-HIGH" in str(span_tag):
            return 5;
        elif "HIGH" in str(span_tag) or "HIGH (No pun intended)" in str(span_tag) or "HIGH " in str(span_tag) or " HIGH" in str(span_tag) or "high" in str(span_tag) or "GH" in str(span_tag) or "High" in str(span_tag):
            return 4;
        elif "LOW" in str(span_tag):
            return 2;


    for b_tag in sp.find_all("b"):
        if "MIXED" in str(b_tag) or " MIXED" in str(b_tag):
            return 3;
        elif "VERY LOW" in str(b_tag):
            return 1;
        elif "VERY HIGH" in str(b_tag) or "VERY-HIGH" in str(b_tag):
            return 5;
        elif "HIGH" in str(b_tag) or "HIGH (No pun intended)" in str(b_tag) or "HIGH " in str(b_tag) or " HIGH" in str(b_tag) or "high" in str(b_tag) or "GH" in str(b_tag) or "High" in str(b_tag):
            return 4;
        elif "LOW" in str(b_tag):
            return 2;




    print("errrr" + ur)
    # print("errrr" + ur + pr)



    return None



class scoreNode:
    bias_num = 0
    fact_check = 0
    domain_name = 0

    def __init__(self, bias_num, fact_check, domain_name):
        self.bias_num = bias_num
        self.fact_check = fact_check
        self.domain_name = domain_name


get_results("left", -2, -54)
get_results("leftcenter", -1, -51)
get_results("center", 0, -40)
get_results("right",1, -44)
get_results("right-center", 2, -44)
get_results("fake-news", None, -54)

#
# for key in diction.keys():
#     node = diction.get(key)
#     if type(node.domain_name) != str:
#         print("!!!!!!!!! " + key)
#     print("source: " + key + "   bias: " + str(node.bias_num) + "    fact_check: " + str(node.fact_check) + "  domain name: " + node.domain_name)
    # print("source: " + key )
    # print("   bias: " + str(node.bias_num))
    # print("    fact_check: " + str(node.fact_check))
    # print("  domain name: " + node.domain_name)
cursor.execute("CREATE TABLE scraped31 (source_name TEXT, domain_name TEXT, fact_check_score INTEGER, bias_score INTEGER)")

for ke in diction.keys():
    sour = ke
    dom = diction.get(ke).domain_name
    bi = diction.get(ke).bias_num
    fc = diction.get(ke).fact_check
    cursor.execute("INSERT INTO scraped31 (source_name, domain_name, fact_check_score, bias_score) VALUES (?,?,?,?)", [sour, dom, fc, bi])

connection.commit()
for row in connection.execute('SELECT * FROM scraped31'):
    print(row)



cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for y in (cursor.fetchall()):
    print(y)


connection.commit()
connection.close()








## add to github

##look at email

## seventeen - left - source domain no exist
##make it null if doesn't have a certain score or website

# make a new table name everytime
# questionable sources - just put bias as null, credibility as 0
#only put numbers into database, not words
# change text to number when creating table
