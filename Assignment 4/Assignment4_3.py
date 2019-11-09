from functools import reduce

def AcceptData():
 size = int(input("Enter number of elements:"))
 arr = list()

 for i in range(0,size,1):
   print("enter number",i+1)
   value = int(input())
   arr.append(value)

 return arr

def main():
 RawData = AcceptData();

 FilteredData = list(filter(lambda no : no >= 70 and no <=90,RawData))
 # print("Filtered data is",FilteredData)

 ModifiedData = list(map(lambda no : no+10,FilteredData))
 #print("Modified data is:",ModifiedData)

 result = reduce(lambda no1 , no2 : no1*no2,ModifiedData)
 print("Final result is:",result)
if __name__ == "__main__":
  main();
