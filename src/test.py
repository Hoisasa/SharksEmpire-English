import os
from github import Github


token  = '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'

g = Github(token)

repo = g.get_repo('Hoisasa/English-word-learning')
release = repo.get_latest_release()
asset = release.get_assets()[0]

g.close()
