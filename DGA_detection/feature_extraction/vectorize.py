from numpy import zeros
from math import log2

class vectorize:
    
    '''Takes a domain name as input and generates a feature vector'''
    
    def __init__(self,domain:str):
               
        self.domain = domain
        self.features = ["NUMBER OF CHARACTERS","NUMBER OF DIFFERENT CHARACTERS","C","V","1-GRAM MEAN","1-GRAM VARIANCE","1-GRAM STANDARD DEVIENCE","2-GRAM MEAN","2-GRAM VARIANCE","2-GRAM STANDARD DEVIENCE","CC","VC","CV","CCC","CVC","VCC","VCV","MAX FREAQUECNY CHARTER/TOTAL NUMBER OF CHARACTER","MIN FREAQUENCY CHARACTER/TOTAL NUMBER OF CHARACTER","SHANON ENTROPY","IN","ER","AN","RE","ES","AR","ON","OR","TE","AL","ST","NE","EN","ING","ION","INE","TER","LIN","ENT","THE","ERS","AND","EST","TIO","TRA","TOR","ART"]
        self.featureTable = dict.fromkeys(self.features ,[])
        self.vector = zeros((len(self.features),))
        cons = 'bcdfghjklmnpqrstvwxyz'
        vow = 'aeiou'
        self.masked = ''
        for i in self.domain:
            
            if i in cons:
        
                self.masked += 'c'
            elif i in vow:
                self.masked += 'v'
            elif i.isdigit():
                self.masked += 'n'
            else:
                self.masked += 's'
        
        self.totalChar()
        self.differentChar()
        self.consonant()
        self.vowel()
        self.__freaquency,u = self.oneGramStat()
        self.twoGramStat()
        self.masked2gram()
        self.masked3gram()
        self.most_least_ratio()
        self.shanon_entropy()
        self.most_freaquent_twoGram_freaquency()
        self.most_freaquent_threeGram_freaquency()
    
    def totalChar(self)->int:
        
        '''Used to get the length of the word'''
        
        self.vector[0] = len(self.domain)
        self.featureTable[self.features[0]] = len(self.domain)
        return len(self.domain)
    
    def differentChar(self)->int:
        self.vector[1] = len(set(self.domain))
        self.featureTable[self.features[1]] = self.vector[1]
        return self.vector[1]
    
    def consonant(self)->int:
        cons = 'bcdfghjklmnpqrstvwxyz'
        count = 0
        for i in self.domain:
            if i in cons:
                count += 1
        self.vector[2] = count
        self.featureTable[self.features[2]] = count
        return self.vector[2]
    
    def vowel(self)->int:
        vow = 'aeiou'
        count = 0
        for i in self.domain:
            if i in vow:
                count += 1
        self.vector[3] = count
        self.featureTable[self.features[3]] = count
        return count
    
    def oneGramStat(self)->dict:
        sequence = dict.fromkeys(self.domain,0)
        for i in self.domain:
            sequence[i] += 1
        self.vector[4] = self.vector[0]/self.vector[1]
        for i in sequence.values():
            self.vector[5] += (i-self.vector[4])**2
        self.vector[5] = self.vector[5]/(len(sequence) - 1)
        self.vector[6] = self.vector[5]**0.5
        self.featureTable[self.features[4]] = self.vector[4]
        self.featureTable[self.features[5]] = self.vector[5]
        self.featureTable[self.features[6]] = self.vector[6]
        
        return sequence,{'mean':self.vector[4],'variance':self.vector[5],'standard variance':self.vector[6]}
        
        
    
    def twoGramStat(self)->dict:
        i = 0
        sequence = {}
        while i + 2 < len(self.domain):
            if self.domain[i:i+2] in sequence.keys():
                sequence[self.domain[i:i+2]] += 1
            else:
                sequence.update({self.domain[i:i+2]:1})
            i += 1
        self.vector[7] = i/len(sequence)
        for i in sequence.values():
            self.vector[8] += (i-self.vector[7])**2
        self.vector[8] = self.vector[8]/(len(sequence) - 1)
        self.vector[9] = self.vector[8]**0.5
        self.featureTable[self.features[7]] = self.vector[7]
        self.featureTable[self.features[8]] = self.vector[8]
        self.featureTable[self.features[9]] = self.vector[9]
        
        
        
        return {'mean':self.vector[7],'variance':self.vector[8],'standard variance':self.vector[9]}
    def masked2gram(self)->dict:
    
        values = {'cc':0,'vc':0,'cv':0}
        i = 0
        while i<len(self.domain):
            
            if self.masked[i:i+2] in values.keys():
                
                values[self.masked[i:i+2]] += 1
            i += 1
        self.vector[10] = values['cc']
        self.vector[11] = values['vc']
        self.vector[12] = values['cv']
        
        self.featureTable[self.features[10]] = self.vector[10]
        self.featureTable[self.features[11]] = self.vector[11]
        self.featureTable[self.features[12]] = self.vector[12]
        
        return values
    
    def masked3gram(self):
        values = {'ccc':0,'cvc':0,'vcc':0,'vcv':0}
        i = 0
        while i<len(self.domain):
            if self.masked[i:i+3] in values.keys():
                values[self.masked[i:i+3]] += 1
            i += 1
    
        self.vector[13] = values['ccc']
        self.vector[14] = values['cvc']
        self.vector[15] = values['vcc']
        self.vector[16] = values['vcv']

        
        self.featureTable[self.features[13]] = self.vector[13]
        self.featureTable[self.features[14]] = self.vector[14]
        self.featureTable[self.features[15]] = self.vector[15]
        self.featureTable[self.features[16]] = self.vector[16]
        
        return values

    def most_least_ratio(self)->dict:
        
        max_char = max(self.__freaquency, key=self.__freaquency.get)
        min_char = min(self.__freaquency,key=self.__freaquency.get)
        
        self.vector[17] = self.__freaquency[max_char]/len(self.domain)
        self.vector[18] = self.__freaquency[min_char]/len(self.domain)
        
        self.featureTable[self.features[17]] = self.vector[17]
        self.featureTable[self.features[18]] = self.vector[18]
        
        return {'max_freaq' : self.vector[17],'min_freaq' : self.vector[18]}
    
    def shanon_entropy(self)->float:
        
        total_chars = len(self.domain)
        probabilities = [count / total_chars for count in self.__freaquency.values()]
        entropy = -sum(p * log2(p) for p in probabilities if p > 0)
        self.vector[19] = entropy
        self.featureTable[self.features[19]] = self.vector[19]
        return entropy
    
    def most_freaquent_twoGram_freaquency(self)->dict:
    
        values = dict.fromkeys("in,er,an,re,es,ar,on,or,te,al,st,ne,en".split(','),0)
        i = 0 
        while i +2 < len(self.domain):
            if self.domain[i:i+2] in values.keys():
                values[self.domain[i:i+2]] += 1
            i += 1
        for i,j in zip(range(20,32),values.values()):
            self.vector[i] = j
            self.featureTable[self.features[i]] = j
        
        return values
    
    def most_freaquent_threeGram_freaquency(self)->dict:
        values = dict.fromkeys('ing,ion,ine,ter,lin,ent,the,ers,and,est,tio,tra,tor,art'.split(','),0)
        i = 0 
        while i + 3 < len(self.domain):
            if self.domain[i:i+3] in values.keys():
                values[self.domain[i:i+3]] += 1
            i += 1
        for i,j in zip(range(33,46),values.values()):
            self.vector[i] = j
            self.featureTable[self.features[i]] = j    