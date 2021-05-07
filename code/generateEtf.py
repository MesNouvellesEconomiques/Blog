import json
import collections

theTags=[]
etfFile=""

def dumpStruct():
    return f"# List of ETFs\n\n"

def dumpSector():
    return f"# List of Sectors\n\n"

def getEtfListForWrite(iEtfRaw):
    etfFile=""
    for etf in iEtfRaw:
        etfFile = etfFile + "## " + etf['name'] + "\n" + etf['description'] + "\n\n"
    return etfFile

def getEtfMatchingSector(iEtfsRaw, iOneSector):
    for aOneEtf in iEtfsRaw:
        if iOneSector["tags"] in iEtfsRaw["tags"]:
            print(f"{aOneEtf} match")

def getSectorListForWrite(iSectorRaw, iEtfsRaw):
    SectorContent=""
    for aOneSector in iSectorRaw:
        SectorContent = SectorContent + "## " + aOneSector['theme'] + "\n" + aOneSector['description'] + "\n\n"
        # Find the ETF for this sector
        getEtfMatchingSector(iEtfsRaw, aOneSector)
    return SectorContent

def writeOutputFile(iDestFile, iContent):
    f = open("../etf.md", "w")
    aTextToWrite=dumpStruct()
    aTextToWrite=aTextToWrite + getEtfListForWrite(iContent)
    f.write(aTextToWrite)
    f.close()

def writeSectorOutputFile(iDestFile, iSectorsRaw, iEtfsRaw):
    f = open(iDestFile, "w")
    aTextToWrite=dumpSector()
    aTextToWrite=aTextToWrite + getSectorListForWrite(iSectorRaw = iSectorsRaw,iEtfsRaw=iEtfsRaw)
    f.write(aTextToWrite)
    f.close()

def processEtfJson(iSrcFile):
    with open(iSrcFile) as json_file:
        data = json.load(json_file)
        return data

def processSectorJson(iSrcFile):
    with open(iSrcFile) as json_file:
        data = json.load(json_file)
        return data

aEtfsRaw = processEtfJson("../etf.json")
aSectorsRaw = processSectorJson("../sectors.json")

writeOutputFile("../etfs.md", aEtfsRaw)
writeSectorOutputFile(iDestFile = "../sectors.md", iSectorsRaw = aSectorsRaw,iEtfsRaw = aEtfsRaw)
