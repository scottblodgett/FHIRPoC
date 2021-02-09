
import ast

def search(list, key):
    for item in list:
        if key in item:
            return item


def my_func(event):

    result = ast.literal_eval(str(event)) 

    # Get my API key
    apiKey = "t2o7CGAVBwf8kxxiBEJwLu3hveH9XbWD"

    listOfItems = []
    for item in result:
        pair = {item['name'] : (item['value'])}
        listOfItems.append(pair)
    
    patientGUID = search(listOfItems, 'txtBasic')
    baseUrl = 'https://syntheticmass.mitre.org/v1/fhir/Patient/'
    fullUrl = baseUrl + str(patientGUID['txtBasic']) + '?' + apiKey
    print(fullUrl)
    # sending get request and saving the response as response object 
    #r = rr.get(url = "https://syntheticmass.mitre.org/v1/fhir/Patient/c8a021dc-b91e-4fe7-b6ec-81c948013fc4?apikey=t2o7CGAVBwf8kxxiBEJwLu3hveH9XbWD") 


    listOfItems = []
    for item in result:
        pair = {item['name'] : (item['value'])}
        listOfItems.append(pair)
    

if __name__ == '__main__':

    event = '[{"name":"rdOption","value":"1"},{"name":"txtBasic","value":"c8a021dc-b91e-4fe7-b6ec-81c948013fc4"},{"name":"txtAll","value":"c8a021dc-b91e-4fe7-b6ec-81c948013fc4"},{"name":"txtNum","value":"3"},{"name":"txtCond","value":"444814009,75498004,36971009,40055000"},{"name":"txtProc","value":"112790001"},{"name":"element_7_1","value":""},{"name":"element_7_2","value":""},{"name":"element_7_3","value":""},{"name":"element_77_1","value":""},{"name":"element_77_2","value":""},{"name":"element_77_3","value":""},{"name":"form_id","value":"999"}]'
    my_func(event)