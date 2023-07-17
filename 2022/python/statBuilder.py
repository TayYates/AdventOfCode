import pandas as pd
import matplotlib.pyplot as plt

def main():
  buildGraphs(2022)

def buildGraphs(year: int):
  df = pd.read_csv(f"../data/performanceDF.csv", delimiter=',')
  df.replace('DNF__', 0, inplace=True)
  df['go'] = df['go'].astype(float)*1000
  df['rust'] = df['rust'].astype(float)*1000
  df['python'] = df['python'].astype(float)*1000
  df['goCompile'] = df['goCompile'].astype(float)*1000
  df['rustCompile'] = df['rustCompile'].astype(float)*1000

  # speeds graph
  plt.figure(dpi = 300)
  plt.yscale('log')
  plt.plot(df['day'], df['go'], label='golang')
  plt.plot(df['day'], df['rust'], label='rust')
  plt.plot(df['day'], df['python'], label='python')
  plt.title("Performance of select languages for Advent of Code 2022")
  plt.xlabel('Day')
  plt.ylabel('Runtime (milliseconds)')
  plt.legend()
  plt.savefig(f"../{year}_speed.png", bbox_inches='tight')

  # speeds table
  # TODO

  # LOC graph
  plt.figure(dpi = 300)
  plt.plot(df['day'], df['goLOC'], label='go')
  plt.plot(df['day'], df['rustLOC'], label='rust')
  plt.plot(df['day'], df['pythonLOC'], label='python')
  plt.title("LOC of select languages for Advent of Code 2022")
  plt.xlabel('Day')
  plt.ylabel('Lines of Code')
  plt.legend()
  plt.savefig(f"../{year}_LOC.png", bbox_inches='tight')

  # LOC table
  # TODO

  # compiler graph
  plt.figure(dpi = 300)
  plt.yscale('log')
  plt.plot(df['day'], df['goCompile'], label='golang')
  plt.plot(df['day'], df['rustCompile'], label='rust')
  plt.title("Compiler speeds for Advent of Code 2022")
  plt.xlabel('Day')
  plt.ylabel('Time to Compile (milliseconds)')
  plt.legend()
  plt.savefig(f"../{year}_compilerSpeed.png", bbox_inches='tight')

  # compiler table
  # TODO

if __name__ == "__main__":
  main()