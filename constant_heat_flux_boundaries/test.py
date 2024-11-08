import numpy as np

original_list = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
left_end = -2.1
right_end = 2.1
n = 4

left_extension = np.linspace(left_end, original_list[0], num=n+1, endpoint=True).tolist()
right_extension = np.linspace(original_list[-1], right_end, num=n+1, endpoint=True)[1:].tolist()

extended_list = left_extension + original_list + right_extension

print(extended_list)
