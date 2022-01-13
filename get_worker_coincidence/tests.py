from main import *

class Test_clean_data:

    def test_one(self):
        input = ["ASTRID=MO10:00-12:00,TH12:00-14:00",
                "ANDRES=SU20:00-21:00"]
        result = {'ASTRID': {'MO': '10:00-12:00', 'TH': '12:00-14:00'},
                'ANDRES': {'SU': '20:00-21:00'}}
        assert clean_data(input)==result

class Test_to_compare_workers:
    def test_one(self):
        input = {'ASTRID': {'MO': '10:00-12:00', 'TH': '12:00-14:00'},
                 'ANDRES': {'SU': '20:00-21:00'}}
        assert to_compare_workers(input)=={'ASTRID-ANDRES':0}

    def test_two(self):
        input = {'ASTRID': {'MO': '10:00-12:00', 'TH': '12:00-14:00'},
                 'ANDRES': {'MO': '10:00-19:00'}}
        assert to_compare_workers(input)=={'ASTRID-ANDRES':1}