#Results.py
import datetime
from datetime import datetime
from StepThroughPages import stepThroughPages


def results(SEARCH_ITEM):
    check = 0
    total_posts = stepThroughPages([], '/search/zip?')
    total_posts = [post for post in total_posts if SEARCH_ITEM in (post.find('a', class_='result-title').get_text()).lower()]

    for i, post in enumerate(total_posts):
        title_div = post.find('a', class_='result-title')
        post_title = title_div.get_text()
        post_URL = title_div.get('href')
        post_time_text = post.find('time').get('datetime')
        post_time = datetime.strptime(post_time_text, '%Y-%m-%d %H:%M')
        ellasped_mins = (datetime.now() - post_time)

        if check < 1:
            check+=1
            global actualResults
            actualResults = f'{len(total_posts)} results containg "{SEARCH_ITEM}"\n'

        actualResults = actualResults + f'{i+1}: {post_title} -- {ellasped_mins} ++ {post_URL} ||||\n'

    return actualResults
