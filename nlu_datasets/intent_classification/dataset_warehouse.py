from dataset import Dataset

import sys
import os

PATH = os.path.join(os.getcwd(), 'nlu_datasets/intent_classification/')


# ATIS dataset
atis = Dataset('atis')
atis._load_train(PATH + 'atis_train.json')
atis._load_test(PATH + 'atis_test.json')
atis._form_all()

# Snips dataset
snips = Dataset('snips')
snips._load_train(PATH + 'snips_train.json')
snips._load_test(PATH + 'snips_test.json')
snips._form_all()

# Banking77 dataset
banking77 = Dataset('banking77')
banking77._load_train(PATH + 'banking77_train.json')
banking77._load_test(PATH + 'banking77_test.json')
banking77._form_all()

# Clinc-150 dataset
clinc150 = Dataset('clinc-150')
clinc150._load_train(PATH + 'clinc150_train.json')
clinc150._load_test(PATH + 'clinc150_test.json')
clinc150._form_all()

# HWU-64 Dataset
hwu64 = Dataset('hwu-64')
hwu64._load_all(PATH + 'hwu64.json')

# AskUbuntu Dataset
ask_ubuntu = Dataset('ask_ubuntu')
ask_ubuntu._load_train(PATH + 'ask_ubuntu_train.json')
ask_ubuntu._load_test(PATH + 'ask_ubuntu_test.json')
ask_ubuntu._form_all()

# Chatbot Dataset
chatbot = Dataset('chatbot')
chatbot._load_train(PATH + 'chatbot_train.json')
chatbot._load_test(PATH + 'chatbot_test.json')
chatbot._form_all()

# WebApplications Dataset
web_applications = Dataset('web_applications')
web_applications._load_train(PATH + 'web_applications_train.json')
web_applications._load_test(PATH + 'web_applications_test.json')
web_applications._form_all()
