"""
Main experiment runner for gradient descent optimization comparison.
"""

import numpy as np
import sys
import os
from typing import Dict, List, Tuple

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from optimizers import SGD, SGDMomentum, RMSProp, Adam
from utils import (prepare_iris_data, split_data, plot_convergence_curves, 
                   create_results_table, save_results_to_file)


class GradientDescentExperiment:
    """
    Main experiment class for comparing gradient descent optimizers.
    """
    
    def __init__(self, epochs: int = 30, random_state: int = 42):
        """
        Initialize the experiment.
        
        Args:
            epochs (int): Number of training epochs
            random_state (int): Random state for reproducibility
        """
        self.epochs = epochs
        self.random_state = random_state
        self.optimizers = {
            'SGD': SGD(learning_rate=0.05),
            'SGD + Momentum': SGDMomentum(learning_rate=0.03, momentum=0.9),
            'RMSProp': RMSProp(learning_rate=0.05, rho=0.9),
            'Adam': Adam(learning_rate=0.05, beta1=0.9, beta2=0.999)
        }
        self.results = {}
        self.costs_dict = {}
    
    def prepare_data(self) -> None:
        """Prepare and split the Iris dataset."""
        print("1. Preparando datos...")
        
        # Prepare Iris data
        X, y = prepare_iris_data()
        
        # Split into train/test
        self.X_train, self.X_test, self.y_train, self.y_test = split_data(
            X, y, test_size=0.2, random_state=self.random_state
        )
        
        print(f"   - Datos de entrenamiento: {self.X_train.shape[0]} muestras")
        print(f"   - Datos de prueba: {self.X_test.shape[0]} muestras")
        print(f"   - Características: {self.X_train.shape[1] - 1} + bias\n")
    
    def run_optimizers(self) -> None:
        """Run all optimizers and collect results."""
        print("2. Entrenando modelos...")
        
        # Set random seed for reproducibility
        np.random.seed(self.random_state)
        
        for name, optimizer in self.optimizers.items():
            print(f"   - Entrenando con {name}...")
            
            # Reset random seed for fair comparison
            np.random.seed(self.random_state)
            
            # Train the optimizer
            final_weights, cost_history = optimizer.optimize(
                self.X_train, self.y_train, self.epochs
            )
            
            # Evaluate on train and test sets
            train_accuracy = optimizer.evaluate_accuracy(final_weights, self.X_train, self.y_train)
            test_accuracy = optimizer.evaluate_accuracy(final_weights, self.X_test, self.y_test)
            
            # Store results
            self.results[name] = {
                'weights': final_weights,
                'final_cost': cost_history[-1],
                'train_accuracy': train_accuracy,
                'test_accuracy': test_accuracy,
                'optimizer': optimizer
            }
            self.costs_dict[name] = cost_history
    
    def display_results(self) -> None:
        """Display experiment results."""
        create_results_table(self.results)
    
    def save_results(self, output_dir: str = "output") -> None:
        """
        Save results and generate plots.
        
        Args:
            output_dir (str): Directory to save outputs
        """
        print("\n3. Guardando resultados...")
        
        # Create output directories
        figures_dir = os.path.join(output_dir, "figures")
        os.makedirs(figures_dir, exist_ok=True)
        
        # Save convergence plot as PDF
        pdf_path = os.path.join(figures_dir, "curvas_convergencia.pdf")
        plot_convergence_curves(self.costs_dict, save_path=pdf_path)
        
        # Save convergence plot as PNG
        png_path = os.path.join(figures_dir, "curvas_convergencia.png")
        plot_convergence_curves(self.costs_dict, save_path=png_path)
        
        # Save detailed results to text file
        results_path = os.path.join(output_dir, "experiment_results.txt")
        save_results_to_file(self.results, self.costs_dict, results_path)
    
    def run_full_experiment(self) -> Tuple[Dict, Dict]:
        """
        Run the complete experiment.
        
        Returns:
            Tuple[Dict, Dict]: Results and cost histories
        """
        print("=== EXPERIMENTO DE OPTIMIZACIÓN CON DATASET IRIS ===\n")
        
        # Prepare data
        self.prepare_data()
        
        # Run optimizers
        self.run_optimizers()
        
        # Display results
        self.display_results()
        
        # Save results
        self.save_results()
        
        return self.results, self.costs_dict


def main():
    """Main function to run the experiment."""
    experiment = GradientDescentExperiment(epochs=30, random_state=42)
    results, costs = experiment.run_full_experiment()
    return results, costs


if __name__ == "__main__":
    results, costs = main()
