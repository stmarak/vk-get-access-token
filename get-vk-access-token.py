import requests
import getpass
from lib import pictorem as pct


def main():
	client_id = '3697615'	# Official VK Windows app client id

	login = input(pct.white.bold('Login: '))
	password = pwd = getpass.getpass(pct.white.bold('Password: '))

	response = requests.get(
		'https://oauth.vk.com/token?grant_type=password&client_id='+client_id+'&client_secret=AlVXZFMUqyrnABp8ncuU&username=' + login + '&password=' + password
	).json()

	try:
		print()
		print(pct.white.bold('Got access token: "') + pct.light_blue.underlined(response['access_token']) + pct.white.bold('".'))

	except:
		print()
		print(pct.red.bold('Ooops... Something went wrong. Check login & password validation.'))


if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		print('\n')
		exit(0)