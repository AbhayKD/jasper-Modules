import requests,re
from num2words import num2words

def doSomethingElse(): return "Common dont be and idiot. Gemme a operation to perform"

op = {"argentina peso":"ARS","australia dollar":"AUD","bitcoin":"BTC","brazil real":"BRL","canada dollar":"CAD","chile Peso":"CLP",
     "china yuan":"CNY","czech republic koruna":"CZK","denmark krone":"DKK","euro":"EUR","fiji dollar":"FJD","honduras lempira":"HNL",
     "hong kong dollar":"HKD","hungary forint":"HUF","iceland krona":"ISK","india rupee":"INR","indonesia rupiah":"IDR","israel shekel":"ILS",
     "japan yen":"JPY","korea won":"KRW","malaysia ringgit":"MYR","mexico peso":"MXN","new zealand dollar":"NZD","norway krone":"NOK",
     "pakistan rupee":"PKR","philippines peso":"PHP","poland zloty":"PLN","russia ruble":"RUB","singapore dollar":"SGD",
     "south africa rand":"ZAR","sweden krona":"SEK","switzerland franc":"CHF","taiwan dollar":"TWD","thailand baht":"THB","turkey liar":"TRY",
     "uk pound":"GBP","us dollar":"USD","vietnam dong":"VND"}

try:
    at = raw_input('Enter currency to convert from?')
    m1 = re.search("|".join(op), at).group()
    a = op.get(m1, doSomethingElse())
    a = a.upper()

    bt = raw_input('Enter currency to convert to?')
    m2 = re.search("|".join(op), bt).group()
    b = op.get(m2, doSomethingElse())
    b = b.upper()

    c = float(raw_input('Enter value to convert?'))
    url = ('https://currency-api.appspot.com/api/%s/%s.json') % (a, b)
    r = requests.get(url)
    ans = c*float(r.json()['rate'])
    print num2words(ans, lang="en_IN")
except:
    print "Please specify the currency properly"

#c = float(raw_input('Enter value to convert?'))
#url = ('https://currency-api.appspot.com/api/%s/%s.json') % (a, b)
#r = requests.get(url)
#print c*float(r.json()['rate'])

