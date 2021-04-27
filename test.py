from stardict import DictCsv
import sys

if __name__ == '__main__':
  word =  sys.argv[1] if len(sys.argv) > 1 else 'prodigy'
  dict = DictCsv('/Users/alhuang/work/deepext/ECDICT/ecdict.csv')
  print('querying ' + word)
  print(dict.query(word))