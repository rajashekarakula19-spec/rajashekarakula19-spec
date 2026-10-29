"""Render repository-owned profile cards from GitHub's API. No third-party stats host."""
import json
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERY = '''query { user(login:"rajashekarakula19-spec") { repositories(ownerAffiliations:OWNER,privacy:PUBLIC,first:100) { totalCount nodes { stargazerCount languages(first:10,orderBy:{field:SIZE,direction:DESC}) { edges { size node { name color } } } } } contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } } } } }'''
if len(sys.argv) > 1:
    payload = json.loads(Path(sys.argv[1]).read_text())
else:
    payload = json.loads(subprocess.check_output(['gh', 'api', 'graphql', '-f', 'query=' + QUERY], text=True))
if payload.get('errors'):
    raise RuntimeError(payload['errors'])
user = payload['data']['user']
repos = user['repositories']
calendar = user['contributionsCollection']['contributionCalendar']
langs = defaultdict(int)
colors = {}
for repo in repos['nodes']:
    for edge in repo['languages']['edges']:
        name = edge['node']['name']
        langs[name] += edge['size']
        colors[name] = edge['node']['color'] or '#a78bfa'
updated = datetime.now(timezone.utc).strftime('%b %d, %Y')

def text(x, y, value, size=16, fill='#e8edf7', weight=400):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{weight}">{escape(str(value))}</text>'

def save(name, body, height, label):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img" aria-label="{escape(label)}"><defs><linearGradient id="edge"><stop stop-color="#22d3ee"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#fb7185"/></linearGradient></defs><rect x="1" y="1" width="998" height="{height-2}" rx="22" fill="#0d1224" stroke="#28314c"/><rect x="24" y="24" width="64" height="4" rx="2" fill="url(#edge)"/>{body}</svg>'''
    (ROOT/'assets'/name).write_text(svg+'\n')

metrics = [('PUBLIC REPOS', repos['totalCount'], '#22d3ee'), ('CONTRIBUTIONS', calendar['totalContributions'], '#a78bfa'), ('REPOSITORY STARS', sum(r['stargazerCount'] for r in repos['nodes']), '#fbbf24'), ('LANGUAGES', len(langs), '#a3e635')]
body = text(28, 65, 'THE BUILD LOG', 24, weight=800) + text(28, 91, 'A snapshot of the work behind the profile.', 13, '#9baac5')
for i, (label, value, color) in enumerate(metrics):
    x = 28 + i*244
    body += f'<rect x="{x}" y="115" width="226" height="116" rx="14" fill="#151d33"/>'
    body += text(x+18, 165, value, 36, color, 800) + text(x+18, 201, label, 11, '#b5c1d9', 700)
body += text(28, 260, f'GitHub API · public repositories · contributions over the last year · updated {updated} UTC', 11, '#8b9bb8')
save('github-stats.svg', body, 285, 'Public GitHub repository and contribution statistics')

ranked = sorted(langs.items(), key=lambda item: item[1], reverse=True)[:6]
total = sum(langs.values()) or 1
body = text(28,65,'LANGUAGE FREQUENCIES',24,weight=800) + text(28,91,'By code bytes across public repositories · not a proficiency score',13,'#9baac5')
for i,(name,size) in enumerate(ranked):
    y=126+i*35
    body += text(28,y+13,name,13,weight=600)
    body += f'<rect x="200" y="{y}" width="650" height="14" rx="7" fill="#1d2840"/><rect x="200" y="{y}" width="{max(2,650*size/total):.1f}" height="14" rx="7" fill="{colors[name]}"/>'
    body += text(875,y+13,f'{size/total:.1%}',13,colors[name],700)
save('github-languages.svg',body,355,'Language distribution by code bytes in public repositories')

body = text(28,65,'CONSISTENCY, ONE SQUARE AT A TIME',24,weight=800)+text(28,91,'Last 12 months of GitHub contributions',13,'#9baac5')
weeks=calendar['weeks']; max_count=max(d['contributionCount'] for w in weeks for d in w['contributionDays']) or 1
palette=['#1b2540','#164e63','#0891b2','#22d3ee','#a3e635']
for x,week in enumerate(weeks):
    for y,day in enumerate(week['contributionDays']):
        count=day['contributionCount'];color=palette[0 if count==0 else min(4,1+int(count/max_count*3))]
        body+=f'<rect x="{28+x*17}" y="{118+y*20}" width="13" height="16" rx="3" fill="{color}"><title>{day["date"]}: {count} contributions</title></rect>'
body+=text(28,288,f'{calendar["totalContributions"]} contributions · snapshot updated {updated} UTC',12,'#9baac5')
save('github-activity.svg',body,315,'GitHub contribution calendar for the last twelve months')
print('Rendered GitHub stats, language distribution, and contribution calendar.')
