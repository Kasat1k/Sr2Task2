import numpy as np
import matplotlib.pyplot as plt

# Матриця переходів для поглинаючого ланцюга
transition_matrix_absorbing = np.array([
    [1, 0, 0, 0, 0, 0, 0],
    [0.3, 0.7, 0, 0, 0, 0, 0],
    [0.4, 0.2, 0.4, 0, 0, 0, 0],
    [0.2, 0.3, 0.5, 0, 0, 0, 0],
    [0, 0.2, 0.3, 0.5, 0, 0, 0],
    [0, 0, 0.4, 0.3, 0.3, 0, 0],
    [0, 0, 0, 0, 0.3, 0.7, 0]
])

# Початковий вектор станів
initial_state = np.array([0, 1, 0, 0, 0, 0, 0])

# Функція для моделювання поглинаючого ланцюга Маркова
def simulate_absorbing_chain(transition_matrix, initial_state, max_steps=100):
    current_state = np.random.choice(len(initial_state), p=initial_state)
    states = [current_state]
    for _ in range(max_steps):
        if transition_matrix[current_state, current_state] == 1:  # Поглинаючий стан
            break
        current_state = np.random.choice(
            len(transition_matrix),
            p=transition_matrix[current_state]
        )
        states.append(current_state)
    return states

# Змоделюємо більше 100 реалізацій
num_realizations = 100
realizations = [simulate_absorbing_chain(transition_matrix_absorbing, initial_state) for _ in range(num_realizations)]

# Графік реалізацій
fig, ax = plt.subplots(figsize=(10, 6))
for i, realization in enumerate(realizations[:10]):  # Візуалізуємо перші 10 реалізацій
    ax.plot(range(len(realization)), realization, marker='o', label=f'Реалізація {i+1}')

ax.set_title('Реалізації поглинаючого ланцюга Маркова')
ax.set_xlabel('Крок')
ax.set_ylabel('Стан')
ax.grid(alpha=0.7)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
plt.tight_layout()
plt.show()
