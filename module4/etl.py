SMA_WINDOW_SIZE = 5

def extract(filename):
    """
    Extracts data from a CSV file and returns it as a list.
    """
    extracted_data = []

    with open(filename, 'r') as data_file:
        for datum in data_file:
            extracted_data.append(tuple(datum.strip().split('\t')))

    return extracted_data[1:]

def transform(data):
    """
    Transforms a list of x,y values to compute an SMA for y values.
    Returns a list of tuples (x,y') where y' is the SMA value computed
    """
    transformed_data = [] # The SMA data

    for index, datum in enumerate(data):
      if index < SMA_WINDOW_SIZE:
          transformed_data.append((datum[0],0))
      else:
          sma = 0
          for i in range(SMA_WINDOW_SIZE):
              sma += float(data[index - i][1])
          sma = sma/SMA_WINDOW_SIZE
          transformed_data.append((datum[0],sma))

    return transformed_data
