from re import findall

pattern = r'href="https://www\.instagram\.com/([^">]+)'

with open('followers.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
followers = findall(pattern, html_content)

with open('following.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
following = findall(pattern, html_content)

not_following_back = [username for username in following if username not in followers]
print(not_following_back)