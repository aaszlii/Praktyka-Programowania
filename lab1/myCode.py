def Add(numbers):
    if not numbers:
        return 0
    if ",\n" in numbers or "\n," in numbers:
        raise ValueError("Blad")
    delimiters = [",","\n"]
    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ",")
    return sum(int(num)for num in numbers.split(",") if num)