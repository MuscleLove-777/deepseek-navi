"""DeepSeek AI完全攻略ナビ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "DeepSeek AI完全攻略ナビ"
BLOG_DESCRIPTION = "中国発の高性能AI DeepSeekの使い方・最新モデル・ChatGPT比較を毎日更新。156カ国DL1位の実力を徹底解説。"
BLOG_URL = "https://musclelove-777.github.io/deepseek-navi"
BLOG_TAGLINE = "中国発AI DeepSeekを完全攻略するための日本語情報サイト"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/deepseek-navi"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "DeepSeek 使い方",
    "DeepSeek 料金・プラン",
    "DeepSeek vs ChatGPT",
    "DeepSeek 最新ニュース",
    "DeepSeek R1モデル",
    "DeepSeek API",
    "中国AI比較",
    "DeepSeek 活用事例",
]

THEME = {
    "primary": "#4f6ef7",
    "accent": "#7c8fff",
    "gradient_start": "#4f6ef7",
    "gradient_end": "#7c8fff",
    "dark_bg": "#0a0e1a",
    "dark_surface": "#151b2e",
    "light_bg": "#f0f3ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "DeepSeek": [
        {"service": "DeepSeek", "url": "https://www.deepseek.com", "description": "DeepSeek公式サイトで始める"},
    ],
    "DeepSeek API": [
        {"service": "DeepSeek API", "url": "https://platform.deepseek.com", "description": "DeepSeek APIプラットフォーム"},
    ],
    "AI比較": [
        {"service": "ChatGPT Plus", "url": "https://chat.openai.com", "description": "ChatGPT Plusに登録する"},
        {"service": "Claude Pro", "url": "https://claude.ai", "description": "Claude Proに登録する"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8096
