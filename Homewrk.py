#task1
#Answer1
python_reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]

keyword = ["good", "excellent", "bad", "poor", "average"]
def keyword_highlighter(review, keyword):
    for keywords in keyword:
        review = review.replace(keywords, keywords.upper())
    return review

for review in python_reviews:
    highlighted_review = keyword_highlighter(review, keyword)
    print(highlighted_review)
#Task2
#Answer1 
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally_count(review, positive_words, negative_words):
    positive_count = 0
    negitive_count = 0
    words = review.lower().split()
    for word in words:
        if word.strip(".!,") in positive_words:
            positive_count += 1
        elif word.strip(".!,") in negative_words:
            negitive_count += 1

    return positive_count, negitive_count

def final_reviews(reviews, positive_words, negative_words):
    for review in reviews:
        pos_count, neg_count = tally_count(review, positive_words, negative_words)
        print(f"Review: \"{review}\"")
        print(f"Positive words: {pos_count}, Negative words: {neg_count}")
        print("-" * 50)

final_reviews(python_reviews, positive_words, negative_words)

#ExtraCredit
def first_thirty(reviews, thrty_char=30):
    if len(reviews) > thrty_char:
        summ_cap = reviews[:thrty_char].rstrip()
    if not summ_cap.endswith(" "):
        last_fin = summ_cap.rfind(" ")
    if last_fin != -1:
            summ_cap =summ_cap[:last_fin]
            return summ_cap + "..."
    else:
        return reviews
    
for review in python_reviews:
    end = first_thirty(review)
    print(f"review: {end}")