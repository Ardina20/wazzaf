import requests
import bs4

result = requests.get("https://www.amazon.com/s?k=gaming+accessories&crid=1JGXF4JA15KD4&sprefix=gaming+a%2Caps%2C510&ref=nb_sb_ss_ts-doa-p_1_8")
print(result)