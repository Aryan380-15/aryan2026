import matplotlib.pyplot as plt
x = [2000,2001,2002,2003,2004,2005,2006,2007]
y = [55,65,90,47,50,99,38,77]
plt.xlabel('year')
plt.ylabel('number')
plt.title("number info")
plt.plot(x,y,'r+--')
plt.show()