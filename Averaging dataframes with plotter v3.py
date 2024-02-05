




import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

#read in data with pandas
data1 = pd.read_csv(r"C:\Users\lab work\Downloads\Spectrums\Luminesence Spectras\Sample K\Sample K2__50x_10s_1%_ 500-650 luminesence spec spot 1.txt",sep='\s+',header=None)
df1 = pd.DataFrame(data1)

data2 = pd.read_csv(r"C:\Users\lab work\Downloads\Spectrums\Luminesence Spectras\Sample K\Sample K2__50x_10s_1%_ 500-650 luminesence spec spot 2.txt",sep='\s+',header=None)
df2 = pd.DataFrame(data2)

data3 = pd.read_csv(r"C:\Users\lab work\Downloads\Spectrums\Luminesence Spectras\Sample K\Sample K2__50x_10s_1%_ 500-650 luminesence spec spot 3.txt",sep='\s+',header=None)
df3 = pd.DataFrame(data3)

data4 = pd.read_csv(r"C:\Users\lab work\Downloads\Spectrums\Luminesence Spectras\Sample K\Sample K2__50x_10s_1%_ 500-650 luminesence spec spot 4.txt",sep='\s+',header=None)
df4 = pd.DataFrame(data4)

data5 = pd.read_csv(r"C:\Users\lab work\Downloads\Spectrums\Luminesence Spectras\Sample K\Sample K2__50x_10s_1%_ 500-650 luminesence spec spot 5.txt",sep='\s+',header=None)
df5 = pd.DataFrame(data5)



dfavg1 = np.mean( np.array([df1, df2, df3, df4, df5 ]), axis=0 )

dfavg1 = pd.DataFrame(dfavg1)
#create output csv to see if mean is correct
#dfavg1.to_csv('output test.csv')




#create x and y variables
x = dfavg1[0]
y = dfavg1[1]

#savgotzky golay filter
yhat = savgol_filter(y, 100, 3) #window size 150, polynomial order 3
                                
#polynomial fit
offset =  5000

y_coeff = np.polyfit(x,y,3)


yhat3 = offset + y - np.polyval(y_coeff, x)

#if you want to output data to csv to read
#yhat3.to_csv( "outputtest", sep='\t')

#figure adjustment

fig = plt.figure()

ax1 = fig.add_subplot(111)
#nessecary to get array to work



#set the array to correct subplot

ax1.set_title("Sample K2 Photoluminesence")  #Important graph quantities  
ax1.set_xlabel('Wavelength (nm)')
ax1.set_ylabel('Intensity (A.U.)')


plt.text(520, 20000, y_coeff, fontsize = 8, 
         bbox = dict(facecolor = 'red', alpha = 0.5))

print(y_coeff)



plt.grid()

#these put the plot out for people to see
plt.plot(x, y,'red', label = 'K2')
#plt.plot(x,yhat,linewidth = '3', color='blue')
plt.plot(x,yhat3,linewidth = '2', color='green' ,label = "K2 w/0 background")


#adding legend
leg = ax1.legend()
plt.show()
