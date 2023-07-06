# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import argparse
import utils
argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
        help="Path of the corpus to evaluate on", default=None)
args = argp.parse_args()
if __name__ == "__main__":
    with open(args.eval_corpus_path,encoding='utf8') as fin:
        lines = [x.strip().split('\t') for x in fin]
        true_places = [x[1] for x in lines]
        total = len(true_places)
        predictions = ['London' for _ in range(total)]
        total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
    if total > 0:
        print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))