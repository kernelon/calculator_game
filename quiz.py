import datetime
import random

from question import Add
from question import Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # generate 10 random questions using number from 1 to 10
        # add all questions to self.questions

    def take_quiz(self):
        # log the start time
        # ask all questions
        # check if all questions were answered correctly
        # log the end time
        # show a summary

    def ask(self, questions):
        # log the start time
        # capture the answers
        # check the answer
        # log the end time
        # if the answer is correct, return true
        # if the answer is false, return false
        # send the elapse time

    def summary(self):
        # print how many questions were correct and how many was wrong eg: 5/10
        # print the total time taken to complete the quiz eg: 30 seconds
