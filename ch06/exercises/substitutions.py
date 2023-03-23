import json

with open("C:\\Users\\trost\\github-classroom\\bucs110SPRING23\\portfolio-David-Trost\\ch06\\exercises\\news.txt", "r",encoding="utf-8") as news_file, open("C:\\Users\\trost\\github-classroom\\bucs110SPRING23\\portfolio-David-Trost\\ch06\\exercises\\subs.json", "r") as subs_file:
    news_text = news_file.read()

    substitutions = json.load(subs_file)

    for key, value in substitutions.items():
        news_text = news_text.replace(key, value)

    with open("betternews.txt", "w") as output_file:
        output_file.write(news_text)