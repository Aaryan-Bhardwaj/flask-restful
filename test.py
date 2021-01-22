import requests

BASE= "http://127.0.0.1:5000/"

# data = [{"name": "how to doodoo like pro", "views": 100485630, "likes": 10},
# 		{"name": "how to sell anything", "views": 2222222223, "likes": 1048764},
# 		{"name": "become a millionaire in 2 days!!!!!!!!", "views": 10, "likes": 1}]

# for i in range (len(data)):
# 	response = requests.put(BASE + "video/" + str(i), data[i])
# 	print(response.json())
# input()
response = requests.patch(BASE + "video/2", {"views":9999})
print(response.json())