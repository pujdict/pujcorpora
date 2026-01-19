"""
This is a simple loader to do verification on yaml files.
"""
import argparse
import yaml
import sys
from pathlib import Path


def load(yaml_file_path: Path):
  with open(yaml_file_path, 'r', encoding='utf-8') as f:
    return yaml.load(f, yaml.Loader)


def main(argv):
  parser = argparse.ArgumentParser(description='Phrase Loader')
  parser.add_argument('file', type=Path, help='YAML files')
  parser.add_argument('--mode', default='test', choices=['test'])
  args = parser.parse_args(argv[1:])
  if args.mode == 'test':
    yaml_phrases = load(args.file)
    for i, yaml_phrase in enumerate(yaml_phrases):
      k, v = next(iter(yaml_phrase.items()))
      v = v or {}
      try:
        teochew_list, puj_list, cmn_list, word_class_list, tag_list = k.split('|')
      except:
        print(f"Error processing item {i}: {k}")


if __name__ == '__main__':
  main(sys.argv)
