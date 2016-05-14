import json
import urllib.parse
import urllib.request


class StationInfo(object):
    def __init__(self, imported_key):
        self._service_key = str(imported_key)
        self._mainurl = 'http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/'

    def nearby(self, tm_x, tm_y, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl, 'getNearbyMsrstnList?', 'tmX=', str(tm_x), '&tmY=', str(tm_y),
            '&pageNo=', page_no, '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key,
            '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'stationName', 'addr', 'tm'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][i][j]

        return returndata

    def detail(self, addr, station_name, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl, 'getMsrstnList?', 'addr=', urllib.parse.quote(addr),
            '&stationName=', urllib.parse.quote(station_name), '&pageNo=', page_no,
            '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key, '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'addr', 'dmX', 'dmY', 'item', 'mangName',
                'map', 'oper', 'photo', 'stationName', 'vrml',
                'year'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][i][j]

        return returndata

    def tmcode(self, umd_name, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl, 'getTMStdrCrdnt?', 'umdName=', urllib.parse.quote(umd_name),
            '&pageNo=', page_no, '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key,
            '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'sidoName', 'sggName', 'umdName', 'tmX', 'tmY'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][i][j]

        return returndata