import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    print(f'succes! {response}')
    print('Content{response.text}')
except Exception as e:
    print(f'there is an error', e)
print('Program ended')