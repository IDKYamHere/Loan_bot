from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu.model import Metadata, Interpreter
from rasa.nlu import config
from rasa.nlu.components import ComponentBuilder
import rasa

builder = ComponentBuilder(use_cache = True)

def train_nlu(domain, config, output, training_files):
        model_path = rasa.train(domain,config, [training_files], output)
        print(model_path)

def run_nlu():
	interpreter = Interpreter.load('C:/Users/divya/OneDrive/Desktop/Bot_Convo/NucBot/models', builder)
	print(interpreter.parse("can you suggest me a loan"))

if __name__ == '__main__':
	train_nlu('domain.yml', 'config.yml', "models", ".\data")
	#run_nlu()