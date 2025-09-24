import pytest

# Ejecuta todos los tests dentro de la carpeta 'tests'
# -q : modo quiet (resumen corto)
# --tb=short : traceback corto
# --maxfail=3 : detenerse después de 3 fallos (opcional)
exit_code = pytest.main(["app/tests", "-q", "--tb=short"])

# exit_code = 0 -> todos pasaron
# exit_code = 1 -> algún fallo
if exit_code == 0:
    print("\n✅ Todos los tests pasaron correctamente.")
else:
    print(f"\n❌ Algunos tests fallaron. Código de salida: {exit_code}")
