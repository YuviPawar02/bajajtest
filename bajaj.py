//1st
import requests
import json

url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

payload = json.dumps({
  "name": "Yuvraj Pawar",
  "regNo": "0827CD221078",
  "email": "yuvrajpawar220131@acropolis.in"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


//2nd
import http.client
import json

conn = http.client.HTTPSConnection("bfhldevapigw.healthrx.co.in")
payload = json.dumps({
  "query": "SELECT e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME, COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT FROM EMPLOYEE e1 JOIN DEPARTMENT d ON e1.DEPARTMENT_ID = d.DEPARTMENT_ID LEFT JOIN EMPLOYEE e2 ON e1.DEPARTMENT = e2.DEPARTMENT AND e2.DOB > e1.DOB GROUP BY e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME ORDER BY e1.EMP_ID DESC"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/hiring/generateWebhook/PYTHON", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
