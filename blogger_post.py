import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 인증 범위
SCOPES = ['https://www.googleapis.com/auth/blogger']

# 블로그 ID는 블로그 주소와는 다름 (숫자 ID)
BLOG_ID = 'YOUR_BLOG_ID'  # 예: 1234567890123456789

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('blogger', 'v3', credentials=creds)
    return service

def post_to_blogger(title, content):
    service = get_service()

    body = {
        'kind': 'blogger#post',
        'title': title,
        'content': content
    }

    post = service.posts().insert(blogId=BLOG_ID, body=body).execute()
    print(f"✅ Posted! Title: {post['title']}, URL: {post['url']}")

if __name__ == "__main__":
    title = "CADinfra 개발 로그 예시"
    content = "<h2>ChatGPT 대화 내용 요약</h2><p>여기 들어갈 내용 정리</p>"

    post_to_blogger(title, content)
