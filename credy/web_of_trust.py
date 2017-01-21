import requests
def verify( url ):
    WOT_API_KEY = "8750e1e44154b413a13b1d029b4d43ee022644e6"
    mywot_api_endpoint = "http://api.mywot.com/0.4/public_link_json2"
    querystring = {"hosts":"/"+ url + "/","callback":"process","key" : WOT_API_KEY}
    payload = ""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "93ffde57-c70f-a775-d5ce-03f8e152e9da"
        }
    response = requests.request("GET", mywot_api_endpoint, data=payload, headers=headers, params=querystring)
    data = response.text.replace("process","")
    try:
        web_of_trust_score = int(data.split("[")[1].split(",")[0])
        return web_of_trust_score
    except:
        return 50
if __name__ == "__main__":
    print verify(raw_input("Enter the URL: "))
