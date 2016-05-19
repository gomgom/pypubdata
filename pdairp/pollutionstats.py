import json
import urllib.parse
import urllib.request


class PollutionStats(object):
    def __init__(self, imported_key):
        self._service_key = str(imported_key)
        self._mainurl = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnStatsSvc/'

    def station(self, station_name, searchCondition, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl + 'getMsrstnAcctoLastDcsnDnsty?', 'stationName=', urllib.parse.quote(station_name),
            "&searchCondition=", searchCondition, '&pageNo=', page_no, '&numOfRows=', num_of_rows,
            '&ServiceKey=', self._service_key, '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'so2Avg', 'coAvg', 'o3Avg', 'no2Avg',
                'pm10Avg'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def period(self, searchDataTime, statArticleCondition, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl + 'getDatePollutnStatInfo?', 'searchDataTime=', searchDataTime,
            "&statArticleCondition=", urllib.parse.quote(statArticleCondition), '&pageNo=', page_no,
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
                'sidoName', 'dataTime', 'so2Avg', 'coAvg', 'o3Avg',
                'no2Avg', 'pm10Avg', 'so2Max', 'coMax', 'o3Max',
                'no2Max', 'pm10Max', 'so2Min', 'coMin', 'o3Min',
                'no2Min', 'pm10Min'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata