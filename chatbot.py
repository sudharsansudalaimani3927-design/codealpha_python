def greet(name):
    print("Welcome to chatbot",name)

def hi():
    print("Hi there!")

def response1():
    print("Yeah! Everything is fine! What about you?")

def response2():
    print("Sounds good!")

def date():
    print("It's 16th June, 2026, Tuesday")

def bye(name):
    print("See you later,",name)

name = input("Enter your name: ")
greet(name)

while True:
    prompt = input("Your prompt: ")

    if "hi" in prompt.lower():
        hi()

    elif "how are you" in prompt.lower():
        response1()

    elif "fine" in prompt.lower():
        response2()

    elif "date" in prompt.lower() or "day" in prompt.lower():
        date()
    
    elif "bye" in prompt.lower():
        bye(name)
        break

    else:
        print("Prompt undefined!")
        

    

    

