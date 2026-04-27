import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open('issues.json', 'r', encoding='utf-8') as f:
    issues = json.load(f)

for issue in issues:
    if issue.get('pull_request'):
        continue
    labels = [l['name'] for l in issue.get('labels', [])]
    label_str = ' | '.join(labels)
    title = issue['title'].replace('\n', ' ')
    print(f"#{issue['number']} [{label_str}] {title}")
