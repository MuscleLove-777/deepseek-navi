"""DeepSeek AI完全攻略ナビ - プロンプト定義

DeepSeek特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはDeepSeek AIの日本語エキスパートです。"
    "中国発AIの技術動向に精通し、DeepSeek R1やV3モデルの仕組み、"
    "コスト効率の高さ、API活用法を深く理解しています。"
    "初心者から開発者まで幅広い読者に実践的な情報を届けるプロのテックライターです。"
    "DeepSeekの最新アップデートを常にキャッチアップし、"
    "他のAI（ChatGPT、Claude、Gemini等）との比較も客観的に行えます。"
    "156カ国でDL1位を獲得した実力を技術的に解説できます。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な手順・解説。操作手順を箇条書きで明示）

## DeepSeekの技術的優位性
（Mixture of Experts / コスト効率 / オープンソース戦略について）

## 他のAIとの比較
（ChatGPT / Claude / Gemini / 他の中国AI との違いを表形式で整理）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "DeepSeek 使い方": "DeepSeek 使い方、DeepSeek 始め方、DeepSeek 登録方法、DeepSeek 無料、DeepSeek チャット、DeepSeek 日本語",
    "DeepSeek 料金・プラン": "DeepSeek 料金、DeepSeek 無料 有料 違い、DeepSeek API 料金、DeepSeek コスト、DeepSeek 月額",
    "DeepSeek vs ChatGPT": "DeepSeek ChatGPT 比較、DeepSeek ChatGPT 違い、AI 比較 2026、DeepSeek 性能、どっちがいい",
    "DeepSeek 最新ニュース": "DeepSeek アップデート、DeepSeek 新機能、DeepSeek V4、中国AI 最新、DeepSeek リリース",
    "DeepSeek R1モデル": "DeepSeek R1、DeepSeek R1 性能、DeepSeek R1 使い方、推論モデル、Chain of Thought",
    "DeepSeek API": "DeepSeek API、DeepSeek API 使い方、DeepSeek SDK、DeepSeek 開発、DeepSeek API 料金",
    "中国AI比較": "中国AI、Baidu ERNIE、Alibaba Qwen、中国AI 規制、DeepSeek 安全性、中国AI 一覧",
    "DeepSeek 活用事例": "DeepSeek ビジネス活用、DeepSeek 仕事効率化、DeepSeek 使い道、DeepSeek コーディング、DeepSeek 翻訳",
}

# ニュースソース
NEWS_SOURCES = [
    "DeepSeek公式 (https://www.deepseek.com)",
    "DeepSeek GitHub (https://github.com/deepseek-ai)",
    "TechCrunch (https://techcrunch.com/tag/deepseek/)",
    "The Verge (https://www.theverge.com/ai)",
    "36Kr (https://36kr.com/)",
    "PingWest (https://en.pingwest.com/)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "中国発AI DeepSeekに関するキーワードを選んでください。\n"
    "日本のユーザーが検索しそうな実用的なキーワードを意識してください。\n"
    "「DeepSeek 使い方」「DeepSeek 料金」「DeepSeek vs ChatGPT」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。\n"
    "DeepSeekが156カ国でDL1位になった背景や、\n"
    "R1モデルの推論能力、驚異的なコスト効率に関するキーワードも有効です。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "DeepSeek AI完全攻略ナビ用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """DeepSeek特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、DeepSeek AI専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- 具体的な操作手順や設定方法を含める
- DeepSeekの技術的優位性（MoE、コスト効率、オープンソース）を含める
- 他AIとの客観的な比較を含める
- 中国AI特有の注意点（データプライバシー、規制等）にも触れる
- 初心者にもわかりやすく、専門用語には補足説明を付ける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""
