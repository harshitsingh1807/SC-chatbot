from openai import OpenAI

client = OpenAI(
    api_key="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",
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please "},
        {"role":"user","content" : "what is coding"}
    ]
)
print (completion.choices[0].message.content)
