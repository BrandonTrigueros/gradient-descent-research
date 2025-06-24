"""
Makefile equivalent for Windows - Project automation script.
"""

import sys
import subprocess
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """Run a command and return success status."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(f"✅ {description} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e}")
        return False


def main():
    """Main automation script."""
    if len(sys.argv) < 2:
        print("📝 Uso: python scripts/make.py <comando>")
        print("\nComandos disponibles:")
        print("  install     - Instalar dependencias de Python")
        print("  experiment  - Ejecutar experimento completo")
        print("  plots       - Generar solo gráficos")
        print("  latex       - Compilar documento LaTeX")
        print("  clean       - Limpiar archivos temporales")
        print("  all         - Ejecutar todo el pipeline")
        return
    
    command = sys.argv[1].lower()
    project_root = Path(__file__).parent.parent
    
    if command == "install":
        run_command(
            "pip install -r requirements.txt",
            "Instalando dependencias de Python"
        )
    
    elif command == "experiment":
        run_command(
            "python main.py",
            "Ejecutando experimento completo"
        )
    
    elif command == "plots":
        run_command(
            "python scripts/create_latex_plots.py",
            "Generando gráficos para LaTeX"
        )
    
    elif command == "latex":
        run_command(
            "python scripts/compile_document.py",
            "Compilando documento LaTeX"
        )
    
    elif command == "clean":
        print("🧹 Limpiando archivos temporales...")
        
        # LaTeX temporary files
        latex_temps = ["*.aux", "*.log", "*.out", "*.toc", "*.lof", "*.lot"]
        for pattern in latex_temps:
            run_command(f"del docs\\{pattern} 2>nul", f"Eliminando {pattern}")
        
        # Python cache
        run_command(
            "rmdir /s /q __pycache__ 2>nul",
            "Eliminando caché de Python"
        )
        
        print("✅ Limpieza completada")
    
    elif command == "all":
        steps = [
            ("python main.py", "Ejecutando experimento completo"),
            ("python scripts/compile_document.py", "Compilando documento LaTeX")
        ]
        
        print("🚀 Ejecutando pipeline completo...")
        all_success = True
        
        for cmd, desc in steps:
            if not run_command(cmd, desc):
                all_success = False
                break
        
        if all_success:
            print("🎉 Pipeline completo ejecutado exitosamente!")
        else:
            print("💥 Pipeline falló en algún paso")
    
    else:
        print(f"❌ Comando desconocido: {command}")
        print("Usa 'python scripts/make.py' para ver comandos disponibles")


if __name__ == "__main__":
    main()
