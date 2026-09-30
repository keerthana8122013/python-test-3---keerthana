grade_book = {
    "Bob": 88,
    "Larry": 92,
    "Jim Bob": 75,
    "Gary": 85,
    "Chad": 81
}
print("----Student Grade Book----")
for name, score in grade_book.items():
    print(f"{name}: {score}")
    print("-"*26)

    total_score = 0
    for score in grade_book.values():
        total_score += score

        class_average = total_score / len(grade_book)
        print(f"Class Average: {class_average:.2f}")

        top_scorer = max(grade_book, key=grade_book.get)
        print(f"Top Scorer: {top_scorer} with a score of {grade_book[top_scorer]}")
        bottom_scorer = min(grade_book, key=grade_book.get)
        print(f"Bottom Scorer: {bottom_scorer} with a score of {grade_book[bottom_scorer]}")
        print("-"*26)

        search_name = input("Enter a student's name to search for their score: ")
        if search_name in grade_book:   
            print(f"{search_name}'s score: {grade_book[search_name]}")
        else:
            print(f"{search_name} is not in the grade book.")

            


