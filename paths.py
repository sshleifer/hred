from pathlib import Path
HOME = Path('/Users/shleifer/curai_temp')
if not HOME.exists():
    HOME = Path('/home/shleifer')
assert HOME.exists()
DATA_DIR = HOME/'MovieTriples/'

TEST_TRIPLES_PATH = DATA_DIR / 'Test.triples.pkl'
#OLD_VAL_TRIPLES_PATH = DATA_DIR / 'Validation.triples.pkl'
#OLD_TRAIN_TRIPLES_PATH = DATA_DIR + '/Training.triples.pkl'
training_dict_path = DATA_DIR + 'Training.dict.pkl'
eval_source_path = '/data2/chatbot_eval_issues/results/AMT_NCM_Test_NCM_Joao/neural_conv_model_eval_source.txt'
dict_file = '/home/harshals/hed-dlg/Data/MovieTriples/Training.dict.pkl'

TRAIN_TRIPLES_PATH = DATA_DIR/'triples_train.pkl'
VAL_TRIPLES_PATH = DATA_DIR/'triples_val.pkl'

#TRAIN_TRIPLES_PATH = NEW_TRAIN_TRIPLES
#NE
