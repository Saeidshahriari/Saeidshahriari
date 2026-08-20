import datetime
import json
import os
import urllib.request

USERNAME = "Saeidshahriari"
USER_API = f"https://api.github.com/users/{USERNAME}"
REPOS_API = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner"


def _get(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def fetch_stats() -> dict:
    user = _get(USER_API)
    repos = _get(REPOS_API)

    lang_counts: dict[str, int] = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1
    top_languages = sorted(lang_counts, key=lang_counts.get, reverse=True)[:3]

    return {
        "public_repos": user.get("public_repos", "?"),
        "followers": user.get("followers", "?"),
        "top_languages": top_languages,
    }


try:
    stats = fetch_stats()
except Exception:
    stats = {"public_repos": "?", "followers": "?", "top_languages": []}

today_str = datetime.datetime.now(datetime.UTC).strftime("%B %d, %Y")
langs_str = " · ".join(stats["top_languages"]) or "—"

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="480" height="70" viewBox="0 0 480 70">
  <rect width="100%" height="100%" fill="#0d1117" rx="10" />
  <text x="20" y="30" font-family="Segoe UI, Ubuntu, sans-serif" font-size="13" fill="#58a6ff" font-weight="bold">
    📦 <tspan fill="#c9d1d9">{stats['public_repos']} public repos</tspan> · 👥 <tspan fill="#c9d1d9">{stats['followers']} followers</tspan> · 🧩 <tspan fill="#c9d1d9">{langs_str}</tspan>
  </text>
  <text x="20" y="52" font-family="Segoe UI, Ubuntu, sans-serif" font-size="13" fill="#58a6ff" font-weight="bold">
    ⚡ Last updated: <tspan fill="#c9d1d9">{today_str}</tspan>
  </text>
</svg>
"""

with open("status.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Status SVG updated successfully.")
