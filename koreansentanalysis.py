import polyglot
from konlpy.corpus import my_corpus
from konlpy.tag import Hannanum
from konlpy.utils import concordance, pprint
from matplotlib import pyplot
from konlpy.tag import Kkma


from polyglot.text import Text

with open('vegetariankoreansister.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')

kkma = Kkma()

sentlist = (kkma.sentences(data))

sentpolarity = 0
senttotal = 0
sentcount = 0

for i in sentlist:
	text = Text(i, hint_language_code='ko')

	for w in text.words:
		senttotal += w.polarity
		sentcount+=1

	sentpolarity = senttotal/sentcount
	print(i)
	sentpolarity = 0
	senttotal = 0
	sentcount = 0