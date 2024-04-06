from openai import OpenAI


api_key = "Your-Api-Key"
client = OpenAI(api_key=api_key)

while True:
    tempInput = input("\nUSER: ")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": 'your content',
            },
            {"role": "user", "content": f"{tempInput}"},
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    print("HILAL: ", response.choices[0].message.content)
