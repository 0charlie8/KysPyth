def main(x):
  
  x = x.replace ('\n', ' ')\
  .replace (' do loc', '')\
  .replace ('do loc', '')\
  .replace ('::=', ' ')\
  .replace ('end.', '')\
  .replace ('::=', '')\
  .replace (' ', ' ')\
  .replace ('(( ', '')\
  .replace ('))', '')\
  .replace ('(( ', '')\
  .replace ('))', '')
  result = x.split()
  itog = []
  for i in range (0, len(result), 2):
  itog.append ((result[i],result[i+1]))
  return itog

print (main('((do loc xeanat::= ques_529 end. do loc xeti::=rari end. do loc edre\n::=erdiza_573 end. ))'))
