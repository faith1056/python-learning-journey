feedback = [
    "The jollof rice was delicious.",
    "The chicken was terrible.",
    "I loved the food.",
    "My delivery was late.",
]

positive_keywords = ["delicious", "loved", "excellent", "amazing", "great"]
negative_keywords = ["terrible", "late", "bad", "cold", "disappointed"]


def analyze_feedback(reviews):
    positive_count = 0
    negative_count = 0
    other_count = 0

    for review in reviews:
        review = review.lower()

        has_positive = any(word in review for word in positive_keywords)
        has_negative = any(word in review for word in negative_keywords)

        if has_positive and not has_negative:
            positive_count += 1
        elif has_negative and not has_positive:
            negative_count += 1
        else:
            other_count += 1

    return positive_count, negative_count, other_count


positive, negative, other = analyze_feedback(feedback)

print("=== Express Bites Feedback Report ===")
print(f"Total reviews: {len(feedback)}")
print(f"Positive reviews: {positive}")
print(f"Negative reviews: {negative}")
print(f"Other or mixed reviews: {other}")
