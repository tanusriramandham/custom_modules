def count_vowels(s):
    vowels='aeiouAEIOU'
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return f"the count of vowels in your string is :{count}"