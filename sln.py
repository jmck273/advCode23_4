def getContent(fileURL):
    '''
    Getting the content of the URL. To not overwhelm the Advent of code server, I have saved
    the file locally as a text file. There shouldn't be the need for these exceptions as I have included the
    text file in the repo, but it is meant to be good coding practices
    '''
    try:
        with open(fileURL, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{fileUrl}' not found")
        return None
    except Exception as e:
        print(f"Error Occurred: {e}")
        return None
    
def getPoints(textIn):
    retSum = 0
    for texts in textIn:
        print(texts)
        #Hardcoding that there are two splits
        text1, text2 = texts.split("|")
        text1SetBad, text1SetUse = text1.split(":")
        text1Set = set(text1SetUse.strip().split())
        text2Set = set(text2.strip().split())
        counter = len(text1Set.intersection(text2Set))
        if counter > 0:
            retSum += (2**(counter-1))
    return retSum

def partTwo(textIn):
    textLen = len(textIn)
    countDict = dict()
    #Initialize dict values at 0
    for i in range(textLen):
        countDict.update({i:1})
    countDict[0] = 1
    for i in range(textLen):
        if(countDict[i] == 0): continue
        text1, text2 = textIn[i].split("|")
        text1SetBad, text1SetUse = text1.split(":")
        text1Set = set(text1SetUse.strip().split())
        text2Set = set(text2.strip().split())
        
        for count in range(countDict[i]):
            counter = len(text1Set.intersection(text2Set))
            if counter > 0:
                for j in range(1,counter+1):
                    countDict[i+j] += 1
    return sum(countDict.values())
    
if __name__ == "__main__":
    textStr = getContent("input.txt")
    textSplit = textStr.splitlines()
    print(getPoints(textSplit))
    print(partTwo(textSplit))
