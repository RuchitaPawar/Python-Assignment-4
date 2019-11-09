from functools import reduce

def AcceptData():
 size = int(input("Enter number of elements:"))
 arr = list()
 for i in range(0,size,1):
   print("enter number",i+1)
   value = int(input())
   arr.append(value)

 return arr

def ChkPrime(no):
  brr = list()
  for x in range(2,no,1):
    if ((no % x) == 0):
      return False
    else:
        brr.append(no)
  return brr

def Modify(no):
   return no*2

def Maximum(no1,no2):
  if (no1 > no2):
      max = no1
  else:
      max = no2
  return max;

def main():
 RawData = AcceptData();
 #print(RawData)

 FilteredData = list(filter(ChkPrime,RawData))
 print("Filtered data is",FilteredData)

 ModifiedData = list(map(Modify,FilteredData))
 print("Modified data is:",ModifiedData)

 result = reduce(Maximum,ModifiedData)
 print("Final result is:",result)

if __name__ == "__main__":
  main();

