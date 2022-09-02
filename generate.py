import argparse
import train

parser = argparse.ArgumentParser()
parser.add_argument("--model", type = str, required=True, help="путь к файлу, из которого загружается модель")
parser.add_argument("--prefix", type = str, required=False, help="начало предложения")
parser.add_argument("--length", type = int, required=True, help="лина генерируемой последовательности")

args = parser.parse_args()

model = train.model()

model.generate(args.model, args.length, args.prefix)