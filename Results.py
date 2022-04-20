#Results.py
import datetime
from datetime import datetime
from StepThroughPages import stepThroughPages
from SpecifySearch import SEARCH_ITEM


def results(post):
    for i, post in enumerate(totalPosts):
        titleDiv = post.find('a', class_='result-title')
        postTitle = titleDiv.get_text()
        postURL = titleDiv.get('href')
        postTimeText = post.find('time').get('datetime')
        postTime = datetime.strptime(postTimeText, '%Y-%m-%d %H:%M')
        ellaspedMins = (datetime.now() - postTime)

        print(f'{len(totalPosts)} results containg "{SEARCH_ITEM}"')
        print(f'{i+1}: {postTitle} -- {ellaspedMins} ++ {postURL} ||||')

totalPosts = stepThroughPages([], '/search/zip?')
totalPosts = [post for post in totalPosts if SEARCH_ITEM in (post.find('a', class_='result-title').get_text()).lower()]
