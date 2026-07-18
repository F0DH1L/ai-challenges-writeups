# AI/LLM Security Challenges

Writeups and solutions for AI/LLM security challenges that I solved.

## Challenges

| # | Challenge | Platform | Category | Technique | Writeup |
|---|-----------|----------|----------|-----------|---------|
| 1 | External Affairs | Hack The Box | Prompt Injection | Direct prompt injection via delimiter injection to force a `GRANTED` verdict | [Writeup](hackthebox-external-affairs) |
| 2 | trynaSob Ransomware | Hack The Box | Prompt Injection | System prompt extraction via translation attack to leak the promo code / flag | [Writeup](hackthebox-trynaSob-ransomware) |
| 3 | Loyalty Survey | Hack The Box | Agentic AI Hijacking | Prompt injection in survey answers to hijack an AI agent into calling `update_citizen_score(score: 100)` | [Writeup](hackthebox-loyalty-survey) |
| 4 | Doctrine Studio | Hack The Box | SSRF / LFI via Agentic Tool Abuse | SSRF → LFI by forcing the agent to call `fetch_news("file:///flag.txt")` | [Writeup](hackthebox-doctrine-studio) |
| 5 | Indirect Prompt Injection | PortSwigger | Indirect Prompt Injection | Poisoning a product review with a JSON-breaking payload to make the chatbot call `delete_account` on Carlos | [Writeup](portswigger-indirect-prompt-injection) |