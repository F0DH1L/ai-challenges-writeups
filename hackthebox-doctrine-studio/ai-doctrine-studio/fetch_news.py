#!/usr/bin/env python3

import sys
import trafilatura
from typing import Optional

def fetch_news(url: str) -> Optional[str]:
    """
    Fetch news content from a URL and return it in markdown format
    Args:
        url: The URL to fetch news from
    Returns:
        str: Markdown formatted content or None on failure
    """
    try:
        # Download the content
        downloaded = trafilatura.fetch_response(url, no_ssl=True)

        if downloaded is None:
            return None

        # extract and convert to markdown if HTML content
        content = trafilatura.extract(downloaded)

        # text content
        if not content:
            if len(downloaded.data) > 2000:
                return downloaded.data[:2000].decode('utf-8', errors='ignore')
            else:
                return downloaded.data.decode('utf-8', errors='ignore')

        return content[:2000] if content else None
    except Exception:
        return None

if __name__ == "__main__":
    # Expect URL as first argument
    if len(sys.argv) != 2:
        sys.exit(1)

    result = fetch_news(sys.argv[1])
    if result:
        print(result)
    sys.exit(0)
