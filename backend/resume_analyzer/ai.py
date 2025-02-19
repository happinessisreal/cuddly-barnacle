import openai

def analyze_resume(content):
    # Use OpenAI's GPT-3 to analyze the resume content
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Analyze the following resume:\n\n{content}\n\nAnalysis:",
        max_tokens=150
    )
    analysis_results = response.choices[0].text.strip()
    return {"analysis": analysis_results}
