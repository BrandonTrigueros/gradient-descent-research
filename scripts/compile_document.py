"""
Enhanced compilation script for LaTeX document.
Fixed version with proper Windows console compatibility.
"""

import subprocess
import sys
import os
from pathlib import Path


def safe_print(message):
    """Print message with fallback for encoding issues."""
    try:
        print(message)
    except UnicodeEncodeError:
        # Fallback to ASCII-safe version without emoji
        clean_message = (message
                        .replace("📄", "[DOC]")
                        .replace("🔄", "[RUN]")
                        .replace("✅", "[OK]")
                        .replace("❌", "[ERR]")
                        .replace("🎉", "[SUCCESS]")
                        .replace("📊", "[INFO]")
                        .replace("🎯", "[DONE]")
                        .replace("💥", "[FAIL]")
                        .replace("💡", "[TIP]"))
        print(clean_message)


def compile_latex_document(tex_file: str = "main.tex", output_dir: str = "docs"):
    """
    Compile LaTeX document with proper error handling.
    
    Args:
        tex_file (str): Name of the main .tex file
        output_dir (str): Directory containing the .tex file
    """
    project_root = Path(__file__).parent.parent
    tex_path = project_root / output_dir / tex_file
    
    if not tex_path.exists():
        safe_print(f"❌ Error: No se encontró el archivo {tex_path}")
        return False
    
    # Change to the document directory
    os.chdir(tex_path.parent)
    
    safe_print(f"📄 Compilando documento LaTeX: {tex_file}")
    safe_print("=" * 50)
    
    try:
        # First compilation
        safe_print("🔄 Primera compilación...")
        result1 = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file],
            capture_output=True,
            text=True
        )
        
        if result1.returncode != 0:
            safe_print("❌ Error en la primera compilación:")
            safe_print(result1.stderr)
            return False
        
        safe_print("✅ Primera compilación completada")
        
        # Second compilation (for references)
        safe_print("🔄 Segunda compilación (referencias)...")
        result2 = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file],
            capture_output=True,
            text=True
        )
        
        if result2.returncode != 0:
            safe_print("❌ Error en la segunda compilación:")
            safe_print(result2.stderr)
            return False
        
        safe_print("✅ Segunda compilación completada")
        
        # Check if PDF was generated
        pdf_file = tex_path.with_suffix('.pdf')
        if pdf_file.exists():
            safe_print(f"🎉 Documento PDF generado exitosamente: {pdf_file}")
            
            # Show file size
            size_kb = pdf_file.stat().st_size / 1024
            safe_print(f"📊 Tamaño del archivo: {size_kb:.1f} KB")
            
            return True
        else:
            safe_print("❌ Error: No se generó el archivo PDF")
            return False
            
    except FileNotFoundError:
        safe_print("❌ Error: pdflatex no está instalado o no está en el PATH")
        safe_print("💡 Instala TeX Live, MiKTeX o TinyTeX para compilar documentos LaTeX")
        return False
    except Exception as e:
        safe_print(f"❌ Error inesperado: {e}")
        return False


def main():
    """Main function to compile LaTeX document."""
    success = compile_latex_document()
    
    if success:
        safe_print("\n🎯 Compilación exitosa!")
        safe_print("Puedes abrir el archivo main.pdf para ver el documento.")
    else:
        safe_print("\n💥 La compilación falló.")
        safe_print("Revisa los errores anteriores para diagnosticar el problema.")
        sys.exit(1)


if __name__ == "__main__":
    main()
