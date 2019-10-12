from bs4 import BeautifulSoup
import pandas as pd
import requests
from googlesearch import search 
import re
import json
import pandas as pd

companies = ['ICBC',
 'China Construction Bank',
 'Berkshire Hathaway',
 'JPMorgan Chase',
 'Wells Fargo',
 'Agricultural Bank of China',
 'Bank of America',
 'Bank of China',
 'Apple',
 'Toyota Motor',
 'AT&T',
 'Citigroup',
 'ExxonMobil',
 'General Electric',
 'Samsung Electronics',
 'Ping An Insurance Group',
 'Wal-Mart Stores',
 'Verizon Communications',
 'Microsoft',
 'Royal Dutch Shell',
 'Allianz',
 'China Mobile',
 'BNP Paribas',
 'Alphabet',
 'China Petroleum & Chemical',
 'Total',
 'AXA Group',
 'Daimler',
 'Volkswagen Group',
 'Mitsubishi UFJ Financial',
 'Comcast',
 'Johnson & Johnson',
 'Banco Santander',
 'Bank of Communications',
 'Nestle',
 'UnitedHealth Group',
 'Nippon Telegraph & Tel',
 'Itaú Unibanco Holding',
 'Softbank',
 'Gazprom',
 'General Motors',
 'China Merchants Bank',
 'IBM',
 'Royal Bank of Canada',
 'Japan Post Holdings',
 'Procter & Gamble',
 'Pfizer',
 'HSBC Holdings',
 'Goldman Sachs Group',
 'Siemens',
 'BMW Group',
 'China Life Insurance',
 'ING Group',
 'Intel',
 'Postal Savings Bank Of China',
 'Sberbank',
 'TD Bank Group',
 'Cisco Systems',
 'Commonwealth Bank',
 'Morgan Stanley',
 'Novartis',
 'Banco Bradesco',
 'Industrial Bank',
 'Ford Motor',
 'Shanghai Pudong Development',
 'CVS Health',
 'Walt Disney',
 'Prudential',
 'Prudential Financial',
 'Oracle',
 'China State Construction Engineering',
 'Citic Pacific',
 'Boeing',
 'Honda Motor',
 'China Minsheng Banking',
 'Westpac Banking Group',
 'Deutsche Telekom',
 'China Citic Bank',
 'Roche Holding',
 'UBS',
 'Bank of Nova Scotia',
 'Rosneft',
 'Amazon.com',
 'PepsiCo',
 'Sumitomo Mitsui Financial',
 'Coca-Cola',
 'United Technologies',
 'Sanofi',
 'Bayer',
 'Mizuho Financial',
 'Zurich Insurance Group',
 'ANZ',
 'BASF',
 'Walgreens Boots Alliance',
 'Nissan Motor',
 'US Bancorp',
 'American Express',
 'Hon Hai Precision',
 'Enel',
 'Merck',
 'National Australia Bank',
 'PetroChina',
 'Unilever',
 'Hyundai Motor',
 'BBVA-Banco Bilbao Vizcaya',
 'Reliance Industries',
 'Charter Communications',
 'SAIC Motor',
 'Chubb',
 'Telefónica',
 'AIA Group',
 'Société Générale',
 'Dow Chemical',
 'Home Depot',
 'Lloyds Banking Group',
 'Medtronic',
 'Kraft Heinz Company',
 'Saudi Basic Industries',
 'Facebook',
 'Munich Re',
 'Intesa Sanpaolo',
 'Barclays',
 'Rio Tinto',
 'BHP Billiton',
 'CK Hutchison',
 'Anheuser-Busch InBev',
 'Taiwan Semiconductor',
 'Capital One Financial',
 'LukOil',
 'Swiss Re',
 'Amgen',
 'Banco do Brasil',
 'Bank of Montreal',
 'Gilead Sciences',
 'China Communications Construction',
 'Honeywell International',
 'Manulife',
 'Korea Electric Power',
 'Generali Group',
 'Alibaba',
 'KDDI',
 'China Telecom',
 'AbbVie',
 'Tokio Marine Holdings',
 'Iberdrola',
 'EDF',
 'PNC Financial Services',
 'Tencent Holdings',
 'Allergan',
 'China Everbright Bank',
 'Credit Agricole',
 'Lockheed Martin',
 'Time Warner',
 'Duke Energy',
 'Anthem',
 'Vale',
 'Nordea Bank',
 'Express Scripts',
 'United Parcel Service',
 'Aetna',
 'China Shenhua Energy',
 'VINCI',
 'Bank of New York Mellon',
 'Renault',
 'China Railway Group',
 'EADS',
 'China Railway Construction',
 'China Vanke',
 'Jardine Matheson',
 'Qualcomm',
 'Hewlett Packard Enterprise',
 'British American Tobacco',
 'Visa',
 'China Pacific Insurance',
 'MetLife',
 'AstraZeneca',
 'Altria Group',
 'SAP',
 'Costco Wholesale',
 'Travelers',
 'Philip Morris International',
 'Union Pacific',
 'Delta Air Lines',
 'Southern Company',
 "Lowe's",
 'National Grid',
 'Legal & General Group',
 'McKesson',
 'Christian Dior',
 'PTT PCL',
 'Dai-ichi Life Insurance',
 'Twenty-First Century Fox',
 'Canadian Imperial Bank',
 'FedEx',
 'GlaxoSmithKline',
 'Deutsche Post',
 '3M',
 "L'Oréal Group",
 'Aflac',
 'Allstate']

def esg_rating(company, weights):
    query = company + "'sustainability'" + "site:https://finance.yahoo.com/quote/"
    link = 0
    for j in search(query, tld="co.in", num=10, stop=1, pause=2):
        link = j
    sleep(randint(8,20))
    page_response = requests.get(link, timeout = 5)
    page_content = BeautifulSoup(page_response.content, "lxml")
    #avg = page_content.find_all("span", attrs = {"class": "Bdstarts(s) Bdstartw(0.5px) Pstart(10px) Bdc($c-fuji-grey-c) Fz(12px) smartphone_Fz(10px) smartphone_Bd(n) Fw(500)"})
    item = page_content.select("div span[data-reactid='38']")
    item2 = page_content.select("div span[data-reactid='48']")
    item3 = page_content.select("div span[data-reactid='58']")
    
    try:
        #percentile_A = avg[0].text
        percentile_E = item[1].text
        percentile_S = item2[0].text
        percentile_G = item3[0].text
    except:
        return "Company does not have ESG"
    
    try:
        #score_a = int(int(re.findall("\d+", percentile_A)[0]))
        score = int(re.findall("\d+", percentile_E)[0])
        score2 = int(re.findall("\d+", percentile_S)[0])
        score3 = int(re.findall("\d+", percentile_G)[0])
        # return [score_a, score, score2, score3]
        scores = [score, score2, score3]
        adj_mean = 0
        for i in range(3):
            adj_mean += scores[i] * weights[i]
        return [adj_mean] + scores
    except:
        return None

def score(lst):
    letters = []
    for score in lst:
        letter = ""
        if 90 <= score <= 100:
            letter = "A"
        elif 80 <= score < 90:
            letter = "B"
        elif 70 <= score < 80:
            letter = "C"
        elif 60 <= score < 70:
            letter = "D"
        else:
            letter = "F"
            letters.append(letter)
            continue
        if score % 10 >= 7:
            letters.append(letter + "+")
        elif 3 <= score % 10 < 7:
            letters.append(letter)
        else:
            letters.append(letter + "-")
    return letters
    
if __name__ == "__main__":
    data = []
    for i in companies:
        try:
            data.append({i : esg_final(i, [1 / 3, 1 / 3, 1 / 3])})
        except:
            continue
    import json
    with open('result.json', 'w') as fp:
        json.dump(data, fp)
    