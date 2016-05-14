import json
import urllib.parse
import urllib.request


class PollutionInfo(object):
    def __init__(self, imported_key):
        self._service_key = str(imported_key)
        self._mainurl = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/'

    def stationdata(self, station_name, data_term, page_no='1', num_of_rows='10', ver='1.2'):
        verurl = '&ver=' + ver
        # It's for changing version, It seems like version system doesn't work on OpenAPI, so I comment them.
        # verurl = '&ver='
        # if ver == '0': verurl = ''
        # else: ver_url += ver

        urllist = [
            self._mainurl + 'getMsrstnAcctoRltmMesureDnsty?', 'stationName=', urllib.parse.quote(station_name),
            "&dataTerm=", data_term, '&pageNo=', page_no, '&numOfRows=', num_of_rows,
            '&ServiceKey=', self._service_key, '&_returnType=json', verurl
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'mangName', 'khaiGrade', 'khaiValue', 'coGrade',
                'coValue', 'no2Grade', 'no2Value', 'o3Grade', 'o3Value',
                'pm10Grade', 'pm10Value', 'pm10Value24', 'pm25Grade', 'pm25Value',
                'pm25Value24', 'so2Grade', 'so2Value'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def strangelist(self, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl, 'getUnityAirEnvrnIdexSnstiveAboveMsrstnList?', 'pageNo=', page_no,
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
                'addr', 'stationName'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def sidodata(self, sido_name, page_no='1', num_of_rows='10', ver='1.2'):
        verurl = '&ver=' + ver
        # It's for changing version, It seems like version system doesn't work on OpenAPI, so I comment them.
        # verurl = '&ver='
        # if ver == '0': verurl = ''
        # else: verurl += ver

        urllist = [
            self._mainurl, 'getCtprvnRltmMesureDnsty?', 'sidoName=', urllib.parse.quote(sido_name),
            '&pageNo=', page_no, '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key,
            '&_returnType=json', verurl
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'mangName', 'stationName', 'khaiGrade', 'khaiValue',
                'coGrade', 'coValue', 'no2Grade', 'no2Value', 'o3Grade',
                'o3Value', 'pm10Grade', 'pm10Value', 'pm10Value24', 'pm25Grade',
                'pm25Value', 'pm25Value24', 'so2Grade', 'so2Value'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def forecastlist(self, inform_code, search_date='0', page_no='1', num_of_rows='10'):
        dateurl = '&searchDate='
        if search_date == '0':
            dateurl = ''
        else:
            dateurl += search_date

        urllist = [
            self._mainurl, 'getMinuDustFrcstDspth?', 'InformCode=', inform_code, dateurl,
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
                'dataTime', 'imageUrl1', 'imageUrl2', 'imageUrl3', 'imageUrl4',
                'imageUrl5', 'imageUrl6', 'informCause', 'informData', 'informGrade',
                'informOverall', 'actionKnack'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata