from flask import Flask, request, jsonify
import google.auth
from googleapiclient.discovery import build
import json
api_key = 'a08bccac56msh7b70008bdbde837p1675a8jsn21112ad9629c' 
youtube = build('youtube', 'v3', developerKey=api_key)

app = Flask(__name__)
def fetch_comments(video_id):
    comments = []
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=50
        )
        response = request.execute()
        print("API Response:", response)
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            comments.append(comment)
        with open("fetched_comments.json", "w") as file:
            json.dump(comments, file, indent=4)

        print("Fetched comments saved to fetched_comments.json")

    except Exception as e:
        print("Error fetching comments:", e)

    return comments
def analyze_sentiments(comments):
    sentiment_summary = {
        "positive": 0,
        "negative": 0,
        "neutral": 0
    }
    for comment in comments:
        # Placeholder sentiment analysis
        if "good" in comment or "great" in comment:
            sentiment_summary["positive"] += 1
        elif "bad" in comment or "poor" in comment:
            sentiment_summary["negative"] += 1
        else:
            sentiment_summary["neutral"] += 1

    return sentiment_summary
def save_to_file(data):
    try:
        with open("output.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Results saved to output.json")
    except Exception as e:
        print("Error saving results:", e)
@app.route('/analyze-comments', methods=['POST'])
def analyze_comments():
    try:
        data = request.json
        video_id = data.get("videoId")

        if not video_id:
            return jsonify({"error": "videoId is required"}), 400
        comments = fetch_comments(video_id)

        if not comments:
            return jsonify({"error": "No comments found"}), 404
        sentiment_results = analyze_sentiments(comments)
        output = {
            "videoId": video_id,
            "sentiments": sentiment_results
        }
        save_to_file(output)
        return jsonify(output)

    except Exception as e:
        print("Error analyzing comments:", e)
        return jsonify({"error": "An error occurred while processing the request"}), 500

if __name__ == '__main__':
    app.run(debug=True)
