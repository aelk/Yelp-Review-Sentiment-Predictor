import json

def numLines(filename):
    return sum(1 for line in open(filename))

def loadData(filename, startLine, endLine, posneg=True):
    data, labels = [], []
    i = 0

    for line in open(filename, 'r'):
        if i > endLine:
            break
        elif i >= startLine:
            obj = json.loads(line)
            data.append(obj['text'])

            if posneg:
                #if obj['stars'] >= 3: labels.append('pos')
                #else: labels.append('neg')
                if obj['stars'] >= 3: labels.append(1)
                else: labels.append(0)
            else:
                labels.append(obj['stars'])

        i += 1

    return data, labels
