# C218 KISHAN SINGH BOXPLOT
x <- c(22, 28, 23, 29, 30, 35, 37, 38, 38, 39)
boxplot(x, main = "Boxplot of Given Data", xlab = 'width x axis', ylab = 'data1')
# using hardcoding
summary(x)
med_main = median(x) # or quantile(x, 0.5)
q1 = quantile(x, 0.25)
q3 = quantile(x, 0.75)
q1
q3
# IQR1 = q3-q1
# IQR1
IQR(x)
ul = 35 + (1.5*6)
ll = 29 - (1.5*6)
x[which(x < ll | x > ul)]
typeof(x)
# boxplot(outliers, main = 'boxplot of outliers')




