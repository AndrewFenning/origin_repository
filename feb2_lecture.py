import matplotlib.pyplot as plt
import numpy
# classes = ['science', 'math', 'social studies', 'english']
# grades = [95,94,82,88]
# plt.bar(x=classes, height = grades)
# plt.show()

x=[1,2,3,4,5]
y=[2,5,3,5,7]
z=[1,1,2,2,3]
# plt.plot(x, y, 'o-',color = 'orange', label = 'line1')
# plt.plot(x, z, 'o-',color = 'green', label = 'line1')
# plt.show()

# plt.scatter(x, y)
# plt.show()
# x2=[[1,1,1,1],[2,2,2,2],[3,3,3,3]]
# y2=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# heights = [[1,2,3,4],[2,7,4,5],[3,4,5,6]]
# plt.contourf(x2,y2,heights)
# plt.show()

l = [1.5,5,3.4,6,3,4.7]
median = numpy.median(l)
stand_dev = numpy.std(l)
print(median, stand_dev)