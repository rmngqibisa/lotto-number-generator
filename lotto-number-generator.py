import random

def predict_next_lottery_numbers(previous_numbers):
    if len(previous_numbers) < 6 :
        return "Insufficient data for prediction. Provide more past lottery numbers."

    # Calculate the average of the previous numbers
    average = sum(previous_numbers) / len(previous_numbers)

    # Generate a set of random numbers around the average
    predicted_numbers = [int(average + random.uniform(-5, 5)) for _ in range(7)]

    return predicted_numbers

# Example uses South African Lottery Numbers from draw date 17 Jan 2024
previous_lottery_numbers = [20, 30, 32, 40, 47, 52, 41]
predicted_numbers = predict_next_lottery_numbers(previous_lottery_numbers)


print("Predicted Lottery Numbers:", predicted_numbers)
