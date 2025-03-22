import os
from github import Github




g = Github(token)

repo = g.get_repo('Hoisasa/English-word-learning')
release = repo.get_latest_release()
asset = release.get_assets()[0]

g.close()
