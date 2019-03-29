import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    # t = 1, 7, 'cat', [1,2,3]
    # print(t)
    # print(t[1])
    #
    # n1, n2, s, l = t
    # print(n1, n2, s, l)
    # return

    print_the_header()

    code = input('What zipcode do you want the weather for (97201 or Beijing)? ')

    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    temp = 'The temp in {} is {} {} and {}'.format(report.loc, report.temp, report.scale, report.cond)
    print("en ", temp)
    print("zh ", translation(temp))

    # display for the forecast

def translation(temp): # cn.bing.com
    url = 'https://www4.bing.com/ttranslatev3?IG=0F5F772B1B624B749831269C1CED5C66&IID=SERP.5518&fromLang=en&text={}' \
          '&to=zh-Hans'.format(temp)
    # url = 'https://cn.bing.com/ttranslatev3?IG=0F5F772B1B624B749831269C1CED5C66&IID=SERP.5518&fromLang=en&text={}' \
    #       '&to=zh-Hans'.format(temp)
    response = requests.post(url)
    if response.status_code == 200 and response.json():
        return response.json()[0]["translations"][0]["text"]
    return temp

# 'https://www4.bing.com/ttranslatev3?IG=0F5F772B1B624B749831269C1CED5C66&IID=SERP.5518&fromLang=en&text=The%20temp%20in%20Beijing,%20CN%20is%2047%20F%20and%20Mostly%20Cloudy&to=zh-Hans'
def print_the_header():
    print('---------------------------------')
    print('           WEATHER APP')
    print('---------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'
    try:
        soup = bs4.BeautifulSoup(html, 'html.parser')
        loc = soup.find(class_='region-content-header').find('h1').get_text()
        condition = soup.find(class_='condition-icon').get_text()
        temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
        scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

        loc = cleanup_text(loc)
        loc = find_city_and_state_from_location(loc)
        condition = cleanup_text(condition)
        temp = cleanup_text(temp)
        scale = cleanup_text(scale)
        report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    except Exception as e:
        report = WeatherReport("", "", "", "")

    # print(condition, temp, scale, loc)
    # return condition, temp, scale, loc

    return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()