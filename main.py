"""
Main script to run all experiments and generate complete results.
"""

import sys
import os
from pathlib import Path

# Add src to Python path and get project root
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / 'src'))

from src.experiment import GradientDescentExperiment
from src.utils import plot_convergence_curves, save_results_to_file
from config import EXPERIMENT_CONFIG, PLOT_CONFIG, PATHS


def main():
    """Run complete experiment pipeline."""
    print("🔬 Iniciando experimentos de descenso de gradiente")
    print("=" * 60)
    
    # Ensure results directories exist
    results_dir = Path(PATHS['results_dir'])
    figures_dir = Path(PATHS['figures_dir'])
    results_dir.mkdir(exist_ok=True)
    figures_dir.mkdir(exist_ok=True)
    
    # Initialize and run experiment
    experiment = GradientDescentExperiment(
        epochs=EXPERIMENT_CONFIG['epochs'],
        random_state=EXPERIMENT_CONFIG['random_seed']
    )
    
    print("📊 Preparando datos del dataset Iris...")
    experiment.prepare_data()
    
    print("🚀 Ejecutando optimizadores...")
    experiment.run_optimizers()
    
    print("📈 Generando visualizaciones...")
    # Generate plots
    png_path = figures_dir / "convergencia_optimizadores.png"
    pdf_path = figures_dir / "convergencia_optimizadores.pdf"
    latex_pdf_path = Path(PATHS['docs_dir']) / "curvas_convergencia.pdf"
    
    # Create plots
    plot_convergence_curves(
        experiment.costs_dict,
        save_path=str(png_path),
        title="Convergencia de Métodos de Optimización - Dataset Iris"
    )
    
    plot_convergence_curves(
        experiment.costs_dict,
        save_path=str(pdf_path),
        title="Convergencia de Métodos de Optimización - Dataset Iris"
    )
    
    # Copy PDF for LaTeX
    plot_convergence_curves(
        experiment.costs_dict,
        save_path=str(latex_pdf_path),
        title="Convergencia de Métodos de Optimización - Dataset Iris"
    )
    
    print("💾 Guardando resultados...")
    # Save detailed results
    results_file = results_dir / "experiment_results.txt"
    save_results_to_file(
        experiment.results,
        experiment.costs_dict,
        str(results_file)
    )
    
    # Print summary
    print("\n📋 RESUMEN DE RESULTADOS")
    print("-" * 60)
    for method, result in experiment.results.items():
        print(f"{method:15} | "
              f"Costo: {result['final_cost']:.4f} | "
              f"Precisión: {result['test_accuracy']:.2%}")
    
    print(f"\n✅ Experimento completado!")
    print(f"📁 Resultados guardados en: {results_dir}")
    print(f"🖼️  Gráficos generados en: {figures_dir}")
    print(f"📄 Gráfico LaTeX en: {latex_pdf_path}")


if __name__ == "__main__":
    main()
