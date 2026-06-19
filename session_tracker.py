from datetime import timedelta, datetime

events = [{'event': 'U.S. Unemployment Rates', 'currency': 'USD', 'date': '2026-06-19', 'impact': 'High'},
		  {'event': 'U.K. Unemployment Rates', 'currency': 'GBP', 'date': '2026-06-26', 'impact': 'Medium'},
		  {'event': 'Eurozone Unemployment Rates', 'currency': 'EUR', 'date': '2026-06-25', 'impact': 'Low'},
		  {'event': 'Manufacturing PMI', 'currency': 'USD', 'date': '2026-06-18', 'impact': 'Low'},
		  {'event': 'Manufacturing PMI', 'currency': 'GBP', 'date': '2026-06-19', 'impact': 'Medium'},
		  {'event': 'Manufacturing PMI', 'currency': 'EUR', 'date': '2026-07-18', 'impact': 'High'},
		  {'event': 'Average Hourly Earnings', 'currency': 'USD', 'date': '2026-06-25', 'impact': 'Low'}]


def upcoming_events(events):
	date_format = '%Y-%m-%d'
	current_date = datetime.today()
	sorted_events = sorted(events, key=lambda e: e['date'])

	for event in sorted_events:
		parsed_dates = datetime.strptime(event['date'], date_format) 
		date_range = (parsed_dates.date() - current_date.date()).days

		if date_range <= 5:
			print(f'{event["event"]}: Coming this week on {event["date"]}')

sessions = {'London': '08:00',
		'New York': '13:00',
		'Tokyo': '00:00',
		'Sydney': '22:00'}
try:
	sess_input = int(input('What is your UTC offset code: '))
except (NameError, ValueError):
	print('Invalid input.')
	exit()

def upcoming_sessions(sessions, sess_input):

	time_reader = timedelta(hours=sess_input)
	time_format = '%H:%M'

	current_time = datetime.now().strftime(time_format)
	current_time_object = datetime.strptime(current_time, time_format)
	hours_convert = current_time_object.hour

	user_local_current_time = current_time_object + time_reader
	user_local_current_hour = user_local_current_time.hour

	hours_convert_list = []
	active_sessions = []

	for session, timer in sessions.items():
		converted = datetime.strptime(timer, time_format)

		local_event_times = converted + time_reader

		local_convert = local_event_times.hour

		hours_convert_list.append(local_convert)

		if user_local_current_hour == local_convert:
			active_sessions.append(sessions)

		print(f'{session} session is at: {local_event_times.strftime(time_format)}')

	if active_sessions:
		print(
			f'It is currently {current_time} and the following sessions are active: {', '.join(active_sessions)}')
	else:
		print(
			f'It is currently {current_time} and no major trading sessions are currently active.')

print('\nActive sessions:')
upcoming_sessions(sessions, sess_input)
print('\n-----------------------------')
print('\nComing Events:')
upcoming_events(events)
