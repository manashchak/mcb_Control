#%% [Imports]
import control as ct
import matplotlib.pyplot as plt
import numpy as np

#%% [Testing]

#* Example transfer function: G(s) = 1 / (s^2 + 2s + 1)
sys_from_tf = ct.tf([1], [1, 2, 1])
#* State space representation:
A = np.array([[0, 1], [-1, -2]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])
sys_from_ss = ct.ss(A, B, C, D)



# %%
