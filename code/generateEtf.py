import json
import collections

theTags=[]
etfFile=""

def dumpStruct():
    return f"# List of ETFs\n\n"

def getEtfListForWrite(iEtfRaw):
    etfFile=""
    for etf in iEtfRaw:
        etfFile = etfFile + "## " + etf['name'] + "\n" + etf['description'] + "\n\n"
    return etfFile

def writeOutputFile(iDestFile, iContent):
    f = open("../etf.md", "w")
    aTextToWrite=dumpStruct()
    aTextToWrite=aTextToWrite + getEtfListForWrite(iContent)
    f.write(aTextToWrite)
    f.close()

def processEtfJson(iSrcFile):
    with open(iSrcFile) as json_file:
        data = json.load(json_file)
        return data

aEtfsRaw = processEtfJson("../etf.json")

writeOutputFile("../etf.md", aEtfsRaw)
