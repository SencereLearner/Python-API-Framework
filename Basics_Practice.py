import time
from tkinter.font import names
from turtledemo.penrose import start

#==========#==========#==========#==========#==========LIST
# Mutable
# Can have mixed data types
l_empty = list() #l_empty = []
l_filled = [1, 'text', True]
print(l_filled)
print(len(l_filled))

for i in l_filled:
    print(l_empty.append(i), l_empty)
print("Final: ", l_empty)

l_empty.pop(1)
l_empty.append(16)
print("Final deleted: ", l_empty)

print(f"Expected: 16, Was: {l_empty[-1]}") #print last element from the list
assert 16 == l_empty[-1]

l1 = list(set([1, 2, 3, 1, 6, 1, 2])) #another way to keep unique values in a list (double cast)
print("Unique values list: ", l1)

l_srez = [2, 4, 6, 8, 1, 3, 5, 7, 9] #taking out part of list with starting and ending index
print("Carving out a part of list: ", l_srez[0:6:2]) #return elements from index 0 to 6 taking every 2nd ele

l_srez2 = [10, 20, 30, 40, 50, 60]
print("Printing entire l_srez2 list", l_srez2[:]) #print out every element in a list
print("Printing reversed l_srez2 WAY 1", l_srez2[::-1]) #print out every element in a list IN REVERSED ORDER
print("Printing reversed l_srez2 WAY 2", sorted(l_srez2, reverse=True)) #another way to print IN REVERSED ORDER
# without reverse=True, it will just sort the list in ascending order

#==========#==========#==========#==========#==========TUPLE
# Immutable (once created, can not be changed)
tup = tuple() #tup = ()
print("Empty Tuple", tup)
tup = (10, 20, 30, 10, 45, 10)
print("Added some values to Tuple: ", tup)
print("Value occurrence count: ", tup.count(10)) #counts how many times 10 is found in the tuple
print("The value is at index: ", tup.index(45)) #gives index of an element
#==========#==========#==========#==========#==========SET
# Can have mixed data types
# Only keeps unique values
# Doesn't guarantee order
# Elements can't be found by index
# Mutable
empty_set = set() #that's the only way how to create an empty set, not empty_set = {}, it will be a dict otherwise
my_set = {1, 5, 'test', True, 1.16, 5}
print("Initial Set values: ", my_set)
my_set.add('added text')
print("Updated set: ", my_set)
#==========#==========#==========#==========#==========DICT
# Elements can be found by key
# Mutable
# Can have mixed data types
my_dict = {'key1' : 'value1', 'key2' : 2, 'key3' : [1, 2, 3]}
print("Dict values: ", my_dict.get('key3'))
my_dict['key4'] = True
print("Added values: ", my_dict)
#==========#==========#==========#==========#==========UNPACKING COLLECTIONS
# To take out each element from collection and save it to a unique variable
my_set2 = {2, 4, 6}
s1, s2, s3 = my_set2
print("Printing unpacked Set values: ", s1, s2, s3)
# example of using this in automation. Since .find_element() expects 2 params, By and Value
# we pass tuple with 2 params and unpack it. Then it turns into a webelement:
# vrs = ("xpath", "//*[text()='Product']")
# driver.find_element(*vrs)
#==========#==========#==========#==========#==========ONE LINE IF-ELSE
#print("Let's drink cocoa!" if answer == 'yes' else "I'd recommend a coffee!")
######################## ARGS, KWARGS ########################
def kwargs_price_list(**kwargs):
    for item, price in kwargs.items():
        print(f"Item is: {item} and price is: {price}")
kwargs_price_list(bread = 1, cheese = 2, milk = 3)

def args_price_list(*args):
    print("Devotee? - ", args[0], "Chants what? - ", args[1], "How many times? ", args[2])
args_price_list("Yes", "Hare Krishna", 1728)

def log_steps(*steps):
    for step in steps:
        print(f"Step: {step}")
log_steps("Open browser", "Login", "Click dashboard", "Verify title")
######################## ARGS, KWARGS ########################

######################## FUNCTION GENERATORS ########################
def even_numbers_up_to(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
evens = even_numbers_up_to(6)
for num in evens:
    print(num)
# It does NOT run immediately
# Pulls one number at a time from the generator (yield i one by one).
# It's very memory efficient because it does not calculate all numbers at once
######################## FUNCTION GENERATORS ########################

######################## LIST COMPREHENSION ########################
# It’s a shorter and often more Pythonic alternative to using loops.
# basic syntax: new_list = [expression for item in iterable if condition]
#example:
raw = ['  Pass ', 'fail ', ' Pass', 'FAIL']
normalized = [x.strip().lower() for x in raw]
print("Formatted using list comprehension: ", normalized)  # ['pass', 'fail', 'pass', 'fail']

raw2 = [1, 2, 3, 4, 5, 6, 7, 8]
list_compr = [x for x in raw2 if x % 2 == 0]
print('Even numbers using LIST COMPREHENSION:', list_compr)
######################## LIST COMPREHENSION ################################################

######################## MAP ################################################
# similar to FILTER but is used to transform each item
mixed_numbers = [3, 6, 9, 12, 15]
def multiply_numbers(x):
    return x * 2
mult_list1 = map(multiply_numbers, mixed_numbers)
print('Multiply each number using MAP:', list(mult_list1))

mult_list2 = map(lambda x: x * 2, mixed_numbers)
print('Multiply each number using MAP WITH LAMBDA:', list(mult_list2))

# can add if else conditions
new_lists_map = map(lambda x: x * 2 if x != 15 else x * 3, mixed_numbers)
print(list(new_lists_map))
# THE SAME IS DONE WITH LAMBDA FUNCTION

######################## MAP ################################################

######################## FILTER ################################################
# similar to MAP but is used to filter sth out based on condition and not modify each item like map does
mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
def even_numbers(x):
    return x % 2 == 0
new_list_filter1 = filter(even_numbers, mixed_numbers)
print('Even numbers using FILTER:', list(new_list_filter1))

# THE SAME IS DONE WITH LAMBDA FUNCTION
new_list_filter2 = filter(lambda x: x % 2 == 0, mixed_numbers)
print('Even numbers using FILTER WITH LAMBDA:', list(new_list_filter2))
######################## FILTER ################################################

######################## DECORATORS ################################################
# Basic Example (THIS IS WHEN A FUNCTION PRINTS SOMETHING BUT DOESN'T RETURN)
def argsKwargsDecorator(func):
    def wrapper(*args, **kwargs):
        print(f'Function started --->>> {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Function finished --->>>  {func.__name__}')
        return result
    return wrapper
@argsKwargsDecorator
def funcWithDecorator(name, age):
    print(f'Name is: {name} \nAge is: {age}')
funcWithDecorator('Krishna', 16) # can use positional arguments (args support it)
funcWithDecorator(name = 'Krishna', age= 16) # or can use named arguments (kwargs support it)

# QA Automation Example (often used for logging, how long function runs, retrying failed tests, etc)
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end - start:.1f} seconds")
    return wrapper
@timer
def login():
    time.sleep(1.1)  # Simulate a test
    print("Login test executed")
login()

# Basic Example (THIS IS WHEN A FUNCTION RETURNS SOMETHING BUT DOESN'T PRINT)
def argsKwargsDecorator2(func):
    def wrapper(*args, **kwargs):
        print(f'Function started --->>> {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Function finished --->>>  {func.__name__}')
        return result
    return wrapper
@argsKwargsDecorator2
def funcWithDecorator(name, age):
    return f'Name is: {name} \nAge is: {age}'
print(funcWithDecorator('Krishna', 16)) # can use positional arguments (args support it)
print(funcWithDecorator(name = 'Krishna', age= 16)) # or can use named arguments (kwargs support it)
######################## DECORATORS ################################################

######################## CLASSES ################################################
# pass means the method can be implemented later, basically a placeholder to avoid empty method error
# it's an abstract method. method implementation is not mandatory in this case
def abstract_method(self):
    pass

# to make it required need to import ABC and pass it to parent method as parameter + decorator for abstract method
from abc import ABC, abstractmethod
class Parent(ABC):
    age = 16
    @abstractmethod
    def abstract_method(self):
        pass
# to implement it, need to inherit Parent class and implement abstract since it's required now
class Child(Parent):
    def abstract_method(self):
        print('Abstract method from Parent class is being implemented')

child = Child()
child.abstract_method()
######################## CLASSES ################################################

######################## WORKING WITH JSON FILE AND CONSTRUCTOR ################################################
# keyword "with" controls automatic file opening and closing and keyword "as" is just an alias
import json

def file_reading(file_name):
    with open(file_name, 'r') as file_data:
        return json.load(file_data)
data = file_reading('//MyTestHotmail/data_file.json')
print(data['title'])

# Example of how it can be initialized through Constructor
class ReadFileClass:

    def __init__(self, file_path):
        self.file_path = file_path # file_path is required to create an object of this class, then it's used in read_file method
        self.data = self.read_file() # calling read_file method through constructor
        self.title = self.data['title'] # just a shortcut for knowing what keys there are in the file
        self.year = self.data.get('year') # another way to get the key

    def read_file(self):
        with open(self.file_path, 'r') as my_file:
            return json.load(my_file) # returns file content (used for JSON ONLY)

instance_object = ReadFileClass('//MyTestHotmail/data_file.json') # because it's in the constructor, it requires to pass file_path
print('File 1 title: ', instance_object.title)
print('File 1 year: ', instance_object.year)

class ReadFileClassJson2(ReadFileClass):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.habitat = self.data['habitat']
        self.age = self.data['age']

read_file_class_two = ReadFileClassJson2('//MyTestHotmail/data_file2.json')
print('File 2 habitat: ', read_file_class_two.habitat)
print('File 2 age: ', read_file_class_two.age)
######################## WORKING WITH JSON FILE AND CONSTRUCTOR ################################################

######################## MORE WORK WITH FILES ################################################
import os
# Cross-platform safe file path
base_path = os.path.dirname(__file__)  # Always gives absolute path for any OS
os_file_path = os.path.join(base_path, 'text.txt')

# Generator function: reads line by line, cleans content
def read_file_lines(file_path):
    with open(file_path, 'r') as my_file:
        for line in my_file:
            yield line.replace(',', ' ').replace('.', ' ').strip()

# Option 1: Print cleaned lines
for line in read_file_lines(os_file_path):
    print(line, end='')  # Avoids adding extra newline

# Option 2: Clean and overwrite file
def clean_file(file_path):
    with open(file_path, 'r') as my_file:
        cleaned_lines = [line.replace(',', ' ').replace('.', ' ').strip() for line in my_file]

    with open(file_path, 'w') as file:
        for line in cleaned_lines:
            file.write(line + '\n')

# Run the cleaning (comment/uncomment depending on what you want to do)
clean_file(os_file_path)

######################## MORE WORK WITH FILES ################################################

######################## ACCESS MODIFIERS ################################################
# _ protected (can be accessed within parent or inherited class)
# __ private (can only be accessed within parent class)
# no underscores (public)
# if a variable is private (__) but I still need to access it outside the class I can use @property decorator

class Temperature:
    __celsius = 25  # private class-level variable
    @property # have to use @Property to read a private class variable even inside the class!
    def print_celsius(self):
        return self.__celsius
t = Temperature()
print("Celsius:", t.print_celsius)

# and to modify private variable outside the class I need to use Setter
class Movie:

    def __init__(self, title):
        self.__title = title # private variable

    @property
    def title(self): # property used for reading the variable outside the class
        return self.__title

    # setter property used for changing the variable outside the class (MUST HAVE @property along with it)
    # setter MUST equal @property method name (title in this case)
    # setter doesn't return anything. setter is called like a property not like a method
    @title.setter
    def title(self, new_title):
        self.__title = new_title

movie = Movie('Krishna The God')
movie.title = movie.title = 'Jaya Radhe!'
print(movie.title)

######################## ACCESS MODIFIERS ################################################

######################## WALRUS := OPERATOR  ################################################
# := used for assignment expressions. It assigns a value to a variable as part of an expression, not as a separate statement.
my_num = 108
while (user_num := int(input('Enter a number: '))) != my_num:
    if user_num > my_num:
        print('The number should be larger')
    else:
        print('The number should be smaller')
print('You guessed correctly!')
######################## WALRUS := OPERATOR := ################################################

######################## HOW TO HIDE SENSITIVE DATA ################################################
# WAY 1 (ADD FILE WITH VARIABLES TO GITIGNORE):
# Have a file with data you want to use and hide (example: passwd = '123'). Add it to git ignore
# import this file to a class or another file, where I want to use this data: https://prnt.sc/qfxogYHV_o2K
# and just call the variable, which has the value I need
from MyTestHotmail import data # that's how I imported the file with the variables I want to use
def krishna(name, age):
    return f'Name is: {name}, age is: {age}'
print(krishna(data.name, data.age))

#WAY 2 (ADD FILE WITH VARIABLES TO GITIGNORE):
from dotenv import load_dotenv # need to import this
import os # need to import this

# create a .env file (can be called literally .env). Add variables there like: name = Krishna, age = 16
# Load the .env file (specify filename if it's not .env)
# if file is called .env then just use load_dotenv()
load_dotenv(dotenv_path="secret.env")

def radha(name, age):
    return f"Radha's Name is: {name}, Radha's Age is: {age}"
# call the variables by os.getenv("variable name, same as specified in the .env file")
print(radha(os.getenv("name"), os.getenv("age")))
######################## HOW TO HIDE SENSITIVE DATA ################################################

######################## FAKER MODULE ################################################
from faker import Faker
fake = Faker()
for _ in range(3):
    print(fake.name_male()) # can generate a variety of things (name, address, phone, zip etc)
######################## FAKER MODULE ################################################

######################## API REQUESTS ################################################
# need to install api module: pip install requests. Then import it
import requests

def get_one_post_by_index():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(response.json())
get_one_post_by_index()
#------------------------------------------------------------------------------------
def post_a_post():
    request_body = {
        "title": "Krishna",
        "body": "Spiritual",
        "userId": 1}

    request_headers = {
        "Content-type": "application/json"}

    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=request_body, headers=request_headers)
    print(response.status_code)
    print(response.json())
post_a_post()
#------------------------------------------------------------------------------------

def put_a_post():
    request_body = {
        "title": "Radha", # changed this to be updated vs what I had in post command
        "body": "Spiritual!",
        "userId": 1}

    request_headers = {
        "Content-type": "application/json"}
    # just changed command to PUT and add id so it modifies a particular post
    response = requests.put('https://jsonplaceholder.typicode.com/posts/16', json=request_body, headers=request_headers)
    print(response.status_code)
    print(response.json())
put_a_post()
#------------------------------------------------------------------------------------
# ASSERT test 1
def get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert len(response.json()) == 100, 'Json Response Length Count Mismatch ! ! !'
get_all_posts()
#ASSERT test 2
def get_one_post_by_id():
    post_id = 21
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.json()['id'] == post_id, 'Post ID doest match ! ! !'
get_one_post_by_id()
#ASSERT test 3
def get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200, 'Status code doesnt match ! ! !'
get_all_posts()
######################## API REQUESTS ################################################

######################## UNITTEST ################################################
# BUILT IN module, used for running tests (less popular). It is a framework.
import unittest
import requests
import sys
# file, class and method name should start with the word 'test' in it
# need to import unittest module and class must inherit from unittest.TestCase
# can run from terminal with this command: python -m unittest -vs
# unittest has its own built in assert which MUST BE used. call it from self.
class TestPostApi(unittest.TestCase):
    def setUp(self): # reserved method name. if found it will run before all tests
        request_body = {
            "title": "Krishna",
            "body": "Spiritual",
            "userId": 1}
        request_headers = {
            "Content-type": "application/json"}
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=request_body, headers=request_headers)
        print(f'\nsetUp method is executed. Post Id is created: {response.json()['id']}')
        self.post_id = response.json()['id']

    @unittest.skip('Skipped as the output is too big !') # skips this particular test
    def test_get_all_posts(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/')
        print(response.json())

    @unittest.skipIf(sys.platform == 'windows', 'Skipped with if condition') # skips this particular test
    def test_skipIf(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/')
        print(response.json())

    def test_get_one_post_by_index(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(response.json())

    def tearDown(self): # reserved method name. if found it will run after all tests
        print(f'Deleting Post Id: {self.post_id}')
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
######################## UNITTEST ################################################

######################## PYTEST ################################################
# NON BUILT IN module, used for running tests (most popular). It is a framework.
# install pytest module: pip install pytest and then import the module
# file, class and method name should start with the word 'test' in it
# doesn't have built in assert, so can use regular python asserts
# can run tests with: python -m pytest -vs or type pytest -vs
import pytest

@pytest.mark.skip('Skipping !') # fixture to skip test
def test_pytest_one():
    assert 2 == 2, 'Mismatch !'
    print('Assert ONE succeeded !')

# fixture to use this method in any other place by calling the methods name
# works as pre-condition. Function which has this fixture called will run this fixture first
# for post-conditions can use function generator using yield keyword.
# similar to return but can actually do more after yield is hit. yield returns results then continues to do what's after yield
@pytest.fixture()
def test_pytest_two():
    print('Returning int 2')
    yield 2
    print('Returned 2 and now printing this final line as a post-condition')

def test_pytest_three(test_pytest_two): # here I used test_pytest_two by decorating it
    assert 2 == test_pytest_two, 'Mismatch !'
    print('Assert TWO succeeded !')

# there is also decoration: @pytest.mark.regression (just example, can be any name)
# which groups tests by certain criteria
# then I just run those groups of tests from terminal: pytest -vs -m regression
# just need to have a file .ini, which will list all those types of tests for python to recognise
# here is content of .ini file as example:
# [pytest]
# markers =
#     smoke: all smoke tests
#     regression

@pytest.mark.smoke
def test_smoke_one():
    print('Smoke test one')

@pytest.mark.smoke
def test_smoke_two():
    print('Smoke test two')

@pytest.mark.regression
def test_regression_one():
    print('Regression test one')

# textures can be in the same file where methods are
# but it's good practice to keep fixtures in a separate file conftest.py
# in the same folder where the tests are which use the fixtures so tests can access the fixtures
# each test folder can have its own conftest.py file so different data can be used for different tests

# @pytest.mark.parametrize is a decorator that allows you to:
# Pass different sets of data to the same test function.
# Avoid writing duplicate test code for similar scenarios.
@pytest.mark.parametrize("number", [1, 2, 3])
def test_is_positive(number):
    assert number > 0
######################## PYTEST ################################################

######################## TEST PARALLELIZATION ################################################
# pip install pytest-xdist
# run from terminal:
# pytest -v -s -n auto or pytest -vsn auto (it will use every core in the machine)
# pytest -vsn 5 (it will use the indicated amount of cores in the machine, in this case 5). Safer option to avoid overload
# it will collect all the pytest tests (all that start with word test) and run them in parallel based on computing power
######################## TEST PARALLELIZATION ################################################

######################## ALLURE REPORT ################################################
# install allure: https://allurereport.org/docs/install-for-macos/
# install java: https://learn.microsoft.com/en-us/java/openjdk/download (need version 11 or 17 for allure to work)
# pip install allure-pytest
# import allure
# run from terminal:
# 1) pytest -v --alluredir=allure-results (this will create a folder with some test data). Only run once
# 2) allure serve allure-results (need to supply folder path) - this option is for quick temporary view or the report
# 3) allure generate allure-results -o allure-report (1st results folder path, 2nd results folder path)
# this option #3 is for permanently saving the results locally
# for segregating features by type, use decorator @allure.feature('NameHere') or @allure.story('NameHere')
import allure

@allure.feature('SmokeTest')
@allure.story('SMT')
@pytest.mark.smoke
def test_smoke_one():
    print('Smoke test one')

@allure.feature('SmokeTest')
@allure.story('SMT')
@pytest.mark.smoke
def test_smoke_two():
    print('Smoke test two')

@allure.feature('RegressionTest')
@allure.story('REGRT')
@pytest.mark.regression
def test_regression_one():
    print('Regression test one')
######################## ALLURE REPORT ################################################















