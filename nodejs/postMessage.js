
    // create http request client to consume the QPX API
    var request = require("request")

    var deviceId    = "3a00d920-d6e4-4b2a-9d7f-1253850fe152";
    var deviceToken = "c6eda4694dcc36a6e7ed3f2c34563d6"
    var messageTyp  = "ba2434ef5c2b4bc8de83";
    var sensorId    = "NodeJS";

    var value       = 99;
    var timeStamp   = 1413191650;

    // JSON to be passed to the QPX Express API
    var requestData = {
            "mode":"sync",
            "messageType":"ba2434ef5c2b4bc8de83",
            "messages":
            [
                {
                    "sensor":"NodeJS",
                    "value":99,
                    "timestamp":1413191650
                    
                }
            ]
        }
    
    // QPX REST API URL (I censored my api key)
    url = "https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/3a00d920-d6e4-4b2a-9d7f-1253850fe152";

    // fire request
    request({
        url: url,
        method: "POST",
        json: true,
        headers:{
            "Authorization" : "Bearer c6eda4694dcc36a6e7ed3f2c34563d6",
            "content-type"  : "application/json"
        },
        body:{
            requestData
        }
    }, function (error, response, body) {
        if (!error && response.statusCode === 200) {
            console.log(body)
        }
        else {

            console.log("error: " + error)
            console.log("response.statusCode: " + response.statusCode)
            console.log("response.statusText: " + response.statusText)
        }
    })