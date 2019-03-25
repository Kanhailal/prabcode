from flask import Flask
from flask import request
import emoji
import re
app = Flask(__name__)
@app.route('/spellCorrect',methods=['get', 'post'])
def WordCheck():
	string = request.form.get('str')
	RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
	if RE_EMOJI.search(string):
		string=RE_EMOJI.sub(r'', string)
	fullSen=[]
	if len(string.split()) > 1 or "-" in string:
		splitstr=string.replace('-',' ').split()
		for wrd in splitstr:
			fullSen.append(wordBreak(wrd.lower()))
	
	else:
		fullSen.append(wordBreak(string.lower()))
	print(' '.join(fullSen))
	return (' '.join(fullSen))


def wordBreak(s):
	dict=["home","assignment","school","bag"]
	segmented = [True];
	finWord=[]
	for i in range (0, len(s)):
		segmented.append(False)
		for j in range(i,-1,-1):
			if segmented[j] and s[j:i+1] in dict:
				segmented[i+1] = True
				finWord.append(s[j:i+1])
				break
	if finWord:
		return (' '.join(finWord))
	else:
		return (s)
	return ""


if __name__ == '__main__':
    app.run(port=5000,debug=True)

