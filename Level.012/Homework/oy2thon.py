#3) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები
temperature = 35
cloudy = False

result1 = temperature > 30 and not cloudy
print(result1)  # True

age = 14
result2 = age > 18 or age == 14
print(result2)  # True

number = 10
result3 = number > 20 and number < 30
print(result3)  # False

score = 85
result4 = score >= 80 and score != 100
print(result4)  # True

money = 5
result5 = money > 10 or not money == 5
print(result5)  # False