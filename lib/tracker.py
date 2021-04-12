from appg_scrape import callScrape
import csv
import pandas as pd
from datetime import datetime, timedelta


today = str(datetime.today().date())
main_file = 'output.csv'


def scrapeArrayToJson(data):
    json = {'prca': {'source': 'prca', 'list': []}}

    for campaign in data:
        json['appg']['list'].append({
            'name': campaign[0],
            'employees': campaign[1],
            'clients': campaign[2],
            'size': campaign[3]
        })
    return json


def initialWriteToCSV(data, file):
    with open(file, mode='w') as csv_file:
        fieldnames = ['name', 'employees', 'clients', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data['appg']['list']:
            print(row)
            writer.writerow({'name': row['name'],
                             'employees': row['employees'],
                             'clients': row['clients'],
                             'size': row['size']
                             })
    print("Finished writing to CSV.")


def runAPPG(url, file):
    start = datetime.now()
    start_str = str(start)
    print("Started at: " + start_str)
    print("Working...\n")

    # 1. Get data from CallScrape
    new_data = callScrape(url)

    # 2. Convert scraped data to JSON
    output = scrapeArrayToJson(new_data)

    # 3. Check if there is existing CSV data.
    print("Writing to CSV for first time\n...")
    initialWriteToCSV(output, file)
    print("CSV written to for first time.")
    
    end = datetime.now()
    total_time = end - start
    print(total_time)


url = "https://publications.parliament.uk/pa/cm/cmallparty/210310/contents.htm"
file = './output.csv'
runAPPG(url, file)
