import openai

openai.api_key = "YOUR_AZURE_OPENAI_KEY"

def summarize(transcript):
    """
    Summarize meeting transcript and extract action items.
    """
    prompt = f"""
    以下は会議の議事録です。
    1. 3行以内の要約
    2. アクションアイテム（To Do形式）を出力してください。

    ---
    {transcript}
    """

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    sample_transcript = "本日は新製品の発売日程を決定..."
    print(summarize(sample_transcript))
