import requests
from pprint import pprint


def translator(strings, language):
    translations = []

    for s in strings:
        translations.append(translate(s, language))

    return translations


def translate(to_be_translated, language):
    url = "https://www.online-translator.com/services/soap.asmx/GetTranslation"

    payload = ("{dirCode:'" + language + "', template:'auto', text:" + "'" + to_be_translated + "'" +
               ", lang:'en', limit:'3000',useAutoDetect:true, key:'123', ts:'MainSite',tid:'', IsMobile:false}")

    headers = {
        'Host': "www.online-translator.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Language': "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding': "gzip, deflate, br",
        'Referer': "https://www.online-translator.com/",
        'Content-Type': "application/json",
        'X-Requested-With': "XMLHttpRequest",
        'Content-Length': "152",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers).json()
    # pprint(response)

    if len(response['d']["resultNoTags"]) > 0:
        translation = response['d']["resultNoTags"].split(',')[2].split(" ")[1]  # More results
    else:
        translation = response['d']["result"]  # Only one result

    return translation
