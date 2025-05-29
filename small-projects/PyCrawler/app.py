import requests
from bs4 import BeautifulSoup
url = "https://stackoverflow.com/questions"

response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
print("type: ", type(questions))
# print(questions[0].attrs)
# print(questions[0].get("id", 0))
# print(questions[0].select_one(".s-link"))
question_list = [question.select_one(
    ".s-link").get_text() for question in questions]
print(question_list)

# for question in questions:
# print(question.select_one(".s-link").get_text())
