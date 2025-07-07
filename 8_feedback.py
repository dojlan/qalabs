from pathlib import Path

# list of students
students = {}

"""Students performance measured in as scores"""
performance = {1:"ok", 2:"good", 3:"excellent", 4:"outstanding"}

while True:
    print("Welcome to the Student Feedback Program!")
    # - Get student names from the user until they enter 'Q' to quit.
    """ Store the names in a dictionary called "students". """
    student = input("Enter student name (or 'Q' to quit): ") 
    if student.strip().lower() == 'q':
        print("Goodbye!!")
        break
    score = int(input(f"Enter score for {student}: "))
    students[student] = score

    """Performance summary for each student."""
    template = f"General comments\n{student} did {performance[score]} in this module.\n\
{student} demonstrated a good understanding of concepts we covered and has shown a \n\
broad knowledgebase. {student} contributed to discussions and asked relevant questions."
    
    template += f"\n\nLearner Punctuality and engagement \n{student} was punctual throughout \
the module and engaged well through Webex."
    
    template += f"\n\nRecommendations on further learning\n{student} continued to practice the \
basics of containerisation, Kubernetes and pipelines."
    print("-" * 20)

    """Create a directory and a file for each student."""
    file_path = "./Coding/feedback"
    Path(file_path).mkdir(parents=True, exist_ok=True)
    new_user = f"{file_path}/{student}"
    with open(new_user + ".txt", "w") as write_to_file:
        write_to_file.write(template)

    # Open the file again, to read..
    with open(new_user + ".txt", "r") as read_from_file:
        print(read_from_file.read())
        read_from_file.close()
