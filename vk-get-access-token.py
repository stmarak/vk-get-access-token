import requests
from getpass import getpass
import argparse


def get_access_token(login, password, client_id, client_secret):
	try:
		response = requests.get(
			'https://oauth.vk.com/token?grant_type=password&' + \
			'client_id=' + str(client_id) + \
			'&client_secret=' + client_secret + \
			'&username=' + login + \
			'&password=' + password
		).json()

	except requests.exceptions.ConnectionError:
		print('[!] Error. Could not get access token. Please check your internet connection')
		exit(0)

	try:
		return response['access_token']

	except:
		print('[-] Error. Could not get access token. Please check if login and password valid')
		exit(0)


def parse_args():
	parser = argparse.ArgumentParser(description='VK Get Access Token v 1.1')

	parser.add_argument('-l', '--login', help='Your VK login', type=str)
	parser.add_argument('-p', '--password', help='Your VK password', type=str)
	parser.add_argument('-q', '--quiet', help='Do not print access token in the terminal', action='store_true')
	parser.add_argument('-f', '--file-path', help='Save access token into file [file path]', type=str)

	vk_app_settings = parser.add_argument_group('VK app settings (optional)')
	vk_app_settings.add_argument('-cl', '--client-id', help='VK app client id', type=int, default=3697615) # 3697615 is client id for official VK app for windows
	vk_app_settings.add_argument('-cs', '--client-secret', help='VK app secret', type=str, default='AlVXZFMUqyrnABp8ncuU') # AlVXZFMUqyrnABp8ncuU is secret for official VK app for windows


	return parser.parse_args()


def main():
	args = parse_args()

	if args.login and args.password:
		access_token = get_access_token(args.login, args.password, args.client_id, args.client_secret)

	elif args.login and not args.password:
		access_token = get_access_token(args.login, getpass('Password: '), args.client_id, args.client_secret)

	elif not args.login and args.password:
		access_token = get_access_token(input('Login: '), args.password, args.client_id, args.client_secret)

	elif not args.login and not args.password:
		access_token = get_access_token(input('Login: '), getpass('Password: '), args.client_id, args.client_secret)


	if not args.quiet:
		print('[*] Your VK access token: "' + access_token + '"')

	if args.file_path:
		try:
			with open(args.file_path, 'w') as file:
				file.write(access_token)
				file.close()

			print('[+] Wrote access token into ' + args.file_path)

		except PermissionError:
			print('[-] Could not write access token to ' + args.file_path + '. Access denied')
			exit(0)


if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		print('\n')
		exit(0)
