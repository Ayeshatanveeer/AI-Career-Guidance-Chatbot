with open("data.txt", "r", encoding="utf-8") as file:
    knowledge = file.read()

print("Career Guidance Chatbot")
print("Type exit to quit")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    elif "internship" in question.lower():
        print("Bot: Internships help students gain practical experience.")

    elif "interview" in question.lower():
        print("Bot: Practice common questions and research the company.")

    elif "career" in question.lower():
        print("Bot: Choose a career based on your interests and skills.")

    else:
        print("Bot: I can help with career guidance, internships and interviews.")