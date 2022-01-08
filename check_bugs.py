import json
from name import get_info
from data_dex import urls, categories

with open("data_cleaned.json", "r") as f:
    dex = json.load(f)

for mon in dex:
    for i, url in enumerate(urls):
        try:
            get_info(mon,url)
        except Exception as exception:
            e = exception.__class__.__name__
            str_error = f"{e}  for {mon}  -  {categories[i]}    -  {url+mon}"
            print(str_error)
            with open("sample.txt", "a") as f:
                f.write(str_error + "\n")