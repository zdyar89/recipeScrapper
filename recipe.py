from bs4 import BeautifulSoup
from urllib.request import urlopen



user_input = input("What recipe are you looking for?: ")
user_input = user_input.split()
final_input = 'https://cafedelites.com/'

char = 0

while char < len(user_input) - 1:
   final_input += user_input[char]
   final_input += '-'
   char += 1

final_input += user_input[len(user_input) - 1] + '/'

print(final_input)


foodHTML = urlopen(final_input)
bs1 = BeautifulSoup(foodHTML.read(), 'html.parser')
bs1 = bs1.find_all('div', class_="wprm-recipe-ingredients-container wprm-block-text-normal")
for div in bs1:
   print(div)


##html = urlopen('https://www.reddit.com/subreddits/leaderboard/')
##bs = BeautifulSoup(html.read(), 'html.parser')
##print(bs.h1)