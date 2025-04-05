def convert_indian_to_arabic(indian_number):
    arabic_digits = {
        '٠': '0', '١': '1', '٢': '2', '٣': '3',
        '٤': '4', '٥': '5', '٦': '6',
        '٧': '7', '٨': '8', '٩': '9'
    }
    if all(num in arabic_digits.values() or num.isdigit() for num in indian_number):
        print("This is an Arabic number, not an Indian number.")
        return None
    result = ''
    for num in indian_number:
        if num in arabic_digits:
            result += arabic_digits[num]
        else:
            result += num 
    return result



input = input("Enter Indian Number ") 
output = convert_indian_to_arabic(input) 
print(f" Arabic Number Of : {input}  Is:  {output}")
