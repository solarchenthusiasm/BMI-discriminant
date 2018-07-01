h = input('please key in your height_using meter as unit')
w = input('please key in your weight_using kilogram as unit')
h = float(h)
w = float(w)
b = w / h / h
if b < 18.5 :
	print('your bmi is', b, 'too thinner')
elif b >= 18.5 and  b < 24 :
	print('your bmi is', b, 'health status')
elif b >= 24 and b < 27 :
	print('your bmi is', b, 'chubby')
elif b >=27 and b < 30 :
	print('your bmi is', b, 'light heavy')
elif b >= 30 and b < 35 :
	print('your bmi is', b, 'heavier')
elif b >= 35 :
	print('your bmi is', b, 'fat')
	