import matplotlib.pyplot as plt
M = range(0, 100, 10)
Q_X = [0.5 * m for m in M]
plt.plot(M, Q_X, label='Кривая Энгеля для X')
plt.xlabel('Доход (M)')
plt.ylabel('Q_X')
plt.grid()
plt.legend()