"""
Plotting utilities for visualization.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Optional
import os


def plot_convergence_curves(costs_dict: Dict[str, List[float]], 
                          save_path: Optional[str] = None,
                          title: str = "Convergencia de Métodos de Optimización - Dataset Iris",
                          figsize: tuple = (10, 6)) -> None:
    """
    Plot convergence curves for different optimizers.
    
    Args:
        costs_dict (Dict[str, List[float]]): Dictionary with method names and their cost histories
        save_path (Optional[str]): Path to save the figure
        title (str): Title for the plot
        figsize (tuple): Figure size
    """
    plt.figure(figsize=figsize)
    plt.rcParams.update({'font.size': 12})
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    linestyles = ['-', '--', '-.', ':']
    markers = ['o', 's', '^', 'D']
    
    for i, (method, costs) in enumerate(costs_dict.items()):
        plt.plot(range(1, len(costs) + 1), costs, 
                color=colors[i % len(colors)], 
                linestyle=linestyles[i % len(linestyles)], 
                linewidth=2.5, label=method, 
                marker=markers[i % len(markers)], 
                markersize=5, markevery=3)
    
    plt.xlabel('Época', fontsize=14)
    plt.ylabel('Función de Costo (Pérdida)', fontsize=14)
    plt.title(title, fontsize=16)
    plt.legend(fontsize=12, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.xlim(1, len(list(costs_dict.values())[0]))
    
    if save_path:
        # Ensure directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, format='pdf', dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado en: {save_path}")
    
    plt.show()


def create_results_table(results: Dict[str, Dict]) -> None:
    """
    Print a formatted results table.
    
    Args:
        results (Dict[str, Dict]): Results dictionary with method names and metrics
    """
    print("\n" + "=" * 80)
    print("RESULTADOS FINALES DEL EXPERIMENTO")
    print("=" * 80)
    print(f"{'Método':<15} {'Costo Final':<12} {'Precisión Entreno':<18} {'Precisión Prueba':<15}")
    print("-" * 80)
    
    for method_name, result in results.items():
        print(f"{method_name:<15} {result['final_cost']:<12.4f} "
              f"{result['train_accuracy']:<18.2%} {result['test_accuracy']:<15.2%}")
    
    print("-" * 80)


def save_results_to_file(results: Dict[str, Dict], costs_dict: Dict[str, List[float]], 
                        filepath: str) -> None:
    """
    Save experiment results to a text file.
    
    Args:
        results (Dict[str, Dict]): Results dictionary
        costs_dict (Dict[str, List[float]]): Cost histories
        filepath (str): Path to save the results file
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("RESULTADOS DEL EXPERIMENTO DE OPTIMIZACIÓN\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("Configuración del Experimento:\n")
        f.write("- Dataset: Iris (Versicolor vs Virginia)\n")
        f.write("- Características: 4 features + bias term\n")
        f.write("- División: 80% entrenamiento, 20% prueba\n")
        f.write("- Épocas: 30\n\n")
        
        f.write("Resultados Finales:\n")
        f.write("-" * 30 + "\n")
        for method_name, result in results.items():
            f.write(f"{method_name}:\n")
            f.write(f"  - Costo Final: {result['final_cost']:.4f}\n")
            f.write(f"  - Precisión Entrenamiento: {result['train_accuracy']:.2%}\n")
            f.write(f"  - Precisión Prueba: {result['test_accuracy']:.2%}\n\n")
        
        f.write("Historial de Costos por Época:\n")
        f.write("-" * 30 + "\n")
        epochs = len(list(costs_dict.values())[0])
        f.write("Época\t" + "\t".join(costs_dict.keys()) + "\n")
        for epoch in range(epochs):
            f.write(f"{epoch+1}\t")
            f.write("\t".join([f"{costs[epoch]:.4f}" for costs in costs_dict.values()]))
            f.write("\n")
    
    print(f"Resultados guardados en: {filepath}")
