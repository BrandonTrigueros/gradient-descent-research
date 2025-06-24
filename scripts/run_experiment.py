"""
Script to run the complete gradient descent experiment.
"""

import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.experiment import GradientDescentExperiment


def main():
    """Run the complete experiment."""
    print("Iniciando experimento de optimización de descenso de gradiente...\n")
    
    # Create and run experiment
    experiment = GradientDescentExperiment(epochs=30, random_state=42)
    results, costs = experiment.run_full_experiment()
    
    print("\n¡Experimento completado exitosamente!")
    print("Revisa la carpeta 'output' para los resultados detallados.")
    
    return results, costs


if __name__ == "__main__":
    results, costs = main()
