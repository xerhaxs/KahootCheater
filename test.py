import requests
import json
import credentials

def get_kahoot(kahootid):
    response = requests.get('https://create.kahoot.it/rest/kahoots/{}'.format(kahootid), headers={'content-type' : 'application/json','authorization'}).json()

    questions = []

    if 'error' in response:
        print("No Kahoot Found!")
        exit()
    else:
        print("FOUND Kahoot titled: '" + response["title"] + "'")

        for i in range(0, len(response["questions"])):
            currentQuestion = {"question": "", "answer": ""}

            currentQuestion["question"] = response["questions"][i]["question"]

            for j in range(0, len(response["questions"][i]["choices"])):
                if response["questions"][i]["choices"][j]["correct"] == True:
                    currentQuestion["answer"] = response["questions"][i]["choices"][j]["answer"]

            questions.append(currentQuestion)

        return questions


kahootid = input("Enter the quiz id from host URL: ")

questions = get_kahoot(kahootid)

print("\nAll Questions: " + str(questions))
