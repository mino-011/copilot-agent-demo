import requests

ACCESS_TOKEN = "YOUR_GRAPH_API_TOKEN"
MEETING_ID = "YOUR_MEETING_ID"

def fetch_meeting_transcript():
    """
    Fetch meeting transcript from Microsoft Graph API.
    """
    url = f"https://graph.microsoft.com/v1.0/communications/onlineMeetings/{MEETING_ID}/transcripts"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        transcript = response.json()
        return transcript.get("content", "")
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print(fetch_meeting_transcript())
