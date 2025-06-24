# 🔬 Investigación de Análisis Numérico: Técnicas de Descenso de Gradiente

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![LaTeX](https://img.shields.io/badge/LaTeX-Document-green.svg)](https://www.latex-project.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Este proyecto implementa y compara diferentes técnicas de descenso de gradiente estocástico y sus variantes para entrenar un modelo de regresión logística en el dataset Iris.

## 📁 Estructura del Proyecto (Mejorada)

```
Investigación AN/
├── 📄 main.py                         # Script principal para ejecutar todo
├── 📄 requirements.txt                # Dependencias de Python
├── 📄 README.md                       # Este archivo
├── 📄 LICENSE                         # Licencia del proyecto
│
├── 📁 src/                            # Código fuente modular
│   ├── 📄 __init__.py
│   ├── 📄 experiment.py               # Clase principal del experimento
│   ├── 📁 optimizers/                 # Implementaciones de optimizadores
│   │   ├── 📄 __init__.py
│   │   ├── 📄 base.py                 # Clase base abstracta
│   │   ├── 📄 sgd.py                  # SGD y SGD+Momentum
│   │   ├── 📄 rmsprop.py              # RMSProp optimizer
│   │   └── 📄 adam.py                 # Adam optimizer
│   └── 📁 utils/                      # Utilidades y herramientas
│       ├── 📄 __init__.py
│       ├── 📄 data_utils.py           # Procesamiento de datos
│       └── 📄 plotting.py             # Funciones de visualización
│
├── 📁 config/                         # Configuraciones del proyecto
│   ├── 📄 __init__.py
│   └── 📄 settings.py                 # Parámetros y configuraciones
│
├── 📁 docs/                           # Documentación LaTeX
│   ├── 📄 main.tex                    # Documento principal
|   ├── 📄 presentacion.tex            # Presentación del proyecto
│   └── 📄 curvas_convergencia.pdf     # Gráficos para LaTeX
│
├── 📁 scripts/                        # Scripts de automatización
│   ├── 📄 make.py                     # Script tipo "Makefile"
│   ├── 📄 compile_document.py         # Compilador LaTeX mejorado
│   ├── 📄 compile_latex.bat           # Script batch original
│   ├── 📄 create_latex_plots.py       # Generador de gráficos
│   └── 📄 run_experiment.py           # Ejecutor de experimentos
│
├── 📁 results/                        # Resultados y salidas
│   ├── 📄 experiment_results.txt      # Resultados detallados
│   └── 📁 figures/                    # Gráficos generados
│       ├── 📄 convergencia_optimizadores.png
│       └── 📄 convergencia_optimizadores.pdf
│
└── 📁 legacy/                         # Archivos originales (opcional)
    ├── 📄 gradient_descent_experiment.py
    └── 📄 create_pdf_plot.py
```

## 🚀 Inicio Rápido

### Método 1: Script Principal (Recomendado)
```bash
# Ejecutar todo el pipeline
python main.py
```

### Método 2: Usando el Sistema de Automatización
```bash
# Ver comandos disponibles
python scripts/make.py

# Ejecutar pipeline completo
python scripts/make.py all

# Solo experimento
python scripts/make.py experiment

# Solo compilación LaTeX
python scripts/make.py latex
```

## 📋 Requisitos

### Python
- Python 3.7+
- numpy >= 1.21.0
- matplotlib >= 3.5.0
- scikit-learn >= 1.0.0

### LaTeX
- Distribución LaTeX (TeX Live, MiKTeX, TinyTeX)
- pdflatex

## 🔧 Instalación

1. **Clonar/Descargar el proyecto**
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   # O usando el script de automatización:
   python scripts/make.py install
   ```

## 📊 Uso Detallado

### 1. Ejecutar Experimentos Completos
```bash
python main.py
```
Esto ejecutará:
- ✅ Preparación de datos del dataset Iris
- ✅ Entrenamiento con todos los optimizadores
- ✅ Generación de gráficos (PNG y PDF)
- ✅ Guardado de resultados detallados

### 2. Compilar Documento LaTeX
```bash
# Método mejorado (recomendado)
python scripts/compile_document.py

# Método tradicional
python scripts/make.py latex
```

### 3. Generar Solo Gráficos
```bash
python scripts/create_latex_plots.py
```

### 4. Limpiar Archivos Temporales
```bash
python scripts/make.py clean
```

## 🧪 Configuración de Experimentos

Edita `config/settings.py` para personalizar:

```python
# Parámetros del experimento
EXPERIMENT_CONFIG = {
    'random_seed': 42,
    'test_size': 0.2,
    'epochs': 30,
    # ...
}

# Configuración de optimizadores
OPTIMIZER_CONFIGS = {
    'SGD': {'learning_rate': 0.05},
    'Adam': {'learning_rate': 0.05, 'beta1': 0.9},
    # ...
}
```

## 📈 Algoritmos Implementados

1. **SGD Básico**: Descenso de gradiente estocástico estándar
2. **SGD + Momentum**: SGD con término de impulso
3. **RMSProp**: Método adaptativo con ajuste de tasa de aprendizaje
4. **Adam**: Combina momentum y RMSProp

## 📊 Resultados

Los resultados se guardan automáticamente en:
- `results/experiment_results.txt` - Resumen detallado
- `results/figures/` - Gráficos en PNG y PDF
- `docs/curvas_convergencia.pdf` - Gráfico para LaTeX

## 🛠️ Desarrollo

### Estructura Modular
- **`src/optimizers/`**: Cada optimizador en su propio archivo
- **`src/utils/`**: Funciones de utilidad reutilizables
- **`config/`**: Configuraciones centralizadas
- **`scripts/`**: Scripts de automatización

### Agregar Nuevo Optimizador
1. Crear archivo en `src/optimizers/`
2. Heredar de `BaseOptimizer`
3. Implementar método `update_weights()`
4. Agregar configuración en `config/settings.py`

## 🐛 Solución de Problemas

### Error: Módulos no encontrados
```bash
pip install -r requirements.txt
```

### Error: LaTeX no compilado
```bash
# Verificar instalación
python scripts/compile_document.py
```

### Error: Archivos no encontrados
```bash
# Limpiar y regenerar
python scripts/make.py clean
python scripts/make.py all
```

## 📝 Citas y Referencias

```bibtex
@article{ruder2016overview,
  title={An overview of gradient descent optimization algorithms},
  author={Ruder, Sebastian},
  journal={arXiv preprint arXiv:1609.04747},
  year={2016}
}
```

## 🤝 Contribuciones

Este proyecto fue desarrollado como parte de una investigación en Análisis Numérico sobre métodos de optimización en machine learning.

**Autores**: Juan Pérez, Ana Gómez

## 📄 Licencia

MIT License - Ver archivo `LICENSE` para detalles.

---

⭐ **¿Te gusta este proyecto?** ¡Dale una estrella y compártelo!

🔗 **Enlaces útiles:**
- [Documentación de NumPy](https://numpy.org/doc/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
