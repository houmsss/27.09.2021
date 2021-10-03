import requests
import re
from collections import Counter
import nltk 
from nltk import pos_tag
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

r = requests.get('https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt')
result = r.content.decode("utf-8")
split = re.findall(r"[\w']+|[.,!?;]", result)

print("After Split:",split)
tokens_tag = pos_tag(split)
print("After Token:",tokens_tag)

counts = Counter(y for _,y in tokens_tag)
print(counts)
sort = sorted(tokens_tag,key = lambda p:counts[p[1]],reverse = True)
print(sort)
