# Procesos de instalacion de fathon

# Tipos de instalacion

- [Conda](#Conda)
- [Python3](#Python)
  - Se requiere el script de este repositorio

## Conda

### Primero se requiere crear un entorno virual con python 3.8
```bash
conda create --name {entorno} python=3.8
```

### Activar el entorno

```bash
conda activate {entorno}
```

### Instalar las librerias necesarias

```bash
pip install matplotlib
pip install fathon
```

## Python

### Para python se requiere ejecutar un script que proporciono aqui

```bash
git clone https://github.com/BAN03/fathon-instalation
cd fathon-instalation
```

### Instalamos las dependencias, clonamos y ejecutamos el script

```bash
sudo apt install libgsl-dev python3-numpy python3-matplotlib cython3
git clone https://github.com/stfbnc/fathon
python3 repo_changes.py
```

### Construimos e instalamos la libreria

```bash
cd fathon 
python3 setup.py build
sudo python3 setup.py install
cythonize -a -i fathon/*.pyx
```

