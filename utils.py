import numpy as np

def convolve1d(I, G, axis=0):
  """
  Perform a 1D convolution for image I with mask G along a specified axis.

  :I: Input image.
  :G: Convolution mask.
  :axis: Axis for convoltion. 0 = Rows, 1 = Columns.
  """

  if (axis == 0):

    result = np.ones(I.shape, dtype=I.dtype)

    # Perform convolution in every row.
    for row in range(I.shape[0]):
      result[row, :] = np.convolve(I[row, :], G, mode='same')

    return result
    
  elif (axis == 1):

    result = np.ones(I.shape, dtype=I.dtype)

    # Perform convolution in every column.
    for col in range(I.shape[1]):
      result[:, col] = np.convolve(I[:, col], G, mode='same')

    return result

  else:
    print("Error: Invalid axis.")
    return