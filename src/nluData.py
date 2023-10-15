import json
import pandas as pd
from tqdm import tqdm,trange

class SlotData:
    def __init__(self, data, verbose=False):
        total_queries = 0
        self.intents = {}
        self.queries = []
        for domain_data in data['domains']:
            if verbose: print('-'*100)
            if verbose: print(domain_data['name'])
            for idx, intent_data in enumerate(domain_data['intents']):
                if verbose: print(f"({idx+1}) {intent_data['description']} {intent_data['name']}")
                self.intents.update({intent_data['name']:[x['name'] for x in intent_data['slots']]})
                if verbose: print(f"Slots: {[x['name'] for x in intent_data['slots']]}")
                if verbose: print(f"No. of Queries: {len(intent_data['queries'])}")
                total_queries += len(intent_data['queries'])
                for items in intent_data['queries']:
                    self.queries.append(self.covert_dict_to_query(items, intent_data['name']))
    
    def covert_dict_to_query(self, dictionary, intent_name):
        output = {}
        output['intent'] = intent_name
        output['English'] = dictionary['text']
        slot_list = dictionary['results_per_service']['Snips']['slots']
        output['English_Slots'] = {}
        output['returnable'] = []
        for item in slot_list:
            if item['expected_a_value'] == "TRUE":
                output['returnable'].append(item['name'])
            output['English_Slots'].update({item['name']:item['value']})
        return output
    
    def get_intents(self):
        return self.intents
    
    def get_intents_names(self):
        return self.intents.keys()
    
    def get_intent_slots(self, intent_name):
        assert intent_name in self.intents, f"{intent_name} is not a valid instance for this dataset"
        return self.intents[intent_name]
    
    def get_queries(self):
        return self.queries
    
    def get_query_count(self):
        return len(self.queries)
    
    def empty(self):
        return ""
    
    def auto_query_translate(self, translator=empty, name='FormalBangla'):
        for i in trange(len(self.queries)):
            sentence = self.queries[i]['English']
            self.queries[i][f'{name}'] = translator(sentence)
            self.queries[i][f'{name}_Slots'] = self.queries[i]['English_Slots']

    