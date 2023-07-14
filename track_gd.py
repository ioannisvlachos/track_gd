import requests
import time

sites = []

site = ['https://alphabank', 'https://ethnikitrapeza', 'https://piraeusbank', 'https://winbank', 'https://myalphaweb', 'https://nbgibankgrethnikitrapeza', 'https://myalphamobile',]
domain = '.godaddysites.com'
f = open('active_phishing_alpha.txt', 'w')

start_time = time.time()
for x in range(10):
    # if x % 100 == 0:
    #     print('Sleeping.....')
    #     time.sleep(2)
    for y in site:
        try:
            website = y + str(x) + domain
            get_site = requests.get(website, timeout = 10)
            if get_site.status_code == 404:
                print('Site ' + website + ' not found!')
            if get_site.status_code == 200:
                print('[*] SUCCESS! Site ' + website + ' is active!')
                if website not in sites:
                    sites.append(website)
        except TimeoutError:
            continue           

for x in sites:
	f.write(str(x))
	f.write('\n')

f.close()

print('Execution time is ' + str((time.time() - start_time)))
