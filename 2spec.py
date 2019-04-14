from pylab import plot,show,draw,figure,loglog,scatter,semilogy
import numpy as np
import matplotlib.pyplot as plt


# Load Noise Power Magnitude file.
filename_np = input("Enter the 2nd Spectrum (.2Spec) file you would like to process: ")
print("Your file is ",filename_np)
f_np = open(filename_np,'r')
np_content = f_np.readlines()
f_np.close()

# Turn that noise power file into an array for python to understand.
headerlen_np = 28  # there are additional lines compared to the default files
footerlen_np = 2 # 2 for test file, 2 for real file?
trim_content_np = np_content[headerlen_np:len(np_content)-footerlen_np]

np_data = []
for row in range(len(trim_content_np)):
	temp = trim_content_np[row].split("\t")
	temp[len(temp)-1]=temp[len(temp)-1].rstrip() # remove new line character (\n) from last element
	for item in range(len(temp)):
		temp[item] =float(temp[item])
	np_data.append(temp)

#print(np_data)

# create m, a list of lists sort of array. Each list of the array contains one bin of m, for easier plotting.
m = []
temp =[]
for bin in range(len(np_data[0])):
	for trace in range(len(np_data)):
		temp.append(np_data[trace][bin])
	m.append(temp[1:])
	temp = []
#print(m[1])
#print(m[1])

# This is organized with columns in the right direction for using. Remove the first data point of each.

plt.figure()
plt.loglog(m[0],m[1], color ='k', marker = 'o', markersize=3, fillstyle = 'none', linestyle = 'none', label = 'O1')
plt.loglog(m[2],m[3], color ='b', marker = 'o', markersize=3, fillstyle = 'none', linestyle = 'none', label = 'O2')
plt.loglog(m[4],m[5], color = 'darkgreen', marker = 'o', markersize=3, fillstyle = 'none', linestyle = 'none', label = 'O3')
plt.loglog(m[6],m[7], color = 'limegreen', marker = 'o', markersize=3, fillstyle = 'none', linestyle = 'none', label = 'O4')
plt.loglog(m[8],m[9], color = 'orange', marker = 'o', markersize=3, fillstyle = 'none', linestyle = 'none', label = 'O5')
plt.loglog(m[10],m[11], color = 'r', marker = 'o', markersize=3, fillstyle = 'none', linestyle = 'none', label = 'O6')
plt.loglog(m[12],m[13], color = 'maroon', marker = 'o', markersize=3, fillstyle = 'none', linestyle = 'none', label = 'O7')
plt.title('Second Spectra \n File: '+filename_np)
plt.xlabel('Frequency/Freq_center (unitless)')
plt.ylabel('Noise Power (Normalized to 1 for Gaussian)')

plt.legend()
plt.tight_layout()
plt.show()
