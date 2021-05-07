class DataHandler:
    def __init__(self, path):
        self.type = pathlib.Path(path).suffix
        self.dataset_location = path
        
        #Use the pandas dataframe to get columns 
        if self.type == '.csv':
            self.df = pd.read_csv(path)
            self.df = self.df[self.df['Domain'] == "CS "]
        elif self.type == '.xlsx':
            self.df = pd.read_excel(path)
            self.df = self.df[self.df['Domain'] == "CS "]

    def getDataframe(self):
        return self.df