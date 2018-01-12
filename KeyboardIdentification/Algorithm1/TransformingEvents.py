import sys
import uuid


KEY_PRESS_EVENT_NAME = "KEY_PRESS"
KEY_RELEASE_EVENT_NAME = "KEY_RELEASE"
MOUSE_PRESS_EVENT_NAME = "MOUSE_PRESS"
MOUSE_RELEASE_EVENT_NAME = "MOUSE_RELEASE"
MOUSE_POSITION_EVENT_NAME = "MOUSE_POSITION"
TASK_STARTED_EVENT_NAME = "TASK_STARTED"
TASK_FINISHED_EVENT_NAME = "TASK_FINISHED"


class keypress:
	def __init__(self, symbol, milliseconds_time):
		self.symbol = symbol.lower()
		self.milliseconds_time = milliseconds_time

	def is_letter(self):
		return len(self.symbol) <= 1 and ord('a') <= ord(self.symbol[0]) <= ord('z')

	def letter_number(self):
		if not self.is_letter:
			raise Exception("attempt to get letter_number of non letter event")
		return ord(self.symbol[0]) - ord('a')


def parse_keypress(event_line):
	parts = event_line.split()
	# print(event_line)
	return keypress(parts[1][0], int(parts[2]))


def read_events(input_file):
	file = open(input_file, 'r')
	while True:
		event = file.readline()
		if not event:
			break
		yield event
	file.close()


def is_keypress_event(event_line):
	if len(event_line) <= 0:
		return False
	parts = event_line.split()
	if len(parts) <= 0:
		return False
	return parts[0] == KEY_PRESS_EVENT_NAME


def filter_events(all_events):
	return (event for event in all_events if is_keypress_event(event))


def generate_output_filename(input_file):
	return "handled users/" + str(uuid.uuid4()) + " " + input_file


def symbol_from_number(symbol_number):
	return chr(symbol_number + ord('a'))


def write_to_file(output_filename, matrix):
	output = open(output_filename, 'w')

	for i in range(26):
		for j in range(26):
			numbers_string = ' '.join((str(x) for x in matrix[i][j]))
			output.write(symbol_from_number(i) + symbol_from_number(j) + " : " + numbers_string + "\n")

	output.close()


def reasonable_delay(milliseconds):
	# delay should not be more than 500 milliseconds
	return milliseconds < 500


def create_matrix():
	matrix = []

	for i in range(26):
		matrix.append([])
		for j in range(26):
			matrix[i].append([])

	return matrix


def construct_matrix(keypress_events):

	frequecies = create_matrix()

	previous_defined = False
	previous_event = None

	for event in keypress_events:
		parsed_event = parse_keypress(event)
		if not parsed_event.is_letter():
			continue

		if not previous_defined:
			previous_defined = True
			previous_event = parsed_event
			continue

		current_event = parse_keypress(event)
		current_delay = current_event.milliseconds_time - previous_event.milliseconds_time
		if reasonable_delay(current_delay):
			frequecies[previous_event.letter_number()][current_event.letter_number()].append(current_delay)

		previous_event = current_event

	return frequecies


def main():
	recorded_events_file_name = sys.argv[1]
	events = read_events(recorded_events_file_name)
	keypress_events = filter_events(events)
	matrix = construct_matrix(keypress_events)
	write_to_file(generate_output_filename(recorded_events_file_name), matrix)


if __name__ == "__main__":
	main()