import html

try:
    import requests
except ModuleNotFoundError:
    print("The requests module is not installed. Run: pip install requests")
    question_data = []
else:
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()

    data = response.json()
    question_data = []

    for question in data["results"]:
        question_data.append({
            "question": html.unescape(question["question"]),
            "correct_answer": question["correct_answer"],
        })
