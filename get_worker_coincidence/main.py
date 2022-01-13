import re  # regular expresions
from datetime import date, datetime  # to work with dates
import argparse  # to define arguments in the input
import os  # to work with paths and folders
from itertools import combinations  # combinations methods


def save_results(data: dict, name_file: str):
    """save a dictionarie in a txt file


    Args:
        data (dict): the dictionary input. 
        e.g. {'BRAYAN':0,'LUIS':3,'MARIA':5}

        name_file (str): the name of the output txt file
    Return:
        the function doesn't have a return variable
        the function create or rewrite a file if have the same name 
    """
    if len(name_file.split('.')) > 1:
        name_file = name_file.split('.')[0]

    if not os.path.isdir('results'):
        os.mkdir('results')

    with open(f'./results/{name_file}_results.txt', 'w', encoding='utf-8') as f:
        for pair, value in data.items():
            f.write(f'{pair}: {value}')
            f.write('\n')


def read(name: str) -> list:
    """ read a txt file and put the lines in a list

    Args:
        name(str): the input txt file

    Return:
        raw_data(list): all the lines of the input txt file

    Exceptions:
        the execption raise when the file doesn't exist in the input_file folder
        the expection raise when the file is not a txt file

    """

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
    """ transform the data input in a dictionary of dictionaries structure

    structure of the dictionary return

    {'NAME': {'DAY':HOUR,DAY:HOUR},NAME:{DAY:HOUR,DAY:HOUR}}


    e.g
    input: []
    ouput: 


    Returns: 
        workers (dict):  A dictionary of dictionaries

    """

    workers = {}

    for worker in raw_data:
        name, week_list = worker.split('=')
        hour = re.split(r',*[A-Z]+', week_list)[1:]
        day = re.split(r'[0-9]+[,:-]*', week_list)
        day = list(filter(lambda x: x != "", day))
        workers[name] = dict(zip(day, hour))
    return workers


def get_hour(hour: str):
    """transform a string to datatype

    Args:
        hour (str): variable with the hour information

    Returns: 
       (hour_in, hour_out): a tuple with the times
    """
    hour_in, hour_out = hour.split("-")
    try:
        hour_in = datetime.strptime(hour_in.lstrip().rstrip(), '%H:%M').time()
        hour_out = datetime.strptime(
            hour_out.lstrip().rstrip(), '%H:%M').time()
    except ValueError as ve:
        print(f'ERROR: {ve} please check, discard date')
    return hour_in, hour_out


def overlap_time(date_in_1: date, date_out_1: date, date_in_2: date, date_out_2: date) -> bool:
    """Compare two ranges of times and return a boolean

    Args:
        date_in_1 (date): initial hour of the first worker
        date_out_1 (date): end hour of the first worker
        date_in_2 (date): initial hour of the second worker
        date_out_2 (date): end hour of the second worker

    Returns:
        (bool): True -> if have coicidence in the conditionals
                False -> if not have coincidence in the conditionals
    """
    if(date_in_2 <= date_in_1 <= date_out_2):
        return True
    elif(date_in_2 <= date_out_1 <= date_out_2):
        return True
    elif(date_in_1 <= date_in_2 <= date_out_1):
        return True
    elif(date_in_1 <= date_out_2 <= date_out_1):
        return True

    return False


def compare_hours(hour1: str, hour2: str) -> bool:
    """get two ranges of hours and return a boolean variable

    Args:
        hour1 (str): [description]
        hour2 (str): [description]

    Returns:
        overlap(bool): get the value acording the overlap_time funciton result

    Exception:
        if the inputs doesn't have the correct structure return false 
    """
    date_in_1, date_out_1 = get_hour(hour1)
    date_in_2, date_out_2 = get_hour(hour2)
    try:
        overlap: bool = overlap_time(
            date_in_1, date_out_1, date_in_2, date_out_2)
    except TypeError:
        return False
    return overlap


def get_coincidence(week1: dict, week2: dict) -> int:
    """ count the numbers of coindicence between two workers schedule 
        represented in a dictionarie datastructure



    Args:
        week1(dict):  a worker schedule dictionarie 
        week2(dict): a worker schedule dictionarie
    Returns:
        cont(int): the count of the coincidences
    """

    cont: int = 0
    days_worker = list(week1.keys())

    for day in days_worker:
        if day in list(week2.keys()):
            cont += compare_hours(week1[day], week2[day])
    return cont


def to_compare_workers(workers: dict) -> dict:
    """compare all workers and return the results in a dictionary

    Args:
        workers(dict): a dictionary of dictionaries structure that represent
                       the worker name and schedule of the week

    Returns:
        combination(dict): pair of workers and the coincidence that they have
    """

    workers_name: list = list(workers.keys())
    combination: dict = {}

    for worker_a, worker_b in combinations(workers_name, 2):
        item = str(worker_a+"-"+worker_b)
        number: int = get_coincidence(workers[worker_a], workers[worker_b])
        combination[item] = number

    return combination


def run(read_name):
    """principal function with the main procces

    Args:
        read_name (str): the name of the raw data file 
    Return:
        The function doesn't return any variables
    """
    # read the txt file and put in a list
    raw_data: list = read(read_name)  
    # put the initial list in a more flexible data structure
    workers: dict = clean_data(raw_data)
    # get the pair worker and hours coincidence
    compare: dict = to_compare_workers(workers)
    print("\nOUTPUT:\n")
    for item, value in compare.items():
        print(f'{item}: {value}')

    save_results(compare, read_name)
    print('\nThe output was saved, please check the "results" folder')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file_name", help="name of the file with the information")

    arg = parser.parse_args()
    run(arg.input_file_name)
