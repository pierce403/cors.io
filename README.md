# cors.io
a simple cors proxy

Now fully flaskified, and ready for deployment on heroku.

## Table of Contents

[TOC]

## Supported HTTP Methods

### GET Request
```javascript
$.getJSON('http://cors.io/?' +
    'https://httpbin.org/get?cors=a_problem',
    function (res) {
        console.log(res);
    });
```
```json
{
    "args": {
        "cors": "a_problem"
    },
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Host": "httpbin.org",
        "User-Agent": ""
    },
    "origin": "",
    "url": "https://httpbin.org/get?cors=a_problem"
}
```

### POST Request

#### application/json

```javascript
$.ajax({
    method: "POST",
    url: 'https://cors.io/?' + 
        'https://httpbin.org/post',
    headers: {
        'Content-Type': 'application/json'
    },
    data: JSON.stringify({
    	"cors": "a_problem"
    }),
    success: (res) => console.log(res)
});
```
```json
{
    "args": {}, 
    "data": "{\"cors\":\"a_problem\"}", 
    "files": {}, 
    "form": {}, 
    "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Content-Length": "20", 
        "Host": "httpbin.org", 
        "User-Agent": ""
    }, 
    "json": {
        "cors": "a_problem"
    }, 
    "origin": "", 
    "url": "https://httpbin.org/post"
}
```

#### application/x-www-form-urlencoded

```javascript
$.ajax({
    method: "POST",
    url: 'https://cors.io/?' + 
        'https://httpbin.org/post',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    data: "cors=a_problem",
    success: (res) => console.log(res)
});
```
```json
{
    "args": {}, 
    "data": "", 
    "files": {}, 
    "form": {
        "cors": "a_problem"
    }, 
    "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Content-Length": "14", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Host": "httpbin.org", 
        "User-Agent": ""
    }, 
    "json": null, 
    "origin": "", 
    "url": "https://httpbin.org/post"
}
```

#### multipart/form-data

```javascript
var formData = new FormData();
formData.append("cors", "a_problem");

files = $("input[type='file']")[0].files;
for (var i = 0; i < files.length; i++)
    formData.append("file " + (i + 1), files[i]);

$.ajax({
    method: "POST",
    url: 'https://cors.io/?' + 
        'https://httpbin.org/post',
    data: formData,
    processData: false,
    contentType: false,
    success: (res) => console.log(res)
});
```
```json
{
    "args": {}, 
    "data": "", 
    "files": {
        "file 1": "file 1 content\n",
        "file 2": "file 2 content\n"
    }, 
    "form": {
        "cors": "a_problem"
    }, 
    "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Content-Length": "310", 
        "Content-Type": "multipart/form-data; boundary=1c7006cba3bb1825a4294d7fd319942c", 
        "Host": "httpbin.org", 
        "User-Agent": ""
    }, 
    "json": null, 
    "origin": "", 
    "url": "https://httpbin.org/post"
}
```

### OPTIONS Request

There is no purpose in requesting this method manually. However, some javascript libraries such as [axios](https://github.com/axios/axios) submit an `OPTIONS` request before the `POST` request in the case of `Content-Type: application/json`.

In order to work with that, an `OPTIONS` request is sent from the website, to itself. This will return the landing page, along with the required to headers in order for CORS to not block the preflight-response.

## Deploying on Heroku

1. First of all begin by forking this reposity. This can be done by clicking the fork button next to the top of repository.
![Fork](https://i.imgur.com/TeNuhY0.png)

2. Then create your heroku app under the name you like.
> ![Create App](https://i.imgur.com/lIiqB4F.png)
> _becomes_
> ![Create App Form](https://i.imgur.com/TbtN8PC.png)

3. You will be taken to the new app's page, where you can specify the deployment method you wish to use. In our case, GitHub.
![Connect to GitHub](https://i.imgur.com/zzheYYQ.png)

4. After connecting to GitHub, search for the name of the fork and _Connect_ it. 
> ![Searching Fork](https://i.imgur.com/V1dOFvC.png)
> _becomes_
> ![Connected Fork](https://i.imgur.com/vqVDbwB.png)

5. After it has been connected, deploy the branch on Heroku.
> ![Pre Deployment](https://i.imgur.com/ujUMtQq.png)
> _becomes_
> ![Post Deployment](https://i.imgur.com/Vih0Qtk.png)

6. View your app.
![App](https://i.imgur.com/7xkUAXV.png)
