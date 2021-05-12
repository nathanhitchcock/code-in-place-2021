SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type an noun and press enter. ") 
    verb = input("Please type an verb and press enter. ")
    compile_sentence(adjective, noun, verb)

def compile_sentence(adjective, noun, verb):
    print(SENTENCE_START + adjective + noun + verb)


if __name__ == "__main__":
    main()
