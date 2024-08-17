def weekday(day_number: int):
    list_of_tuples = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        # etc
    ]

    match day_number:
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case 7: return "Sunday"
        case _: return "Invalid day number"


print(weekday(5))
