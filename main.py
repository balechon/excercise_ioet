import re  # regular expresions
from datetime import date, datetime  # to work with dates
import argparse  # to define arguments in the input
import os  # to work with paths and folders


def save_results(data: dict, name_file: str):
    run_date = datetime.today().strftime('%d-%m-%Y')
    if len(name_file.split('.')) > 1:
        name_file = name_file.split('.')[0]

    if not os.path.isdir('results'):
        os.mkdir('results')

    with open(f'./results/{name_file}_results_{run_date}.txt', 'w', encoding='utf-8') as f:
        for pair, value in data.items():
            f.write(f'{pair}: {value}')
            f.write('\n')


def read(name: str) -> list:
    raw_data = []

    if len(name.split('.')) > 1:
        name = name.split('.')[0]

    try:
        if not os.path.isdir('input_files'):
            raise ValueError('"input_file" folder does not exist')
    except ValueError as ve:
        print(f"""ERROR: {ve}
-PLease, create the folder "input_file" an put your file in there        
        """)
        exit()

    try:
        with open(f'./input_files/{name}.txt', 'r', encoding='utf-8') as f:
            for line in f:
                raw_data.append(line.rstrip())
    except:
        print("""ERROR READING THE FILE, posible cause of the error: 
- The extension is not ".txt"
- The name is incorrect
- The file is not in the folder "input_files" """)
        exit()
    return raw_data


def clean_data(raw_data: list) -> dict:
    workers = {}
    for worker in raw_data:
        name, days = worker.split('=')
        days = days.split(',')
        workers[name] = days
    return workers


def split_date(date_hour: str) -> tuple[str, str]:
    date_hour = re.split('(\d.*)', date_hour)
    date_hour.pop()
    return date_hour[0], date_hour[1]


def get_hour(hour: str) -> tuple[date, date]:
    hour_in, hour_out = hour.split("-")
    try:
        hour_in = datetime.strptime(hour_in.lstrip().rstrip(), '%H:%M').time()
        hour_out = datetime.strptime(
            hour_out.lstrip().rstrip(), '%H:%M').time()
    except ValueError as ve:
        print(f'ERROR: {ve} please check, discard date')
    return hour_in, hour_out


def overlap_time(date_in_1: date, date_out_1: date, date_in_2: date, date_out_2: date) -> bool:
    cont: int = 0
    if(date_in_2 <= date_in_1 <= date_out_2):
        cont = cont+1
    elif(date_in_2 <= date_out_1 <= date_out_2):
        cont = cont+1
    elif(date_in_1 <= date_in_2 <= date_out_1):
        cont = cont+1
    elif(date_in_1 <= date_out_2 <= date_out_1):
        cont = cont+1

    if cont > 0:
        return True
    else:
        return False


def compare_hours(hour1: str, hour2: str) -> bool:
    date_in_1, date_out_1 = get_hour(hour1)
    date_in_2, date_out_2 = get_hour(hour2)
    try:
        overlap: bool = overlap_time(
            date_in_1, date_out_1, date_in_2, date_out_2)
    except TypeError:
        return False
    return overlap


def get_coincidence(week1: list, week2: list) -> int:
    cont: int = 0
    for register1 in week1:
        for register2 in week2:
            day1, hour1 = split_date(register1)
            day2, hour2 = split_date(register2)

            if day1 != day2:
                continue
            if compare_hours(hour1, hour2):
                print(f'- coincidence at {day1}: {hour1} - {hour2}')
                cont = cont+1
            else:
                # print('the two workers not coincidence')
                cont = cont+0
    return cont


def to_compare_workers(workers: dict) -> dict:
    workers_name: list = list(workers.keys())
    workers_week: list = list(workers.values())

    combination: dict = {}
    for i in range(0, len(workers_name)):
        for j in range(0, len(workers_name)):
            if i == j or i > j:
                continue
            item = workers_name[i]+'-'+workers_name[j]

            print('\n * '+item)
            number: int = get_coincidence(workers_week[i], workers_week[j])
            combination[item] = number
    return combination


def run(read_name):
    raw_data: list = read(read_name)
    workers: dict = clean_data(raw_data)
    compare: dict = to_compare_workers(workers)
    print("\nOUTPUT:\n")
    for item, value in compare.items():
        print(f'{item}: {value}')

    save_results(compare, read_name)
    print('\nThe output was save, please check the folder "results"')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file_name", help="name of the file with the information")

    arg = parser.parse_args()
    run(arg.input_file_name)
