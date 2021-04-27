import pandas as pd
import os

cols = [ 'Preferred Indicator',
         'Face Amount Band','Gender',
         'Smoker Status',
 'Insurance Plan',
 'Issue Age',
 'Duration',
 'Attained Age',
 'Number of Deaths',
 'Policies Exposed',]
dat = pd.read_csv('../../scratchpad/2009-15 Data 20180601.txt',nrows=2e6,sep='\t',usecols=cols)
os.remove('../../scratchpad/2009-15 Data 20180601.txt')
dat = dat[(dat['Issue Age']>=40)&(dat['Issue Age'] <60)&(dat['Duration']<10)]
dat = dat[dat['Policies Exposed']>0]
dat.to_csv('../../scratchpad/ILECsample_40-60.txt')