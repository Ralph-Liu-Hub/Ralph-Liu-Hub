#!/usr/bin/env python3
"""Generate weekly commit-activity SVG bar charts for private project repos.

Reads GITHUB_TOKEN from the environment and writes one SVG per repo to assets/.
Uses only the stdlib so it runs in CI with no extra pip installs.
"""
import json
import os
import subprocess
import sys
import time

REPOS = [
    "Website-TheJob",
    "Project-Ralph",
    "project-sophos",
    "project-mercury",
    "project-artemis",
]
OWNER = "Ralph-Liu-Hub"
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

BAR_COLOR = "#2f81f7"
BG_COLOR = "#0d1117"
TEXT_COLOR = "#c9d1d9"
WIDTH, HEIGHT = 760, 120
PAD_LEFT, PAD_RIGHT, PAD_TOP, PAD_BOTTOM = 10, 10, 10, 20


def fetch_commit_activity(repo, token, retries=6, delay=3):
    url = f"https://api.github.com/repos/{OWNER}/{repo}/stats/commit_activity"
    for attempt in range(retries):
        result = subprocess.run(
            [
                "curl", "-s",
                "-H", f"Authorization: Bearer {token}",
                "-H", "Accept: application/vnd.github+json",
                "-H", "User-Agent: activity-chart-generator",
                url,
            ],
            capture_output=True, text=True, check=True,
        )
        body = result.stdout
        if body:
            data = json.loads(body)
            if isinstance(data, list) and data:
                return data
        time.sleep(delay)
    raise RuntimeError(f"commit_activity for {repo} not ready after {retries} attempts")


def render_svg(repo, weeks):
    totals = [w["total"] for w in weeks]
    max_val = max(totals) or 1
    n = len(totals)
    plot_w = WIDTH - PAD_LEFT - PAD_RIGHT
    plot_h = HEIGHT - PAD_TOP - PAD_BOTTOM
    bar_w = plot_w / n

    bars = []
    for i, total in enumerate(totals):
        bar_h = (total / max_val) * plot_h
        x = PAD_LEFT + i * bar_w
        y = PAD_TOP + (plot_h - bar_h)
        bars.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{max(bar_w - 1, 0.5):.2f}" '
            f'height="{max(bar_h, 0.5):.2f}" fill="{BAR_COLOR}" rx="1"/>'
        )

    total_commits = sum(totals)
    recent_commits = sum(totals[-8:])
    label = (
        f"{repo} — {total_commits} commits / 52 weeks "
        f"({recent_commits} in last 8 weeks)"
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT + 24}" viewBox="0 0 {WIDTH} {HEIGHT + 24}">
  <rect width="100%" height="100%" fill="{BG_COLOR}" rx="6"/>
  {''.join(bars)}
  <text x="{PAD_LEFT}" y="{HEIGHT + 16}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif" font-size="12" fill="{TEXT_COLOR}">{label}</text>
</svg>'''
    return svg


def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("STATS_PAT")
    if not token:
        print("GITHUB_TOKEN or STATS_PAT env var required", file=sys.stderr)
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)
    for repo in REPOS:
        print(f"Fetching commit activity for {repo}...")
        weeks = fetch_commit_activity(repo, token)
        svg = render_svg(repo, weeks)
        out_path = os.path.join(OUT_DIR, f"activity-{repo.lower()}.svg")
        with open(out_path, "w") as f:
            f.write(svg)
        print(f"  wrote {out_path}")


if __name__ == "__main__":
    main()
