import requests
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

# Issues to fetch details for
issue_nums = [660, 691, 733, 715, 692, 670, 568, 664, 714, 693, 617, 585, 357, 143, 130, 116, 590, 335, 223, 699, 721, 728, 738, 740, 680, 655, 537, 533, 526, 522, 650, 569, 618, 185, 676, 669, 666, 652, 679, 549, 315, 329, 684, 739, 687, 697]

for num in issue_nums:
    url = f'https://api.github.com/repos/Creators-of-Aeronautics/Simulated-Project/issues/{num}'
    try:
        resp = requests.get(url, proxies=proxies)
        if resp.status_code == 200:
            issue = resp.json()
            body = (issue.get('body') or '')[:2000]
            print(f"\n{'='*80}")
            print(f"#{num}: {issue['title']}")
            print(f"Labels: {[l['name'] for l in issue.get('labels', [])]}")
            print(f"Body:\n{body}")
        else:
            print(f"#{num}: HTTP {resp.status_code}")
    except Exception as e:
        print(f"#{num}: Error: {e}")
