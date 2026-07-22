<h1 align="center">Hi, I'm Ralph Liu 👋</h1>

<p align="center">
  <em>Building reliable software & data products — turning private work into public results.</em>
</p>

<p align="center">
  <a href="mailto:cyliu.analyst@gmail.com"><img src="https://img.shields.io/badge/Email-cyliu.analyst%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://www.linkedin.com/in/chieh-yu-liu"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://sites.google.com/view/ralph-cy-liu/"><img src="https://img.shields.io/badge/Website-Visit-FF5722?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"/></a>
  <a href="https://www.amazon.com/dp/B0FGZ57659"><img src="https://img.shields.io/badge/Book-Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white" alt="Book on Amazon"/></a>
  <a href="https://github.com/Ralph-Liu-Hub"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
</p>

---

## 👨‍💻 About Me

- 🔭 Most of my work lives in **private repositories** (personal and paid client projects), so this profile is where I document what I've built and the impact it delivered.
- 🧠 I care about clean architecture, measurable outcomes, and shipping things that hold up in production.
- 📫 Reach me at **cyliu.analyst@gmail.com** — open to opportunities and collaboration.

> 💡 **Recruiter note:** My contribution graph and stats below **include private contributions**. My public repo count is intentionally low because client work stays private — the numbers reflect real, ongoing output.

---

## 🛠️ Tech Stack

<!-- Edit this list to match your actual stack. Badges from https://shields.io -->

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)

**Frontend**

![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Backend & Data**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Shell](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnubash&logoColor=white)

**DevOps & Tools**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 🚀 Project Highlights

> My repositories are private (client and personal work), so here's what I've built, how it's engineered, and real weekly commit activity pulled straight from each repo.

### 🔹 Sophos Academy — CFA/CPA exam prep platform
**Stack:** `Next.js 16` · `React 19` · `TypeScript` · `PostgreSQL (Supabase)` · `Tailwind CSS` · `Claude Sonnet`
- **What it does:** Live product ([sophosacademy.org](https://sophosacademy.org)) selling expert-reviewed CFA/CPA mock exams, a free practice question bank, and SEO-optimized study guides, with its own purchase/dashboard/admin system.
- **Stands out:** Full commercial stack shipped solo — auth (Google OAuth + magic link), payments (webhook-based checkout, no SDK), AI-generated exam questions with prompt caching, and a 195-test Vitest suite gating every CI run.

![Sophos Academy activity](assets/activity-project-sophos.svg)

### 🔹 Project Artemis — AI recruiting platform
**Stack:** `Next.js 14` · `Node.js/Express` · `TypeScript` · `PostgreSQL` · `Docker` · `Claude Sonnet`
- **What it does:** End-to-end talent-acquisition tool — AI candidate sourcing, 4-dimension AI evaluation streamed live via SSE, auto-triage, interview scheduling by parsing inbound email replies, and AI-drafted candidate/interviewer emails.
- **Stands out:** Multi-tenant SaaS architecture with per-org PostgreSQL schema isolation enforced by a custom CI lint gate, priority job queues (pg-boss) for live vs. background AI evaluation, and prompt-cached JDs so only marginal candidate tokens are billed per evaluation.

![Project Artemis activity](assets/activity-project-artemis.svg)

### 🔹 Mercury — Wyckoff Box-Zone AI trading system
**Stack:** `Python (asyncio)` · `PostgreSQL` · `Redis` · `FastAPI` · `Docker` · `Claude API`
- **What it does:** Fully automated crypto futures trading system on Gate.io, implementing the Wyckoff Box-Zone methodology end-to-end — zone detection, signal generation, risk-managed execution, and portfolio tracking.
- **Stands out:** 8 independent asyncio agents communicating over a Redis pub/sub bus, a dedicated Sentinel agent enforcing a max-drawdown circuit breaker, and a weekly Evolution agent that uses Claude to tune strategy parameters from live performance.

![Mercury activity](assets/activity-project-mercury.svg)

### 🔹 Project Ralph — agentic AI personal-branding pipeline
**Stack:** `Python` · `GitHub Actions` · `Claude Code` · `LinkedIn API`
- **What it does:** An agentic content pipeline that drafts, validates, and — after human review — automatically publishes this profile's LinkedIn posts on a fixed Mon/Wed/Fri schedule.
- **Stands out:** Hard rule-gated validator (hashtag rules, mandatory verifiable references, length limits, credential-leak scanning) runs in CI on every PR; publishing authority always requires a human merge, never fully autonomous.

![Project Ralph activity](assets/activity-project-ralph.svg)

### 🔹 Website-TheJob — company marketing site
**Stack:** `Next.js` · `TypeScript` · `Vercel`
- **What it does:** Production marketing website for [thejob.com.tw](https://thejob.com.tw).

![Website-TheJob activity](assets/activity-website-thejob.svg)

<sub>Charts show weekly commit counts for the last 52 weeks, pulled from each repo's real commit history and refreshed automatically (see below).</sub>

<!--
  Tip: to add an architecture diagram or a screen-recording GIF,
  drop the file in an `assets/` folder in this repo and embed it:
  ![Project demo](assets/project-demo.gif)
-->

---

## 📫 Get in Touch

| Channel | Link |
| --- | --- |
| 📧 Email | [cyliu.analyst@gmail.com](mailto:cyliu.analyst@gmail.com) |
| 💼 LinkedIn | [linkedin.com/in/chieh-yu-liu](https://www.linkedin.com/in/chieh-yu-liu) |
| 📝 Personal Website | [sites.google.com/view/ralph-cy-liu](https://sites.google.com/view/ralph-cy-liu/) |
| 📚 Book | [No-Nonsense Cryptocurrency Investing Concepts for Beginners](https://www.amazon.com/dp/B0FGZ57659) |
| 🐙 GitHub | [github.com/Ralph-Liu-Hub](https://github.com/Ralph-Liu-Hub) |

<p align="center"><em>Thanks for stopping by — let's build something great together. 🚀</em></p>
