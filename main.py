# CCTV 및 경찰관서의 좌표 정보 받아오기 위함
# 주소 관련 변수들 클래스 다이어그램에는 float형이라고 나와 있는데 (lat,lng) 형태의 튜플이 적합해보임
import os
import backend.mapapp.models as models

# 유저의 정보를 다루는 클래스
class User(object):
    def __init__(self, currentLocation, destination):
        self.currentLocation = currentLocation
        self.destination = destination
    def search(self):pass
    def specifyDestination(self):pass

# 지도의 정보와 조작 정보를 관리하기 위한 클래스
# Database 클래스에서 받은 정보와 user의 현재 위치를 저장한다.
# 지도 관련 기능의 On/Off 여부를 결정한다.
class map(object):
    def __init__(self, maptype, cctvLocation, POLocation, currentLocation):
        self.maptype = maptype
        self.cctvLocation = cctvLocation
        self.POLocation = POLocation
        self.currentLocation = currentLocation
    def dragable(self):pass
    def scaleControlable(self):pass
    def showMaptype(self):pass

# CCTV 및 경찰 관서의 위치 정보 표시 여부를 결정하는 클래스
class showLocation(object):
    def __init__(self, cctvLocation, POLocation):
        self.cctvLocation = cctvLocation
        self.POLocation = POLocation
    def showCctvLocation(self):pass

# 길안내에 필요한 정보 처리를 하는 클래스
class Navigate(object):
    def __init__ (self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    def isCurrentLocation(self):return result
    def setStartPoint(currentLocation):return currentlocation
    def setEndpoint(destination):return destination
    def changeSearchtoLatLng(search):return search
    def navigate(startPoint, endPoint):pass

# 가장 가까운 경찰관서까지의 길안내에 필요한 정보 처리를 하는 클래스
class NavigatetoNearestPO(object):
    def __init__ (self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    def setStartPoint(currentLocation):
        return currentLocation
    def setEndpoint(destination):
        return destination
    def navigate(startPoint, endPoint):pass
