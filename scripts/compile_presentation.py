"""
Script to compile the Beamer presentation.
"""

import subprocess
import sys
import os
from pathlib import Path


def compile_presentation():
    """Compile the Beamer presentation."""
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / "docs"
    presentation_tex = docs_dir / "presentacion.tex"
    
    if not presentation_tex.exists():
        print(f"❌ Error: No se encontró el archivo {presentation_tex}")
        return False
    
    # Change to docs directory
    os.chdir(docs_dir)
    
    print("📄 Compilando presentación Beamer...")
    print("=" * 50)
    
    try:
        # First compilation
        print("🔄 Primera compilación...")
        result1 = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "presentacion.tex"],
            capture_output=True,
            text=True
        )
        
        if result1.returncode != 0:
            print("❌ Error en la primera compilación:")
            print(result1.stderr)
            return False
        
        print("✅ Primera compilación completada")
        
        # Second compilation (for navigation and references)
        print("🔄 Segunda compilación (navegación)...")
        result2 = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "presentacion.tex"],
            capture_output=True,
            text=True
        )
        
        if result2.returncode != 0:
            print("❌ Error en la segunda compilación:")
            print(result2.stderr)
            return False
        
        print("✅ Segunda compilación completada")
        
        # Check if PDF was generated
        pdf_file = presentation_tex.with_suffix('.pdf')
        if pdf_file.exists():
            print(f"🎉 Presentación PDF generada exitosamente: {pdf_file.name}")
            
            # Show file size
            size_kb = pdf_file.stat().st_size / 1024
            print(f"📊 Tamaño del archivo: {size_kb:.1f} KB")
            print(f"📄 Páginas: Aproximadamente 23 páginas")
            
            return True
        else:
            print("❌ Error: No se generó el archivo PDF")
            return False
            
    except FileNotFoundError:
        print("❌ Error: pdflatex no está instalado o no está en el PATH")
        print("💡 Instala TeX Live, MiKTeX o TinyTeX para compilar documentos LaTeX")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False


def main():
    """Main function."""
    print("🎯 Compilador de Presentación Beamer")
    print("====================================\n")
    
    success = compile_presentation()
    
    if success:
        print("\n🎯 ¡Compilación exitosa!")
        print("📖 Puedes abrir el archivo presentacion.pdf para ver la presentación.")
        print("💡 La presentación tiene 23 diapositivas con navegación interactiva.")
    else:
        print("\n💥 La compilación falló.")
        print("🔍 Revisa los errores anteriores para diagnosticar el problema.")
        sys.exit(1)


if __name__ == "__main__":
    main()
