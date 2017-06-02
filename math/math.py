import re,math
from semantic.solver import MathService
from num2words import num2words

def text2int (textnum, numwords={}):
    if not numwords:
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

#        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ""
    onnumber = False
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                if onnumber:
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
            else:
                scale, increment = numwords[word]

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True

    if onnumber:
        curstring += repr(result + current)

    return curstring

def doSomethingElse(): return "Common dont be and idiot. Gemme a operation to perform"
def add(first,second):
    return first + second
def subs(first,second,nfrom):
    if nfrom == "from": return second - first
    else: return first - second
def mul(first, second):
    return first * second
def div(first, second):
    return first / second
def root(first):
    return math.sqrt(first)
def power(first,second):
    return math.pow(first, second)
def log(first):
    return math.log10(first)
def calc(string):
    service = MathService()
    return service.parseEquation(string)


while True:
    text = raw_input("Enter")
    numText = text2int(text)
    nfrom = ""
    second = 1
    nums = [int(s) for s in numText.split() if s.isdigit()]
    try:
        first = nums[0]
        second = nums[1]
    except:
        first = nums[0]

    if "from" in numText:
        nfrom = "from"

    op = {"log": log(first),"add":add(first,second),"substract":subs(first,second,nfrom),"divi":div(first,second),
         "multipl":mul(first,second),"square root":root(first),"raise":power(first,second),"plus":add(first,second),
         "minus":subs(first,second,None), "into": mul(first,second), "Calculator": calc(text)}

    try:
        m = re.search("|".join(op), numText).group()
        ans = op.get(m, doSomethingElse())
        print num2words(ans, lang="en_IN")
    except:
        print "No op found"
