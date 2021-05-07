class PredictPaper:
    def __init__(self, dataPath, graphPath):
        self.dh = DataHandler(dataPath)
        self.dataset = self.dh.getDataframe()
        self.dataset = self.dataset.reset_index()
        self.g = Graph(10000)
        self.g.importNetwork(graphPath)
        self.querySet = []
        self.result = {}


    def predictUtil(self, queryKeyList):
        for queryKey in queryKeyList:
            queryKey = queryKey.strip().lower()
            queryDict = self.g.BFS(queryKey, 3)
            self.querySet.extend([queryKey])
            self.querySet.extend([item[0] for item in queryDict])
        return self.querySet


    # Gives sorted dictionary result of papers and number of matching keywords 
    # between input keywords and rake extracted keywords from abstract
    def predict(self, queryKeyList, commonWordsCount):
        self.querySet = self.predictUtil(queryKeyList)
        ran = len(self.dataset['Rake keywords'])
        for i in range(1000):
            val = self.dataset['Rake keywords'][i]
            keywords = val.split(";")
            com = self.calcCommon(keywords)
            if com >= commonWordsCount:
                self.result[i] = com
        self.result = dict(sorted(self.result.items(), key = lambda kv:(kv[1], kv[0]), reverse = True))
        for key in self.result:
            self.result[key] = [self.result[key], self.dataset['area'][key].strip().lower()]
        return self.result

    def calcCommon(self, keywords):
        cou = 0
        for w1 in self.querySet:
            for w2 in keywords:
                if(w1.strip().lower() == w2.strip().lower()):
                    cou+=1
        return cou