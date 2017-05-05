ibrary(gdata)                   # load gdata package 
> help(read.xls)                   # documentation 
> mydata = read.xls("v4Michelle_10032026_writetocsv.csv")  # read from first sheet
getwd()
setwd(dir)
data = read.csv("v4Michelle_10032026_writetocsv.csv", header = TRUE)

##crapo typed wrong thing was meant to be "data = " not "dat = "

#why so many errors in red keep typing data 

# get means for variables in data frame mydata
# excluding missing values 
sapply(mydata, mean, na.rm=TRUE) #didnt work 
> summary(dat)
library(Hmisc) #had to install this package 
describe(mydata) 
# n, nmiss, unique, mean, 5,10,25,50,75,90,95th percentiles 
# 5 lowest and 5 highest scores

library(pastecs) # package didnt work - directory problem 
stat.desc(mydata) 
# nbr.val, nbr.null, nbr.na, min max, range, sum, 
# median, mean, SE.mean, CI.mean, var, std.dev, coef.var

library(psych)
describe(mydata)
# item name ,item number, nvalid, mean, sd, 
# median, mad, min, max, skew, kurtosis, se

