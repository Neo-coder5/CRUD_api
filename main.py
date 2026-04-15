import requests

url = "https://weatherapi-com.p.rapidapi.com/alerts.json"

querystring = {"q":"london"}

headers = {
	"x-rapidapi-key": "42f5fde9f4msh0f42e7db665200bp1521b1jsnc519c50876fb",
	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())