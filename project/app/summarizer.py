# project/app/summarizer.py

import nltk
from newspaper import Article

from app.models.tortoise import TextSummary


async def generate_summary(summary_id: int, url: str) -> None:
    article = Article(url)
    article.download()  # download HTML
    article.parse()  # extract meaningful content

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()  # predict relevant keywords

    # summary generated with background task after response is sent to client
    await TextSummary.filter(id=summary_id).update(summary=article.summary)
