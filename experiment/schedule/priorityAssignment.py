import SchedulabilityAnalysis as sa


class Sensor:
    def __init__(self,arrivalTime,transmissionTime,deadLine,weight,priority = 0):
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority

def printSensor(sensorGroup):
    for x in range(0,len(sensorGroup)):
        print "sensor[{}].priority = {}".format(x,sensorGroup[x].priority)
    
def search(sensorGroup,priority):
    for x in sensorGroup:
        if x.priority == priority:
            index = sensorGroup.index(x)
            return index
def finialTest(sensorGroup):
    
    count = 0
    for x in sensorGroup:
        if x.priority == 0:
            count = count +1
    if count >1:
        return False
    for x in range(0,len(sensorGroup)):
        if sa.isSchedule(sensorGroup,x):
            continue
        else:
            return False
        
    return True

def initialSensor(sensorGroup,assignedArray,unassignedArray):
    for x in range(0,len(sensorGroup)):
        if sensorGroup[x] in assignedArray:
            print "sensor[{}] in assignedArray".format(x)
            continue
        sensorGroup[x].priority = 0



def priorityAssignmentAlgo(sensorGroup,assignedArray,unassignedArray):



    #########
    
    initialSensor(sensorGroup,assignedArray,unassignedArray)
    
    ## note unassigned sensor index

    
    assignedPriority = [x.priority for x in assignedArray]
    if assignedPriority:
        currentPriority = max(assignedPriority)+len(unassignedArray)
    else:
        currentPriority = len(unassignedArray)
    finialPriority = []
    print "==="
    for x in range(0,10):
        if x in assignedPriority:
            print x
    print currentPriority

    
    
    ## lowest priority first be assigned
    count = 0
    
    while currentPriority >= 0 :
       
        print "currentPriority:{}".format(currentPriority)

        ## check currentPriority is assigned 
        if currentPriority in assignedPriority:
            currentPriority = currentPriority -1
            continue
        else:
                   
            for target in sensorGroup:
                print "sensorGroup"
                printSensor(sensorGroup)           
                print "target.priority={} weight={}".format(target.priority,target.weight)
                print "current priority={}".format(currentPriority)
                count = count +1
                if target.priority == 0:
                    target.priority = currentPriority
                else:
                    print ""
                    continue
                
                index = sensorGroup.index(target)

                ## check schedule.
                if sa.isSchedule(sensorGroup,index):
                    print "target index:{} can schedule at priority {}  and jump".format(index,currentPriority)
                    
                    break
                else:
                    print "target index:{} can't schedule at priority {}".format(index,currentPriority)
                    ## to avoid duplicate priority in sensor
                    target.priority = 0
                
            
            currentPriority = currentPriority - 1
    
    print "count = {}".format(count)
    printSensor(sensorGroup)
    return finialTest(sensorGroup)

def main():
    
    ### arrival time, transmission time, deadLine, weight, priority
    a = Sensor(0.1,1.08,3.0,7,0)
    b = Sensor(0.1,1.08,4.0,4,1)
    c = Sensor(0.1,0.52,4.5,5,2)
    d = Sensor(0.0,1.08,100,4,5)
    '''
    a = Sensor(0.0,5.0,40.0,0,1)
    b = Sensor(0.0,2.0,50.0,1,3)
    c = Sensor(0.0,1.0,9.0,2,1)
    d = Sensor(0.0,1.0,8.0,3,2)
    e = Sensor(0.0,2.0,7.0,4,4)
    f = Sensor(0.0,1.0,15.0,4,5)
    '''
    print "main"
    
    sensorGroup = [a,b,c,d]#,d,e,f]
    assignedArray = [d]
    unassignedArray = [a,b,c]

    #assignedArray = [c,d,f]
    #unassignedArray = [a,b,e]
    for x in assignedArray:
        if x.priority ==0:
            print ("please remove priority 0 in assigned Array")
            break
    else:        
        if priorityAssignmentAlgo(sensorGroup,assignedArray,unassignedArray):
            print "==== sensorGroup can be schedulable"
        else:
            print "====can't be schedulable"

    printSensor(sensorGroup)
if __name__ == "__main__":
    main()
