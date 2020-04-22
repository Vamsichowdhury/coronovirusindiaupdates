from django.shortcuts import render
import requests

# disable printing warnings
requests.packages.urllib3.disable_warnings()
from datetime import timezone, datetime, timedelta
from bs4 import BeautifulSoup
import urllib

def home(request):
    session = requests.Session()
    p_time = datetime.now(timezone.utc)
    # search what is my user agent in google to get this
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.149 Safari/537.36"}
    url = "https://www.worldometers.info/coronavirus/country/india/"
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    # <div> tag with <<.class="maincounter-number">> with child tag <span>
    # count = [ < span style = "color:#aaa" > 874 < / span >, < span > 20 < / span >, < span > 73 < / span >]

    count = soup.select("div.maincounter-number > span")
    l = []
    s=''
    for i in count:
        num = str(i.get_text())
        for i in num:
            if i.isdigit():
                s = s+i
        l.append(int(s))
        s=''
    cases, deaths, recovered = l
    return render(request, "covid19app/home.html", context={"cases": cases, "deaths": deaths,
                                                            "recovered": recovered, "time": p_time})


def aboutMe(request):
    return render(request, "covid19app/aboutMe.html")
