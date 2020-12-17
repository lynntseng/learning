chinese = input('請輸入國文分數 : ')
chinese = float(chinese)

math = input('請輸入數學分數 : ')
math = float(math)

english = input('請輸入英文分數 : ')
english = float(english)

score = (chinese + math + english) / 3
score = float(score)

print('你的平均分數 : ' , score)

if score >= 95 :
     print('你的成績 : ' ,'A+')
elif 95 > score >= 85 :
      print('你的成績 : ','A') 
elif 85 > score >= 80 :
     print('你的成績 : ' ,'B') 
elif 80 > score >= 75 :
     print('你的成績 : ' ,'C')  
else :
     print('你的成績 : ' ,'D') 