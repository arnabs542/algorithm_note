import pandas as pd
import numpy as np

class NpvIrr:
    # file should be the data
    def __init__(self, data, header = True):
        # load input data, csv file
        self.data = self.__read_file(data)
        self.years = self.data.columns.tolist()
        self.users = self.data.index.tolist()
        self.n_years = self.data.shape[1]
        self.n_users = self.data.shape[0]

        # other data need to be stored
        self.rate = None
    
    """
    data is the address of the input csv file, should be str

    desc: the input data should have header, and all header of years should be integer, and also should have row name (index) which could be string
    """
    # inner helper function to read the data.csv
    def __read_file(self, data):
        data = pd.read_csv(data, index_col = 0)
        return data
    
    # compute the npv
    """
    rate should be int
    data should be pandas dataframe
    """
    def __computeNpv(self, rate, data):
        self.rate = rate
        data = pd.DataFrame(data)
        data['npv'] = data.iloc[:, :self.n_years].apply(lambda x: round(np.npv(rate, x),2), 1)
        return data

    # compute the irr, numpy irr has some bugs
    """
    data should be pandas dataframe
    """
    def __computeIrr(self, data):
        data = pd.DataFrame(data)
        data['irr'] = data.iloc[:, :self.n_years].apply(lambda x: round(np.irr(x) * 100, 2), 1)
        
        return data 
    
    # get result
    def getResult(self, rate):
        self.data = self.data.iloc[:, :self.n_years]
        self.data = self.__computeIrr(self.data)
        self.data = self.__computeNpv(rate, self.data)
        return

    # add a new user for data
    """
    users_name should be list[str]
    users_data should be list[list[]]

    desc: add new users data into the NpvIrr object, it will keep the previous analysis results and generate new results if possible.
    """
    def addUsers(self, users_name, users_data):
        if len(users_data[0]) != self.n_years:
            raise ValueError('new user\'s investment years should be equal to the previous user\'s investment years')

        # if we haven't computed irr npv
        if self.n_years == self.data.shape[1]:
            users_data = pd.DataFrame(users_data, index = users_name, columns = self.data.columns)
            self.data = self.data.append(users_data)

        # if we have computed irr npv
        else:
            users_data = pd.DataFrame(users_data, index = users_name)
            print(users_data)
            users_data = self.__computeIrr(users_data)
            users_data = self.__computeNpv(self.rate, users_data)
            users_data.columns = self.data.columns
            self.data = self.data.append(users_data)

        self.n_users = self.data.shape[0]
        self.users = self.data.index.tolist()

        return

    # add years for users
    """
    years_data should be list[list[float]]

    desc: it will clear all analysis results before, and perform new analysis using the same rate
    """
    def addYears(self, years_data):
        for l in years_data:
            if len(l) != self.n_users:
                raise ValueError("Input years_data should have the same length of users, noting changed.")
                return

        # check whether we performed analysis before
        if self.n_years != self.data.shape[1]:
            flag = True
        else:
            flag = False

        self.data = self.data.iloc[:, :self.n_years]

        # get the previous year number
        if self.years[-1].isdigit():
            prev_year = int(self.years[-1])
        else:
            raise ValueError("Invalid year column.")
        
        # add year information one by one
        for i in range(len(years_data)):
            curr_year = str(prev_year + 1)
            self.data[curr_year] = years_data[i]
            self.years.append(curr_year)
            self.n_years += 1
            prev_year += 1

        if flag:
            self.getResult(self.rate)
        return

    # get the user data, by using one name or a range of user index
    def getData(self, num = (0, 5), names = []):
        if names != []:
            return self.data.loc[names].values

        print('Invalid user')
        return

    # show the result
    def showResults(self):
        if len(self.data.columns) == self.n_years:
            print('Warning: no analysis performed before.')
            return
        
        # iteate each user
        for i in range(len(self.users)):
            print(self.users[i], '\'s cash flow:', end = ' ')
            # the cash flow for the user
            for j in range(self.n_years):
                print(self.data.iloc[i,j], end=' ')
            print()

            if 'npv' in self.data.columns:
                print('The Net Present Value (NPV) is: %f with rate of: %s %s' % (self.data['npv'].iloc[i], str(100 * self.rate), '%'))
            if 'irr' in self.data.columns:
                print('The  Internal Rate of Return (IRR) is: %s %s' % (self.data['irr'].iloc[i], '%'))
            print()
                
        return 
    
    # print pd.dataframe
    def summary(self, dataframe = True):
        if self.rate:
            print("current rate is: %s; number of users is: %s; number of years is: %s" % (self.rate, self.n_users, self.n_years))
        else:
            print("current number of users is: %s; number of years is: %s" % (self.n_users, self.n_years))

        if dataframe:
            print(self.data)
        return
    
    # output to a file, csv
    def save_csv(self, addr):
        self.data.to_csv(addr)
        return

data = 'C:\\Users\\liuyu\\Desktop\\2019_summer\\metcs\\data.csv'
solver = NpvIrr(data)
temp = solver.getData(names=['consideration'])
print(temp)
print("before computation")
solver.summary()
print("add users before computation")
solver.addUsers(['6', '7'], [[-10000, 800, 8000, 837, 900, 1000], [-19423, 9872, 8762, 1093, 500, 198]])
solver.summary()
print("add years before computation")
solver.addYears([[-1000,928,2324,234,9288,8631,5973,9428]])
solver.summary()
print("after computation")
solver.getResult(.05)
solver.summary()
print("after computation2")
solver.getResult(.01)
solver.summary()
print("add users after computation")
solver.addUsers(['8', '9'], [[-4632, 800, 800, 83, 900, 1261, 1000], [9423, -987, 1862, 1093, 5040, 1898, -222]])
solver.summary()
print("add years after computation")
solver.addYears([[1000,3000,200,4000,400,200,-1000,9000, 150, 1000],[42,250,3453,2309,-453,3000,31,35,4367,8763]])
solver.summary()

solver.save_csv('C:\\Users\\liuyu\\Desktop\\2019_summer\\metcs\\result.csv')

temp = solver.getData(names=['buttocks'])
print(temp)
solver.showResults()

    # # get the result
    # """
    # names contains all queries of names, it should be a list[str]
    # """
    # def showResult(self, names = None):
    #     for idx, user in enumerate(self.users):
    #         if names == user:
    #             return self.data.iloc[idx, :self.n_years].values
    #     print('Invalid user')
    #     return
