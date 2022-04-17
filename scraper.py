from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.htbstudio.casttotv.smartview.mirrorcast',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5 # defaults to None(means all score)
)

print(result)

import json

with open('review_all.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4, default=str)