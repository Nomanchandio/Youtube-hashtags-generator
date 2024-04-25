import os
import json
import googleapiclient.discovery
import googleapiclient.errors

API_KEY = os.getenv('API_KEY', 'AIzaSyAVZhXNtFnRkq0Dzx8WZLTd4hxRo-w98q4')

api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=API_KEY)

def generate_hashtags(target_keyword, max_results=30):
    request = youtube.search().list(
        q=target_keyword,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    hashtags = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_request = youtube.videos().list(
            part="snippet",
            id=video_id
        )
        video_response = video_request.execute()
        
        description = video_response['items'][0]['snippet']['description']
        video_hashtags = [word for word in description.split() if word.startswith('#')]
        hashtags.extend(video_hashtags)

    hashtag_counts = {}
    for hashtag in hashtags:
        hashtag_counts[hashtag] = hashtag_counts.get(hashtag, 0) + 1

    sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)

    formatted_hashtags = [f"#{hashtag[0]}" for hashtag in sorted_hashtags[:15]]

    return formatted_hashtags


def lambda_handler(event, context):
    target_keyword = event['keyword'] if 'keyword' in event else ''
    if not target_keyword:
        return {
            'statusCode': 400,
            'body': 'Target keyword is missing'
        }
    
    hashtags = generate_hashtags(target_keyword)
    
    response_body = {
        'generated_hashtags': hashtags
    }
    
    return {
        'statusCode': 200,
        'body': response_body
    }

if __name__ == '__main__':
    event = {'keyword': 'programming tutorials'}
    context = {}
    print(lambda_handler(event, context))