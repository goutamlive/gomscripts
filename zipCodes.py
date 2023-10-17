def get_secret_message():
    urlFirstPart = "https://api.zipcodestack.com/v1/search?codes="
    urlSecondPart = "&country=us&apikey=*******"
    with open('filePath/zipCodes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            zipCode =row['zipCode']
            response = requests.get(urlFirstPart+zipCode+urlSecondPart)
            responseJson = json.loads(response.text)
            pinInfo = responseJson['results'][zipCode][0]
            print(f"{zipCode},{pinInfo['city']},{pinInfo['state']}")

if __name__ == "__main__":
    get_secret_message()
