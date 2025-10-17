from typing import List, Dict

from fastmcp import FastMCP

import feedparser


mcp = FastMCP(
    name="FreeCodeCamp RSS Feed searcher"
)

@mcp.tool()
def fcc_news_search(query: str, max_results: int = 5)-> List[Dict[str, str]]:
    """
    Searches FreeCodeCamp News RSS feed for articles matching a query.

    This function fetches and parses the FreeCodeCamp News RSS feed. It searches through
    the entries for occurrences of the query in either the title or description of the
    articles. The results are returned as a list of dictionaries, containing the title,
    description, and URL of each matching article. Only a maximum number of results
    specified by the `max_results` parameter will be returned.

    Raises:
        ValueError: If the `query` argument is an empty string.

    Args:
        query (str): The search query to filter articles. It must not be empty.
        max_results (int, optional): The maximum number of matching results to return. Defaults to 5.

    Returns:
        List[Dict[str, str]]: A list containing dictionaries for each matching article. Each dictionary
        includes the keys "title", "description", and "url".
    """
    if not query:
        raise ValueError("Query must not be empty.")

    feed_url = "https://www.freecodecamp.org/news/rss"
    feed = feedparser.parse(feed_url)
    query_lower = query.lower()
    results = []
    for entry in feed.entries:
        title = entry.get("title","")
        description = entry.get("description","")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append(
                {
                    "title": title,
                    "description": description,
                    "url": entry.get("link","")
                }
            )

        if len(results) >= max_results:
            break


    return results or [{"message": "No results found."}]


@mcp.tool()
def fcc_youtube_search(query: str, max_results: int = 5)-> List[Dict[str, str]]:
    """
    Fetch and filter videos from the FCC YouTube feed that match a given query.

    This function retrieves videos from the FCC (FreeCodeCamp) YouTube channel's
    RSS feed, filters the titles based on a case-insensitive match with the
    provided query, and returns a list of the matched video details up to a
    specified maximum number.

    Parameters:
    query: str
        The search query used to filter video titles (case-insensitive).
    max_results: int, optional
        The maximum number of results to return. Default is 5.

    Returns:
    List[Dict[str, str]]
        A list of dictionaries containing matched video details, with each
        dictionary holding:
            - title: The title of the video.
            - url: The URL to the video.

        If no matching videos are found, a single-entry list is returned with
        a dictionary containing a "message" key: [{"message": "No videos found"}].
    """
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ")
    query_lower = query.lower()
    results = []
    for entry in feed.entries:
        title = entry.get("title", "")
        if query_lower in title.lower():
            results.append({
                "title": title,
                "url": entry.get("link", "")
            })
            if len(results) >= max_results:
                break

    return results or [{"message": "No videos found"}]

if __name__ == "__main__":
    mcp.run()