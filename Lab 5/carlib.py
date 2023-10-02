class Car:
    
    def __init__(self, make, model, num_of_door):
        
        self._make = make
        self._model = model
        self._num_of_door = num_of_door
        self._is_car_running = False
        self._current_trip = list([])
    
    
    
    def getMake(self):
        
        return self._make
    
    def setMake(self, make):
        
        self._make = make
    
    def getModel(self):
        
        return self._model
    
    def setModel(self, model):
        
        self._model = model        
    
    def getNumOfDoor(self):
        
        return self._num_of_door
    
    def setNumOfDoor(self, num_of_door):
        
        self._num_of_door = num_of_door
    
    def getIsCarRunning(self):
        
        return self._is_car_running
    
    def setIsCarRunning(self, is_car_running):
        
        self._is_car_running = is_car_running
    
    def getCurrentTrip(self):
        
        return self._current_trip
    
    def setCurrentTrip(self, current_trip):
        
        self._current_trip = current_trip
    
    
    
    def startEngine(self):
        
        self.setCurrentTrip(list([]))
        self.setIsCarRunning(True)
    
    
    
    def stopEngine(self):
        
        self.setIsCarRunning(False)
    
    
    
    def addMotion(self, distance_in_m, duration_in_sec):
        
        if self.getIsCarRunning():
            
            motion = {'distance_in_m': distance_in_m, 'duration_in_sec': duration_in_sec}
            self.getCurrentTrip().append(motion)
            
            distanceInKm = distance_in_m / 1000
            travelTimeInHour = duration_in_sec / 3600            
            
            return distanceInKm / travelTimeInHour
    
    
    
    def computeCurrentTripTravelTimeInMinute(self):
        
        travelTime = 0
        
        for motion in self.getCurrentTrip():
            
            travelTime += motion['duration_in_sec'] / 60
        
        return travelTime
    
    
    
    def computeCurrentTripTotalDistanceInKm(self):
        
        totalDistance = 0
        
        for motion in self.getCurrentTrip():
            
            totalDistance += motion['distance_in_m'] / 1000
        
        return totalDistance
    
    
    
    def computeCurrentTripAverageSpeedInKmPerHour(self):
        
        travelTimeInHour = self.computeCurrentTripTravelTimeInMinute() / 60
        totalDistanceInKm = self.computeCurrentTripTotalDistanceInKm()
        
        return totalDistanceInKm / travelTimeInHour
    
    
    def toString(self):
        
        return self._make + ', ' + self._model + ', ' + str(self._num_of_door) + ', ' + str(self._is_car_running) + ', ' + str(self._current_trip)
