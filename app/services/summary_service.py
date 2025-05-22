from app.utils.http_client import make_summary_api_request

def summarize_article(url):
    return make_summary_api_request(url)