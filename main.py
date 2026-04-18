import language_tool_python

def grammar_checker():
    tool = language_tool_python.LanguageTool('en-US')

    text = input("Enter your sentence: ")

    matches = tool.check(text)
    corrected_text = tool.correct(text)

    print("\nOriginal:", text)
    print("Corrected:", corrected_text)

grammar_checker()