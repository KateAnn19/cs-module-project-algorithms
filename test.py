import csv



##########################################
class BankRecords():
    def __init__(self, office_location):
        self.office_location = office_location
    def __str__(self):
        return f"Located in ({self.office_location}"

recordcount = []

def recordsreader(records=[]):
  with open('input_data.csv', 'r') as f:
      reader = csv.reader(f)
      next(reader)
      for line in reader:
          if(line[5]) == "Northern California" or (line[5]) == "Southern California":
            recordcount.append(City(line[0], float(line[3]), float(line[4])))    
  return recordcount

print()   

recordsreader(input_data)


##########################################


##########################################
# in class guided problems
##########################################

# UPER 
# Understand the problem 
# inputs:
    # a number
    # a positive integer
    # verify how large?
    # what about zero? return none 
    # can we get bad data? no 
#output: Boolean (true or false depending on if it divides itsself)



def divides_self(num):
    pass

