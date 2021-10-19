# To use the website, duh
import wikipedia
import sumy
import nltk


# Welcome the users to improve user experience
def intro():
    # updated instructions to include the summarizing option
    instructions = "\n\nWelcome to my very first AI project: Researching AI Assistant!" \
                   "\nThis assistant is quite easy to use. " \
                   "\nType \"Y\" or \"N\" when prompted, otherwise type normally to answer questions." \
                   "\nAll your research will automatically be saved to a text document." \
                   "\nYou will have the option to summarize your research if you wish. " \
                   "\nYour research summary will automatically be saved into a separate text document." \
                   "\n\nNow you know how to use my Researching AI Assistant!"

    print(instructions)
    # add_to_file(file, intro)

    question_readiness = "\n\nAre you ready to get started? Type Y or N."
    # add_to_file(file, question_readiness + "\n")

    ready_ans = input(question_readiness)
    # add_to_file(file, ready_ans + "\n")
    ready_ans = ready_ans.upper()

    if ready_ans == "Y" or ready_ans == "YES":
        return True
    else:
        double_check_readiness = "\n\nAre you sure you want to exit? Type Y or N."

        double_check_ans = input(double_check_readiness)
        double_check_ans.upper()

        if double_check_ans == "Y" or double_check_ans == "YES":
            return False
        elif double_check_ans == "N" or double_check_ans == "NO":
            return True
        else:
            print("\n\nNo viable answer could be found.\nTry again later.")
            return False


def summarize(summarizing_file):
    try:
        research_file = open("Research Raw Data.txt", "r")
    except IOError:
        print("Could not open file for research!")
    with research_file:
        from sumy.parsers.plaintext import PlaintextParser
        from sumy.nlp.tokenizers import Tokenizer
        from sumy.summarizers.lex_rank import LexRankSummarizer
        parser = PlaintextParser.from_string(research_file.read(), Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary_length = input("How many sentences would you like summary to be? \nEx: 1, 2, 3, etc.\n"
                               "Number of sentences: ")
        summary_length = int(summary_length)
        # summary is a tuple
        summary = summarizer(parser.document, summary_length)
        print("\n\nSummary: \n")
        add_to_file(summarizing_file, "Summary: \n")
        for sentence in summary:
            print(sentence) # issue "Sentence" is an object
            summarizing_file.write(str(sentence))


def create_essay(file, research_topic):
    # Create a variable to hold the wiki page info
    research_page = wikipedia.page(research_topic, auto_suggest=False)

    # display the page to the screen
    print(f"\n\n\t\t*** {research_topic.upper()} ***")
    title = f"\n\n\t\t*** {research_topic.upper()} ***\n"
    add_to_file(file, title)
    print("_" * 50 + "\n")
    formatting = "_" * 50 + "\n"
    add_to_file(file, formatting)

    print("\n\t\t*** Content ***\n")
    add_to_file(file, "\n\t\t*** Content ***\n")
    raw_content = research_page.content.replace("== References ==", " ")
    print(raw_content)
    add_to_file(file, raw_content)
    print("_" * 50)
    add_to_file(file, formatting)

    print("\n\t\t*** References ***\n")
    add_to_file(file, "\n\t\t*** References ***\n")
    raw_references = research_page.references
    for each_ref in raw_references:
        ref = each_ref + "\n"
        print(each_ref)
        add_to_file(file, ref)
    # print(research_page.references)
    print("_" * 50)
    add_to_file(file, formatting)


def add_to_file(file, string_to_add):
    # raw_file = open("Research Raw Data.txt", "wb")
    # encoded_string = string_to_add.encode("utf8")
    file.write(string_to_add.encode("ascii", "ignore").decode())


def conclusion():
    print("\n\nThank you for using my first AI.")
    print("Improvements will continue to be made to improve this AI assistant.")
    print("Until next time, have a good day!")


def main():
    try:
        raw_file = open("Research Raw Data.txt", "w")  # "a+", for appending to a file
    except IOError:
        print("Could not open file for research!")
    with raw_file:
        # print("Time to write to a file!")
        proceed = intro()
        again = False

        while not again:
            if proceed:
                print("\n\n", "_" * 50, "\n")
                what_to_research_question = "\t\tWhat would you like to research?\n\t\tTopic: "
                research_topic = input(what_to_research_question)
                create_essay(raw_file, research_topic)
                keep_going_status = input("\t\tWould you like to research something else?\nType Y or N: ")
                keep_going_status = keep_going_status.upper()

                if keep_going_status == "N" or keep_going_status == "NO":
                    again = True
                    # Ask user if they would like their research summarized.
                    summarize_research = input("\nWould you like to summarize your previous research?\nType Y or N: ")
                    summarize_research = summarize_research.upper()
                    if summarize_research == "Y" or summarize_research == "YES":
                        try:
                            sum_raw_file = open("Summarized Research.txt", "w")
                        except IOError:
                            print("Could not open file for summary!")
                        with sum_raw_file:
                            raw_file.close()
                            # close research file for writing and open it for reading?
                            # Then send both files to the summarize method?
                            # or open research.txt in summarize method and just send summary file?
                            summarize(sum_raw_file)
                            print("\nSummary Complete. Summary Saved.")

        # End of while loop
        # Indicates the user is done using the AI assistant
        # Complete the closing actions for the program below
        conclusion()
        raw_file.close()
        sum_raw_file.close()
        exit()


if __name__ == '__main__':
    main()
