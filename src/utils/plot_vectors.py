import matplotlib.pyplot as plt
import numpy as np

def plot_vectors(title, vectors, determinant = False):
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    colors = ['magenta', 'orange']

    for i, (x, y) in enumerate(vectors):
        plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=colors[i])
        pos_x = x + 0.1
        pos_y = y + 0.1 if y >= 0 else y - 0.4
        plt.text(pos_x, pos_y, f"({x}, {y})", fontsize=12, color=colors[i])

    if determinant:
        det_val = np.linalg.det(vectors)
        area = abs(det_val)

        parallelogram = np.array([[0, 0], vectors[0], vectors[0] + vectors[1], vectors[1]])

        plt.fill(parallelogram[:, 0], parallelogram[:, 1], color='red', alpha=0.2, label=f'det = {area:.2f}')
        plt.legend()

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.xticks(range(-5, 6))
    plt.yticks(range(-5, 6))

    plt.title(title)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()