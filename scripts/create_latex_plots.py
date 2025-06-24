"""
Script to generate plots for LaTeX document.
"""

import sys
import os
import numpy as np

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import from src package
from src.experiment import GradientDescentExperiment
from src.utils import plot_convergence_curves


def create_latex_plots():
    """Create plots specifically formatted for LaTeX document."""
    print("Generando gráficos para documento LaTeX...\n")
    
    # Run experiment to get data
    experiment = GradientDescentExperiment(epochs=30, random_state=42)
    experiment.prepare_data()
    experiment.run_optimizers()
    
    # Create plots directory
    plots_dir = os.path.join("..", "docs")
    os.makedirs(plots_dir, exist_ok=True)
    
    # Generate LaTeX-compatible PDF plot
    pdf_path = os.path.join(plots_dir, "curvas_convergencia.pdf")
    plot_convergence_curves(
        experiment.costs_dict, 
        save_path=pdf_path,
        title="Convergencia de Métodos de Optimización - Dataset Iris"
    )
    
    print(f"Gráfico PDF para LaTeX guardado en: {pdf_path}")
    print("¡Listo para incluir en el documento LaTeX!")


if __name__ == "__main__":
    create_latex_plots()
