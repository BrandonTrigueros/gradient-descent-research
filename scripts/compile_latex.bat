@echo off
cd /d "c:\Users\Brandon\Desktop\Investigación AN"

echo Compilando documento LaTeX...
pdflatex main.tex
echo.
echo Primera compilación completada.
echo.
echo Compilando referencias...
pdflatex main.tex
echo.
echo Segunda compilación completada.
echo.
echo Documento PDF generado: main.pdf

pause
