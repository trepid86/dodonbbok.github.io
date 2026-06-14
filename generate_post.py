import os
import google.generativeai as genai
from datetime import datetime

def generate_weekly_post():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    today = datetime.now().strftime("%Y년 %m월 %d일")
    
    response = model.generate_content(f"""
{today} 기준 이번 주 핫한 주식 분석 리포트를 작성해줘.
- 주간 핫 종목 5~7개 선정
- 각 종목별 이슈 및 분석
- 시장 전체 흐름 요약
- 마크다운 형식으로 작성
- 투자 유의사항 포함
    """)
    
    content = response.text
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"_posts/{date_str}-weekly-stock-report.md"
    
    post = f"""---
layout: post
title: "📈 주간 핫 주식 분석 ({today})"
date: {date_str}
categories: 주식분석
tags: [주식, 핫주식, 주간분석]
---

{content}

---
> ⚠️ 본 내용은 투자 참고용이며 투자 판단과 책임은 본인에게 있습니다.
"""
    
    os.makedirs("_posts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(post)
    
    print(f"✅ 포스트 생성 완료: {filename}")

generate_weekly_post()
