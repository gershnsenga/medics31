import requests

def get_widely_spread_diseases():
    url = "https://disease.sh/v3/covid-19/jhucsse"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        diseases = set()
        for case in data:
            if 'country' in case:
                diseases.add(case['province'] + ', ' + case['country'])
            elif 'countryregion' in case:
                diseases.add(case['provincestate'] + ', ' + case['countryregion'])
        return diseases
    else:
        print("Failed to fetch data:", response.status_code)
        return None

def main():
    print("Fetching widely spread diseases...")
    diseases = get_widely_spread_diseases()
    if diseases:
        print("Widely spread diseases:")
        for disease in diseases:
            print(disease)
    else:
        print("No data available.")

if __name__ == "__main__":
    main()

