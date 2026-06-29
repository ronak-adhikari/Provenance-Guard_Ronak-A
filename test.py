import requests

tests = [
    {
        "text": "Artificial intelligence represents a transformative paradigm shift in modern technological development. By leveraging advanced machine learning algorithms, organizations can optimize their operational efficiency and drive sustainable growth.",
        "creator_id": "test-user-1"
    },
    {
        "text": "ok so i tried making sourdough again and it was... not great lol. the crust was good but inside was basically a gummy mess. i think i let it proof too long? anyway my roommate ate three slices so maybe it wasnt that bad",
        "creator_id": "test-user-2"
    },
    {
        "text": "The morning light filtered through the curtains as she reached for her coffee. Some days felt heavier than others, though she couldn't quite explain why.",
        "creator_id": "test-user-3"
    }
]

for t in tests:
    response = requests.post("http://127.0.0.1:5000/submit", json=t)
    print(response.json())
    print()