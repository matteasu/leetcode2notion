from scraper import Scraper

s = Scraper("https://leetcode.com/problems/two-sum/")

s.load_page()
question_title, diff, problem, examples, rest = s.scrape()

print(question_title)
print(diff)
print(problem)
print(examples)
print(rest)
